import express from "express";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";
import { z } from "zod";

const PORT = Number(process.env.PORT || 8787);
const UPSTREAM_URL = process.env.CLAUDE_DESIGN_MCP_URL || "https://api.anthropic.com/v1/design/mcp";
const ACCESS_TOKEN = process.env.CLAUDE_DESIGN_ACCESS_TOKEN;
const BRIDGE_API_KEY = process.env.BRIDGE_API_KEY;

const READ_ONLY_TOOLS = [
  ["list_design_systems", "List Claude Design design systems available to the authenticated account."],
  ["list_projects", "List Claude Design projects available to the authenticated account."],
  ["get_project", "Read metadata for one Claude Design project."],
  ["list_files", "List files in a Claude Design project."],
  ["read_file", "Read one file from a Claude Design project."],
  ["get_conversation", "Read the generation conversation associated with a Claude Design project."],
  ["render_preview", "Render or retrieve a preview for a Claude Design project without modifying source files."],
  ["get_claude_design_prompt", "Read Claude Design's current live design-system instructions."],
];

function assertBridgeAuth(req, res) {
  if (!BRIDGE_API_KEY) return true;
  const auth = req.headers.authorization || "";
  if (auth !== `Bearer ${BRIDGE_API_KEY}`) {
    res.status(401).json({ error: "unauthorized" });
    return false;
  }
  return true;
}

async function createUpstreamClient() {
  if (!ACCESS_TOKEN) {
    throw new Error(
      "CLAUDE_DESIGN_ACCESS_TOKEN is not configured. Use a design-scoped token in the hosting environment; never commit it to Git."
    );
  }

  const client = new Client({
    name: "drx-claude-design-bridge",
    version: "0.1.0",
  });

  const transport = new StreamableHTTPClientTransport(new URL(UPSTREAM_URL), {
    authProvider: {
      token: async () => ACCESS_TOKEN,
    },
  });

  await client.connect(transport);
  return client;
}

async function callUpstreamTool(name, args = {}) {
  const client = await createUpstreamClient();
  try {
    return await client.callTool({ name, arguments: args });
  } finally {
    await client.close().catch(() => {});
  }
}

function textResult(value) {
  return {
    content: [
      {
        type: "text",
        text: typeof value === "string" ? value : JSON.stringify(value, null, 2),
      },
    ],
  };
}

function makeServer() {
  const server = new McpServer({
    name: "DR.X Claude Design Bridge",
    version: "0.1.0",
  });

  for (const [upstreamName, description] of READ_ONLY_TOOLS) {
    server.registerTool(
      `claude_design_${upstreamName}`,
      {
        title: `Claude Design: ${upstreamName}`,
        description: `Use this when ChatGPT needs read-only access to Claude Design. ${description}`,
        inputSchema: {
          arguments: z
            .record(z.string(), z.unknown())
            .optional()
            .describe("Arguments forwarded to the matching Claude Design MCP tool."),
        },
        annotations: {
          readOnlyHint: true,
          destructiveHint: false,
          openWorldHint: true,
          idempotentHint: true,
        },
      },
      async ({ arguments: args }) => {
        try {
          const result = await callUpstreamTool(upstreamName, args || {});
          return textResult(result);
        } catch (error) {
          return {
            isError: true,
            content: [
              {
                type: "text",
                text: `Claude Design bridge error: ${error instanceof Error ? error.message : String(error)}`,
              },
            ],
          };
        }
      }
    );
  }

  return server;
}

const app = express();
app.disable("x-powered-by");
app.use(express.json({ limit: "2mb" }));

app.get("/health", (_req, res) => {
  res.json({
    ok: true,
    service: "drx-claude-design-bridge-mcp",
    upstreamConfigured: Boolean(ACCESS_TOKEN),
    bridgeAuthEnabled: Boolean(BRIDGE_API_KEY),
  });
});

app.post("/mcp", async (req, res) => {
  if (!assertBridgeAuth(req, res)) return;

  const server = makeServer();
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined,
    enableJsonResponse: true,
  });

  res.on("close", () => {
    transport.close().catch(() => {});
    server.close().catch(() => {});
  });

  try {
    await server.connect(transport);
    await transport.handleRequest(req, res, req.body);
  } catch (error) {
    if (!res.headersSent) {
      res.status(500).json({
        error: error instanceof Error ? error.message : String(error),
      });
    }
  }
});

app.get("/mcp", (req, res) => {
  if (!assertBridgeAuth(req, res)) return;
  res.status(405).set("Allow", "POST").json({ error: "POST /mcp required" });
});

app.delete("/mcp", (req, res) => {
  if (!assertBridgeAuth(req, res)) return;
  res.status(405).set("Allow", "POST").json({ error: "Stateless bridge has no sessions to delete" });
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`DR.X Claude Design Bridge MCP listening on :${PORT}/mcp`);
});
