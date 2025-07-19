# Agent Examples

A collection of minimal, practical AI agent examples using different frameworks and approaches.

## Project Structure

```
├── examples/
│   ├── mcp/                    # MCP (Model Context Protocol) examples
│   │   ├── mcp_crewai_client.py
│   │   ├── mcp_openai_client.py
│   │   ├── MCP_README.md
│   │   └── mcp_tools/          # MCP server implementations
│   │       └── fastmcp_currency_tool.py
│   ├── routing/                # Routing examples (LangGraph)
│   │   ├── langgraph_routing.py
│   │   └── README.md
│   ├── prompt_chaining/        # Prompt chaining example
│   │   ├── prompt_chaining.py
│   │   ├── sample_transcript.txt
│   │   └── README.md
│   ├── parallelization/        # Parallelization example
│   │   ├── parallel_langchain.py
│   │   └── README.md
│   ├── reflection/             # Reflection and memory examples
│   │   ├── memory_reflection.py
│   │   ├── reflection.py
│   │   ├── reflection_loop.py
│   │   └── README.md
│   └── simple_agents/          # Basic agent construction examples
│       ├── local_transformers_no_api.py
│       ├── openai_agentsdk_simple.py
│       ├── ollama_langchain_simple.py
│       └── Simple_Agents.md
├── config/                     # Configuration templates
│   └── env.example
├── requirements.txt
└── README.md
```

## Quick Start

1. **Install dependencies**:
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
   # Prompt chaining
   python examples/prompt_chaining/prompt_chaining.py

   # Routing (LangGraph)
   python examples/routing/langgraph_routing.py

   # Parallelization (LangChain)
   python examples/parallelization/parallel_langchain.py

   # Reflection (LLM memory & critique)
   python examples/reflection/memory_reflection.py
   python examples/reflection/reflection.py
   python examples/reflection/reflection_loop.py

   # MCP (Model Context Protocol)
   python examples/mcp/mcp_crewai_client.py
   # or
   python examples/mcp/mcp_openai_client.py
   ```

## Examples

### Prompt Chaining
- Multi-step LLM workflow: summarize, extract insights, and suggest next steps from a sales call transcript.
- Input transcript is read from `examples/prompt_chaining/sample_transcript.txt` (replace with your own to try different calls).
- 📖 [Prompt Chaining README](examples/prompt_chaining/README.md)

### Routing (LangGraph)
- Intelligent message routing using an LLM to select the right agent (support, order, product) for each query.
- Simple canned responses for each agent to clearly show routing.
- 📖 [Routing README](examples/routing/README.md)

### Parallelization (LangChain)
- Run multiple LLM chains (e.g., summary and sentiment) in parallel on the same input for efficiency.
- 📖 [Parallelization README](examples/parallelization/README.md)

### Reflection (LLM Memory & Critique)
- Minimal examples of LLM-powered memory and reflection for self-improving answers.
- Includes:
  - `memory_reflection.py`: Minimal memory+reflection demo
  - `reflection.py`: Basic single-turn reflection
  - `reflection_loop.py`: Multi-turn iterative reflection
- 📖 [Reflection README](examples/reflection/README.md)

### MCP Examples
- Use external tools via Model Context Protocol (MCP) with CrewAI or OpenAI clients.
- ⚠️ **Note:** OpenAI MCP integration may have issues (see code comments and docs).
- 📖 [MCP Setup Guide](examples/mcp/MCP_README.md)

### Simple Agents
- Minimal agent construction patterns for local transformers, OpenAI, and Ollama.
- 📖 [Simple Agents Guide](examples/simple_agents/Simple_Agents.md)

## Prerequisites
- Python 3.8+
- OpenAI API key (for OpenAI examples)
- [ngrok](https://ngrok.com/) (for MCP examples)
- [Ollama](https://ollama.com/) (for local LLM examples)

## Environment Variables
Create a `.env` file:
```
OPENAI_API_KEY=your-api-key-here
MCP_SERVER_URL=https://your-ngrok-url.ngrok-free.app/
```


