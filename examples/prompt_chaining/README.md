# Prompt Chaining Example

This example demonstrates how to use prompt chaining to analyze a sales call transcript.

## How it works

The script uses the OpenAI API to perform a three-step analysis of a sales call transcript:

1.  **Summarize the call:** The first prompt summarizes the entire sales call.
2.  **Extract key insights:** The second prompt extracts key insights from the summary.
3.  **Generate next steps:** The third prompt generates next steps based on the extracted insights.

## How to run

1.  Install the required packages:
    ```
    pip install -r requirements.txt
    ```
2.  Create a `.env` file in the root of the repository and add your OpenAI API key:
    ```
    OPENAI_API_KEY="<your-api-key>"
    ```
3.  Run the script:
    ```
    python examples/prompt_chaining/prompt_chaining.py
    ```
