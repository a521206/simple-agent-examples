# MCP (Model Context Protocol) Guide

Model Context Protocol (MCP) allows AI agents to use external tools and data sources.

> **⚠️ Warning**: The OpenAI MCP client (`mcp_openai_client.py`) is currently facing issues and may not work properly. This may be resolved in future versions. The CrewAI MCP client works correctly.

## Setup

1. **Install dependencies**:
   ```bash
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Start MCP server**:
   ```bash
   python mcp_tools/fastmcp_currency_tool.py
   ```

3. **Expose with ngrok**:
   ```bash
   ngrok http 8000
   ```

4. **Configure environment**:
   ```bash
   cp config/env.example .env
   # Edit .env with your ngrok URL
   ```

## Usage

```python
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

server_config = {
    "url": "https://your-ngrok-url.ngrok-free.app/mcp",
    "transport": "streamable-http"
}

with MCPServerAdapter(server_config) as tools:
    agent = Agent(role="Expert", tools=tools)
    # ... rest of your code
```

## Available Tools

- `convert_currency`: Convert between USD, EUR, GBP, JPY
- `get_supported_currencies`: List available currency pairs

## Troubleshooting

- **Import errors**: Ensure virtual environment is activated
- **Connection issues**: Check ngrok is running and URL is correct
- **Missing URL**: Set `MCP_SERVER_URL` in `.env` file 