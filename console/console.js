/* DR.X Console — render layer.
 *
 * Renders window.__DRX_STATE__, produced by scripts/build_console_state.py.
 * This file computes no figures of its own: it formats, orders, and labels the
 * values it is handed. If a number is wrong, the fix belongs in the extractor
 * or in the contract file the extractor read.
 */
(function () {
  "use strict";

  var STATES = ["proven", "partial", "unproven", "failed", "stale"];

  var STATE_LABEL = {
    proven: "proven",
    partial: "partial",
    unproven: "not run",
    failed: "failed",
    stale: "stale",
  };

  var STATE_MEANING = {
    proven: "Executed, evidence recorded, current.",
    partial: "Some evidence recorded, coverage incomplete.",
    unproven: "Defined but never executed.",
    failed: "Executed and did not pass.",
    stale: "Evidence predates a material change.",
  };

  /* Helpers ------------------------------------------------------------- */

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    if (attrs) {
      Object.keys(attrs).forEach(function (key) {
        var value = attrs[key];
        if (value === null || value === undefined || value === false) return;
        if (key === "text") node.textContent = value;
        else if (key === "class") node.className = value;
        else node.setAttribute(key, value);
      });
    }
    (children || []).forEach(function (child) {
      if (child === null || child === undefined) return;
      node.appendChild(typeof child === "string" ? document.createTextNode(child) : child);
    });
    return node;
  }

  function stateChip(state) {
    return el("span", { class: "state", "data-state": state }, [
      el("span", { class: "marker", "data-state": state, "aria-hidden": "true" }),
      el("span", { class: "label", text: STATE_LABEL[state] || state }),
    ]);
  }

  function distribution(counts, total) {
    var bar = el("div", { class: "dist", role: "img" });
    var described = [];
    STATES.forEach(function (state) {
      var n = counts[state] || 0;
      if (!n) return;
      described.push(n + " " + STATE_LABEL[state]);
      bar.appendChild(
        el("span", {
          "data-state": state,
          style: "flex: " + n + " 0 auto",
        })
      );
    });
    bar.setAttribute(
      "aria-label",
      total ? described.join(", ") + " of " + total : "no items recorded"
    );
    return bar;
  }

  function legend(counts) {
    var list = el("ul", { class: "legend" });
    STATES.forEach(function (state) {
      var n = counts[state] || 0;
      if (!n) return;
      list.appendChild(
        el("li", { title: STATE_MEANING[state] }, [
          el("span", { class: "marker", "data-state": state, style: "color: var(--st-" + state + ")" }),
          el("span", { class: "count", text: String(n) }),
          el("span", { text: STATE_LABEL[state] }),
        ])
      );
    });
    return list;
  }

  /* Bar and legend are one unit: the bar shows proportion, the legend states
   * the counts in words. Neither is decorative without the other. */
  function distributionBlock(counts, total) {
    return el("div", { class: "dist-group" }, [distribution(counts, total), legend(counts)]);
  }

  function provenance(sources) {
    var list = [].concat(sources || []).filter(Boolean);
    if (!list.length) return null;
    return el("p", { class: "provenance", text: "read from " + list.join(", ") });
  }

  function panel(id, title, lede, sources) {
    var head = el("div", { class: "panel-head" }, [
      el("div", {}, [el("h2", { id: id + "-title", text: title }), lede ? el("p", { class: "lede", text: lede }) : null]),
      provenance(sources),
    ]);
    return el("section", { class: "panel", id: id, "aria-labelledby": id + "-title" }, [head]);
  }

  function formatDate(value) {
    if (!value) return "unknown";
    var d = new Date(value);
    if (isNaN(d.getTime())) return String(value);
    return d.toLocaleString(undefined, {
      year: "numeric",
      month: "short",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
    });
  }

  /* Sections ------------------------------------------------------------- */

  function renderVerdict(state) {
    var v = state.verdict;
    var r = state.readiness || {};

    var blocking = el("ul", { class: "blocking" });
    (v.blocking || []).forEach(function (reason) {
      blocking.appendChild(el("li", { text: reason }));
    });

    var headline = el("div", { class: "verdict-headline" }, [
      stateChip(v.state),
      el("h2", { text: v.headline }),
      blocking,
      el("p", {
        class: "verdict-rule",
        text: "Verdict governed by " + v.governed_by + ". It never reads better than its worst material input.",
      }),
    ]);

    var readout = el("div", { class: "readout" }, [
      el("div", { class: "readout-value" }, [
        el("span", { text: r.score === null || r.score === undefined ? "—" : String(r.score) }),
        el("span", { class: "scale", text: "/ " + (r.scale || "10.5") }),
      ]),
      el("p", {
        class: "readout-caption",
        text: r.available
          ? "Knowledge readiness, assessed " + (r.assessed_on || "date not recorded") +
            ". Governed by the lowest material dimension" +
            (r.governing_dimension ? ", currently " + r.governing_dimension.toLowerCase() + "." : ".")
          : "areas/knowledge-readiness.md is not present.",
      }),
      provenance(r.source ? [r.source] : null),
    ]);

    return el("section", { class: "verdict", "data-state": v.state, "aria-labelledby": "verdict-title" }, [
      el("h2", { id: "verdict-title", class: "visually-hidden", text: "System verdict" }),
      headline,
      readout,
    ]);
  }

  function renderReadiness(state) {
    var r = state.readiness;
    var section = panel(
      "readiness",
      "Knowledge readiness",
      "Dimensions ordered lowest first, because the lowest governs the overall score. A strong project model cannot hide a weak one.",
      r && r.source ? [r.source] : null
    );

    if (!r || !r.available || !r.dimensions.length) {
      section.appendChild(
        el("p", { class: "empty" }, [
          "No assessment recorded. Populate ",
          el("span", { class: "mono", text: "areas/knowledge-readiness.md" }),
          " to fill this panel.",
        ])
      );
      return section;
    }

    var ladder = el("div", { class: "ladder" });
    var governing = r.governing_dimension;
    r.dimensions.forEach(function (dim) {
      var isGoverning = dim.name === governing;
      var pct = Math.max(0, Math.min(100, (dim.score / (r.scale || 10.5)) * 100));
      ladder.appendChild(
        el("div", { class: "rung", "data-governing": String(isGoverning) }, [
          el("div", { class: "rung-name" }, [
            el("span", { class: "text", text: dim.name, title: dim.name }),
          ]),
          el("div", { class: "rung-track" }, [
            el("div", { class: "rung-fill", style: "width: " + pct.toFixed(1) + "%" }),
          ]),
          el("div", { class: "rung-score", text: dim.score.toFixed(1) }),
        ])
      );
    });
    section.appendChild(ladder);
    section.appendChild(
      el("p", {
        class: "provenance",
        text: "confidence per dimension: " +
          r.dimensions.map(function (d) { return d.name.toLowerCase() + " " + d.confidence; }).join(" · "),
      })
    );
    return section;
  }

  function renderAcceptance(state) {
    var a = state.acceptance;
    var section = panel(
      "gates",
      "Release gates",
      a.release_gate
        ? "Release gate: " + a.release_gate.replace(/_/g, " ") + ". " + (a.reason || "")
        : a.reason || "",
      a.sources
    );

    section.appendChild(distributionBlock(a.counts, a.total));

    var certified = el("dl", { class: "figures" }, [
      el("div", { class: "figure" }, [
        el("dt", { text: "Production certified" }),
        el("dd", { text: a.production_certified ? "yes" : "no" }),
        el("span", { class: "note", text: "suite_state.production_certified" }),
      ]),
      el("div", { class: "figure" }, [
        el("dt", { text: "Human owner signoff" }),
        el("dd", { text: a.human_owner_signoff ? "yes" : "no" }),
        el("span", { class: "note", text: "suite_state.human_owner_signoff" }),
      ]),
      el("div", { class: "figure" }, [
        el("dt", { text: "Critical gates with pass evidence" }),
        el("dd", { text: a.critical_proven + " of " + a.critical_total }),
        el("span", { class: "note", text: "every critical test must pass to release" }),
      ]),
      el("div", { class: "figure" }, [
        el("dt", { text: "Tests ever executed" }),
        el("dd", { text: a.executed + " of " + a.total }),
        el("span", { class: "note", text: "unexecuted tests are shown, not omitted" }),
      ]),
    ]);
    section.appendChild(certified);

    if (!a.tests.length) {
      section.appendChild(
        el("p", { class: "empty" }, [
          "No tests defined. Populate ",
          el("span", { class: "mono", text: "evaluations/acceptance-tests.yaml" }),
          ".",
        ])
      );
      return section;
    }

    var body = el("tbody");
    // Worst first, then critical, then alphabetical: the reading order that
    // surfaces risk rather than flattering the suite.
    var order = { failed: 0, stale: 1, unproven: 2, partial: 3, proven: 4 };
    a.tests
      .slice()
      .sort(function (x, y) {
        if (order[x.state] !== order[y.state]) return order[x.state] - order[y.state];
        if (x.critical !== y.critical) return x.critical ? -1 : 1;
        return String(x.id).localeCompare(String(y.id));
      })
      .forEach(function (t) {
        body.appendChild(
          el("tr", {}, [
            el("td", {}, [
              el("span", { class: "id", text: t.id }),
              t.objective ? el("span", { class: "objective", text: t.objective }) : null,
            ]),
            el("td", {}, [
              el("span", { class: "flag", "data-critical": String(t.critical), text: t.critical ? "critical" : "standard" }),
            ]),
            el("td", {}, [stateChip(t.state)]),
            el("td", { class: "num", text: String(t.evidence_count) }),
            el("td", { class: "mono", text: t.invalidated ? "invalidated" : t.raw_status }),
          ])
        );
      });

    section.appendChild(
      el("div", { class: "table-wrap" }, [
        el("table", {}, [
          el("thead", {}, [
            el("tr", {}, [
              el("th", { scope: "col", text: "Gate" }),
              el("th", { scope: "col", text: "Tier" }),
              el("th", { scope: "col", text: "Proof state" }),
              el("th", { scope: "col", text: "Evidence" }),
              el("th", { scope: "col", text: "Recorded status" }),
            ]),
          ]),
          body,
        ]),
      ])
    );
    return section;
  }

  function renderSkills(state) {
    var s = state.skills;
    var section = panel(
      "skills",
      "Skill fitness",
      "A version number is a contract baseline, not evidence of performance. Promotion requires " +
        (s.minimum_runs_for_promotion || "repeated") + " recorded runs.",
      s.sources
    );

    section.appendChild(distributionBlock(s.counts, s.total));

    if (!s.items.length) {
      section.appendChild(
        el("p", { class: "empty" }, [
          "No skills registered. Add contracts under ",
          el("span", { class: "mono", text: "skills/" }),
          " and register them in ",
          el("span", { class: "mono", text: "evaluations/skill-fitness.yaml" }),
          ".",
        ])
      );
      return section;
    }

    var body = el("tbody");
    var order = { failed: 0, stale: 1, unproven: 2, partial: 3, proven: 4 };
    s.items
      .slice()
      .sort(function (x, y) {
        if (order[x.state] !== order[y.state]) return order[x.state] - order[y.state];
        return x.name.localeCompare(y.name);
      })
      .forEach(function (k) {
        body.appendChild(
          el("tr", {}, [
            el("td", {}, [el("span", { class: "id", text: k.name })]),
            el("td", { class: "mono", text: k.version }),
            el("td", {}, [stateChip(k.state)]),
            el("td", { class: "num", text: String(k.runs) }),
            el("td", { class: "mono", text: k.benchmark_status }),
            el("td", {}, [
              el("span", {
                class: "flag",
                text: k.has_contract && k.registered ? "contract + registry"
                  : k.has_contract ? "contract only"
                  : "registry only",
              }),
            ]),
          ])
        );
      });

    section.appendChild(
      el("div", { class: "table-wrap" }, [
        el("table", {}, [
          el("thead", {}, [
            el("tr", {}, [
              el("th", { scope: "col", text: "Skill" }),
              el("th", { scope: "col", text: "Version" }),
              el("th", { scope: "col", text: "Proof state" }),
              el("th", { scope: "col", text: "Runs" }),
              el("th", { scope: "col", text: "Benchmark status" }),
              el("th", { scope: "col", text: "Presence" }),
            ]),
          ]),
          body,
        ]),
      ])
    );
    return section;
  }

  function renderKnowledge(state) {
    var k = state.knowledge;
    var g = state.graph;
    var section = panel(
      "knowledge",
      "Knowledge base",
      "Corpus and graph coverage. The graph is current only when it indexes every indexable file in the repository.",
      [].concat(k.sources || [], (g && g.sources) || [])
    );

    var figures = el("dl", { class: "figures" });

    if (g && g.available) {
      figures.appendChild(
        el("div", { class: "figure" }, [
          el("dt", {}, [el("span", { text: "Graph coverage " }), stateChip(g.state)]),
          el("dd", { text: g.indexed_files + " of " + g.repository_files + " files" }),
          el("span", {
            class: "note",
            text: g.unindexed_total
              ? g.unindexed_total + " files are not represented in the graph"
              : "every indexable file is represented",
          }),
        ])
      );
      figures.appendChild(
        el("div", { class: "figure" }, [
          el("dt", { text: "Graph size" }),
          el("dd", { text: g.nodes + " nodes · " + g.links + " links" }),
          el("span", { class: "note", text: g.communities + " communities, " + g.hyperedges + " hyperedges" }),
        ])
      );
    }

    figures.appendChild(
      el("div", { class: "figure" }, [
        el("dt", { text: "Indexed corpus" }),
        el("dd", { text: String(k.total_files) + " files" }),
        el("span", { class: "note", text: k.corpus.map(function (c) { return c.directory + " " + c.files; }).join(" · ") }),
      ])
    );
    figures.appendChild(
      el("div", { class: "figure" }, [
        el("dt", { text: "Entities" }),
        el("dd", { text: k.projects.length + " projects · " + k.topics + " topics" }),
        el("span", { class: "note", text: k.skills_indexed + " skills indexed, schema v" + k.schema_version }),
      ])
    );

    section.appendChild(figures);

    if (g && g.available && g.unindexed_total) {
      var sample = g.unindexed.slice(0, 8);
      section.appendChild(
        el("p", { class: "provenance" }, [
          "not in graph: " + sample.join(", ") +
            (g.unindexed_total > sample.length ? " and " + (g.unindexed_total - sample.length) + " more" : ""),
        ])
      );
    }
    return section;
  }

  function renderHistory(state) {
    var section = panel(
      "history",
      "Decisions and reviews",
      "Superseded decisions are preserved rather than rewritten.",
      ["decisions/", "reviews/"]
    );

    if (!state.history.length) {
      section.appendChild(
        el("p", { class: "empty" }, [
          "No records. Add files under ",
          el("span", { class: "mono", text: "decisions/" }),
          " or ",
          el("span", { class: "mono", text: "reviews/" }),
          ".",
        ])
      );
      return section;
    }

    var list = el("div", { class: "history" });
    state.history.forEach(function (entry) {
      list.appendChild(
        el("div", { class: "entry" }, [
          el("span", { class: "date", text: entry.date || "undated" }),
          el("span", { class: "title", text: entry.title, title: entry.path }),
          el("span", { class: "kind", text: entry.kind }),
        ])
      );
    });
    section.appendChild(list);
    return section;
  }

  /* Chrome --------------------------------------------------------------- */

  function renderRail(state) {
    var sections = [
      { id: "readiness", label: "Readiness", tally: state.readiness && state.readiness.score !== null ? String(state.readiness.score) : "—" },
      { id: "gates", label: "Release gates", tally: state.acceptance.critical_proven + "/" + state.acceptance.critical_total },
      { id: "skills", label: "Skill fitness", tally: state.skills.benchmarked + "/" + state.skills.total },
      { id: "knowledge", label: "Knowledge base", tally: state.graph && state.graph.available ? state.graph.indexed_files + "/" + state.graph.repository_files : "—" },
      { id: "history", label: "Decisions", tally: String(state.history.length) },
    ];

    var nav = el("nav", { class: "rail-nav", "aria-label": "Console sections" });
    sections.forEach(function (s) {
      nav.appendChild(
        el("a", { href: "#" + s.id }, [
          el("span", { text: s.label }),
          el("span", { class: "tally", text: s.tally }),
        ])
      );
    });

    var toggle = el("button", { class: "theme-toggle", type: "button", "aria-pressed": "false" }, [
      el("span", { text: "Theme" }),
      el("span", { class: "mono", "data-theme-label": "", text: "system" }),
    ]);

    return el("aside", { class: "rail" }, [
      el("div", { class: "rail-mark" }, [
        el("strong", { text: "DR.X Console" }),
        el("span", { text: "Erfan Second Brain" }),
      ]),
      nav,
      el("div", { class: "rail-foot" }, [
        toggle,
        el("span", {
          class: "mono",
          text: (state.generated_at || "").slice(0, 10) || "ungenerated",
          title: "State generated " + formatDate(state.generated_at),
        }),
      ]),
    ]);
  }

  function wireTheme(root) {
    var button = root.querySelector(".theme-toggle");
    if (!button) return;
    var label = button.querySelector("[data-theme-label]");
    var order = ["system", "light", "dark"];
    var stored = null;
    try {
      stored = window.localStorage.getItem("drx-console-theme");
    } catch (err) {
      stored = null; // private mode or blocked storage; system default is correct
    }
    var current = order.indexOf(stored) >= 0 ? stored : "system";

    function apply(mode) {
      if (mode === "system") document.documentElement.removeAttribute("data-theme");
      else document.documentElement.setAttribute("data-theme", mode);
      label.textContent = mode;
      button.setAttribute("aria-pressed", String(mode !== "system"));
      button.setAttribute("aria-label", "Theme: " + mode + ". Activate to change.");
      try {
        window.localStorage.setItem("drx-console-theme", mode);
      } catch (err) {
        /* non-fatal: the choice simply does not persist */
      }
    }

    apply(current);
    button.addEventListener("click", function () {
      current = order[(order.indexOf(current) + 1) % order.length];
      apply(current);
    });
  }

  function wireScrollSpy() {
    var links = Array.prototype.slice.call(document.querySelectorAll(".rail-nav a"));
    if (!links.length || !("IntersectionObserver" in window)) return;
    var byId = {};
    links.forEach(function (a) {
      byId[a.getAttribute("href").slice(1)] = a;
    });
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          links.forEach(function (a) { a.removeAttribute("aria-current"); });
          var link = byId[entry.target.id];
          if (link) link.setAttribute("aria-current", "true");
        });
      },
      { rootMargin: "-20% 0px -70% 0px" }
    );
    Object.keys(byId).forEach(function (id) {
      var node = document.getElementById(id);
      if (node) observer.observe(node);
    });
  }

  /* Boot ----------------------------------------------------------------- */

  function fail(message) {
    document.body.appendChild(
      el("div", { class: "main" }, [
        el("p", { class: "empty" }, [
          message + " Run ",
          el("span", { class: "mono", text: "python3 scripts/build_console_state.py" }),
          " and reload.",
        ]),
      ])
    );
  }

  function boot() {
    var state = window.__DRX_STATE__;
    if (!state) {
      fail("Console state has not been generated.");
      return;
    }

    var main = el("main", { class: "main" }, [
      el("header", { class: "masthead" }, [
        el("div", {}, [
          el("h1", { text: "System state" }),
          el("p", {
            text: "Every value below is read from a repository file and names its source. " +
              "Presence and proof are separate axes: a contract that exists has not thereby been verified.",
          }),
        ]),
        el("div", { class: "stamp" }, [
          el("span", { text: "generated " + formatDate(state.generated_at) }),
          el("span", {}, [
            el("span", { text: "contracts " }),
            stateChip(state.verification.state),
          ]),
        ]),
      ]),
      renderVerdict(state),
      renderReadiness(state),
      renderAcceptance(state),
      renderSkills(state),
      renderKnowledge(state),
      renderHistory(state),
      el("p", {
        class: "footnote",
        text: state.contract + " Regenerate with scripts/build_console_state.py; CI refreshes it on every push to main. " +
          "A stale console shows a stale timestamp rather than confidently wrong numbers. " +
          "It records no commit of its own, because a committed artifact cannot name the commit that contains it: " +
          "run git log console/state.json for that, and build_console_state.py --check for whether it is current.",
      }),
    ]);

    var shell = el("div", { class: "shell" }, [renderRail(state), main]);
    document.body.appendChild(shell);
    wireTheme(shell);
    wireScrollSpy();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
