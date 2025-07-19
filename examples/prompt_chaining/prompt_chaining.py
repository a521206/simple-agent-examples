import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_sales_call(transcript: str) -> dict:
    """Analyze a sales call transcript using prompt chaining."""
    # Step 1: Summarize the call
    summary = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "user", "content": f"Summarize this sales call:\n{transcript}"}]
    ).choices[0].message.content

    # Step 2: Extract key insights
    insights = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "user", "content": f"Extract key insights from this summary:\n{summary}"}]
    ).choices[0].message.content

    # Step 3: Generate next steps
    next_steps = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[{"role": "user", "content": f"Based on these insights, suggest next steps:\n{insights}"}]
    ).choices[0].message.content

    return {
        "summary": summary,
        "insights": insights,
        "next_steps": next_steps
    }

# Example usage
if __name__ == "__main__":
    # This would typically come from an audio file
    sample_transcript = """
    [Sales Rep] Thanks for joining us today. How can we help you?
    [Customer] We're looking to improve our team's productivity...
    """

    result = analyze_sales_call(sample_transcript)
    print(f"Summary: {result['summary']}")
    print(f"\nKey Insights: {result['insights']}")
    print(f"\nNext Steps: {result['next_steps']}")
