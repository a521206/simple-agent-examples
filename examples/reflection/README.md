# Reflection Examples (Diet/Health)

This directory demonstrates minimal LLM-powered reflection and memory systems:

## Scripts
- **memory_reflection.py**: Minimal example. Stores past user queries, responses, and feedback. For a new query, finds the most similar past query using the LLM, reflects on how to improve the response, and shows how memory and reflection can help generate better answers.
- **reflection.py**: Basic single-turn reflection loop. The LLM generates an answer, critiques it, and (optionally) improves it once based on the critique.

## Scenario (memory_reflection.py)
- The memory contains a past query about lunch for weight loss with negative feedback ("Too generic").
- The new query is about dinner for weight loss.
- The LLM is prompted to suggest improvements for the new answer, based on the past feedback.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set your OpenAI API key in a `.env` file:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```
3. Run a script:
   ```bash
   python examples/reflection/memory_reflection.py
   python examples/reflection/reflection.py
   ```

## Example Output (memory_reflection.py)
```
User query: What should I eat for dinner if I want to lose weight?
Most similar past response: Try a salad with grilled chicken and lots of veggies.
Reflection: (LLM suggests being more specific, e.g., include example meals)
Assistant response: ...
```

## Why Reflection?
Reflection lets LLMs use past feedback to improve future answers, making them more helpful and specific over time. 