# Simple Agent Examples

This directory contains examples of building simple agents using different frameworks and models.

## Examples

| File                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `local_transformers_no_api.py` | Example of building an agent using only local HuggingFace Transformers (Flan-T5). No API calls or cost. |
| `ollama_langchain_simple.py`   | Example of building an agent using a local Ollama LLM via LangChain. No external API calls or costs. |
| `openai_agentsdk_simple.py`    | Example of building an agent using the OpenAI Agents SDK and OpenAI API. Requires an API key. |

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running (for Ollama example)
- OpenAI API key (for OpenAI Agents SDK example)

## Usage

### 1. Local Transformers (No API, No Cost)
```bash
python examples/simple_agents/local_transformers_no_api.py
```
- Demonstrates agent construction using only local models (Flan-T5).
- No external dependencies or API costs.

### 2. LangChain + Ollama (No API Cost)
```bash
python examples/simple_agents/ollama_langchain_simple.py
```
- Demonstrates agent construction using LangChain and a local LLM (Ollama).
- Requires Ollama running locally with the `llama3.1:8b` model pulled.

### 3. OpenAI Agents SDK (Requires API Key)
```bash
# Ensure .env file is configured with OPENAI_API_KEY
python examples/simple_agents/openai_agentsdk_simple.py
```
- Demonstrates agent construction using the OpenAI Agents SDK and OpenAI's GPT models.
- Requires `OPENAI_API_KEY` in your `.env` file.

## Notes

- Each script demonstrates different agent construction patterns
- The example task is job title suggestion, but the patterns can be adapted to any use case
- You can modify the `profile_summary` variable in each script to test with different profiles
- Local examples (Transformers, Ollama) have no API costs
- OpenAI example requires an API key

## Agent Construction Patterns

These examples showcase three different approaches to building AI agents:

1. **Pure Local**: Using HuggingFace Transformers for completely offline inference
2. **Local LLM**: Using Ollama with LangChain for local large language model inference
3. **Cloud API**: Using OpenAI's Agents SDK with cloud-based GPT models

Each approach has different trade-offs in terms of cost, performance, and complexity. 