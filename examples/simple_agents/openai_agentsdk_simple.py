"""
This script demonstrates a simple job title suggestion agent using the OpenAI Agents SDK
and OpenAI API (gpt-4o or gpt-3.5-turbo). Requires an OpenAI API key set in the environment
variable OPENAI_API_KEY.
"""
from agents import Agent, Runner
import os

profile_summary = "I know Python and love maths"

print("Starting Job Title Suggester (OpenAI Agents SDK)")
print("="*50)
print(f"Profile: {profile_summary}")
print("="*50)

if not os.getenv("OPENAI_API_KEY"):
    print("WARNING: OPENAI_API_KEY environment variable is not set. Please set it to use this script.")

career_agent = Agent(
    name="Career Advisor",
    instructions=(
        "You are a career advisor. Read a LinkedIn profile summary and suggest 3–5 relevant job titles. "
        "Respond only with job titles, each on a new line."
    ),
    model="gpt-4o"  # You can also use "gpt-3.5-turbo"
)

try:
    response = Runner.run_sync(career_agent, f"Suggest job titles for this summary:\n\n{profile_summary}")
    print("\nResults:")
    print("="*50)
    print(response.final_output)
    print("="*50)
except Exception as e:
    print(f"An error occurred during agent execution: {e}") 