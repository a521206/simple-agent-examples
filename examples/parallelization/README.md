# Parallelization Example (LangChain)

This example demonstrates how to run multiple LLM chains in parallel using LangChain's `RunnableParallel`.

## What It Does
- Runs a **summary** and **sentiment analysis** on the same input text at the same time
- Uses OpenAI's GPT model for both tasks
- Prints both results to the console

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
3. Run the script:
   ```bash
   python examples/parallelization/parallel_langchain.py
   ```

## Example Output
```
Summary: LangChain makes it easy to build LLM-powered apps.
Sentiment: The sentiment is positive.
```

## Why Parallelization?
Parallelization lets you process the same input with multiple chains at once, saving time and making your LLM workflows more efficient. 