# Planning Example

This directory demonstrates a minimal LLM-powered planning system:

## Script
- **planning.py**: Given a set of possible actions and a goal, the LLM creates a plan by sequencing only the necessary actions to achieve the goal.

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
   python examples/planning/planning.py
   ```

## Example Output
```
Goal: Develop a business strategy for a new startup in Healthcare.

Available actions:
- research_market: Research market conditions and opportunities.
- develop_strategy: Develop business strategy based on market research.
- customize_strategy_healthcare: Customize the business strategy for the healthcare sector.
...

LLM is planning...

Planned sequence: ['research_market', 'develop_strategy', 'customize_strategy_healthcare']

--- Executing Plan ---
[EXECUTE] research_market: Research market conditions and opportunities.
[EXECUTE] develop_strategy: Develop business strategy based on market research.
[EXECUTE] customize_strategy_healthcare: Customize the business strategy for the healthcare sector.

Planning and execution complete.
``` 