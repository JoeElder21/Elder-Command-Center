# Nano Banana MCP Setup Guide

## Step 1: Get Gemini API Key
Get a free Gemini API key at [ai.google.dev](https://ai.google.dev)

## Step 2: Install
```bash
claude mcp add nanobanana-mcp -e GOOGLE_AI_API_KEY=your_key -- npx -y @ycse/nanobanana-mcp
```

## Step 3: Verify
Restart your Claude Code session and verify MCP tools load correctly.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tools not loading | Restart Claude Code session after adding MCP |
| API key error | Verify key at ai.google.dev console |
| npx timeout | Check network connection, try `npx -y @ycse/nanobanana-mcp` standalone |
| Permission denied | Ensure Node.js and npm are installed and in PATH |

## Canva Integration Pipeline
Nano Banana MCP enables AI-powered image generation via Gemini, which can be used as part of a pipeline:
1. Generate or edit images using Nano Banana MCP tools
2. Export results for use in Canva designs
3. Combine with other design assets for final deliverables
