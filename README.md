# Agent Examples

A collection of AI agent examples using different frameworks and approaches.

## Project Structure

```
├── examples/
│   ├── mcp/                    # MCP (Model Context Protocol) examples
│   │   ├── mcp_crewai_client.py
│   │   ├── mcp_openai_client.py
│   │   ├── MCP_README.md
│   │   └── mcp_tools/          # MCP server implementations
│   │       └── fastmcp_currency_tool.py
│   └── simple_agents/          # Basic agent construction examples
│       ├── local_transformers_no_api.py
│       ├── openai_agentsdk_simple.py
│       ├── ollama_langchain_simple.py
│       └── Simple_Agents.md
├── config/                     # Configuration templates
│   └── env.example
├── docs/                       # Documentation (empty)
├── requirements.txt
└── README.md
```

## Quick Start

1. **Setup environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   pip install -r requirements.txt
   ```

2. **Configure**:
   ```bash
   cp config/env.example .env
   # Edit .env with your API keys
   ```

3. **Run examples**:
   ```bash
   # Simple agents (no setup required)
   python examples/simple_agents/local_transformers_no_api.py
   
   # MCP examples (requires ngrok)
   python examples/mcp/mcp_crewai_client.py
   ```

## Examples

### Simple Agents
Basic agent construction patterns with different frameworks:

- **Local Transformers** - Offline inference using Flan-T5 (no API cost)
- **Ollama + LangChain** - Local LLM with LangChain (no API cost)  
- **OpenAI Agents SDK** - Cloud-based GPT models (requires API key)

📖 [Detailed guide](examples/simple_agents/Simple_Agents.md)

### MCP Examples
Agents using external tools via Model Context Protocol:

- **CrewAI MCP Client** - Currency conversion with CrewAI
- **OpenAI MCP Client** - Currency conversion with OpenAI ⚠️

> **⚠️ Warning**: OpenAI MCP integration is currently facing issues and may not work properly. This is a known issue with the OpenAI library's MCP implementation that may be resolved in future versions.

📖 [Setup guide](examples/mcp/MCP_README.md)

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) (for local LLM examples)
- OpenAI API key (for OpenAI examples)
- [ngrok](https://ngrok.com/) (for MCP examples)

## Environment Variables

Create `.env` file:
```
OPENAI_API_KEY=your-api-key-here
MCP_SERVER_URL=https://your-ngrok-url.ngrok-free.app/
```


