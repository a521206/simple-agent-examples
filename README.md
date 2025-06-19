# Local & OpenAI Agent Construction Examples

This project demonstrates how to build simple agents using different frameworks and models:
- **Local HuggingFace Transformers (no API, no cost)**
- **LangChain with local Ollama LLM (no API cost)**
- **OpenAI Agents SDK (requires OpenAI API key)**

The example task is career/job title suggestion, but the focus is on showcasing agent construction patterns, not the specific use case.

## Project Structure

| File                        | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `local_transformers_no_api.py` | Example of building an agent using only local HuggingFace Transformers (Flan-T5). No API calls or cost. |
| `ollama_langchain_simple.py`   | Example of building an agent using a local Ollama LLM via LangChain. No external API calls or costs. |
| `openai_agentsdk_simple.py`    | Example of building an agent using the OpenAI Agents SDK and OpenAI API. Requires an API key. |

## Prerequisites
- Python 3.8+
- [Ollama](https://ollama.com/) installed and running (for Ollama example)
- (Optional) OpenAI API key for OpenAI Agents SDK example

## Setup
1. **Clone the repository** (if needed)
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv .venv
   # On Windows PowerShell:
   .venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Usage

### 1. Local Transformers (No API, No Cost)
```sh
python local_transformers_no_api.py
```
- Demonstrates agent construction using only local models (Flan-T5).

### 2. LangChain + Ollama (No API Cost)
```sh
python ollama_langchain_simple.py
```
- Demonstrates agent construction using LangChain and a local LLM (Ollama).
- Requires Ollama running locally with the `llama3.1:8b` model pulled.

### 3. OpenAI Agents SDK (Requires API Key)
```sh
# Set your OpenAI API key first:
$env:OPENAI_API_KEY="sk-..."  # PowerShell
export OPENAI_API_KEY="sk-..."  # macOS/Linux
python openai_agentsdk_simple.py
```
- Demonstrates agent construction using the OpenAI Agents SDK and OpenAI's GPT models.

## Notes
- Each script prints the input profile and results in a clear, structured format.
- You can modify the `profile_summary` variable in each script to test with different profiles or tasks.
- The example task is job title suggestion, but the agent construction pattern can be adapted to any use case.

---

**Explore and compare how agents can be built with different frameworks and models!** 