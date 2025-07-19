# Prompt Chaining Example

This example demonstrates **prompt chaining**: using the output of one LLM prompt as the input to the next, to build a multi-step reasoning pipeline.

## What It Does
- Analyzes a sales call transcript (from `sample_transcript.txt`)
- Chains three LLM prompts:
  1. **Summarize** the call
  2. **Extract key insights** from the summary
  3. **Suggest next steps** based on the insights
- Prints all results to the console

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
   python examples/prompt_chaining/prompt_chaining.py
   ```

## Input Transcript
- The script reads the sales call transcript from `sample_transcript.txt` in this folder.
- You can replace the contents of this file with your own transcript to analyze different calls.

## Example Output
```
Summary: ...

Key Insights: ...

Next Steps: ...
```

## Why Prompt Chaining?
Prompt chaining lets you break down complex tasks into smaller, more reliable LLM steps. This improves reasoning, transparency, and control over multi-step workflows.
