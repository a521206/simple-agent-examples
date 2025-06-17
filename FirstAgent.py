from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
import os

# Get OpenAI API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Define a LinkedIn job search agent
job_search_agent = Agent(
    role="Job Advisor",
    goal="Suggest relevant job titles based on a user's LinkedIn summary.",
    backstory="You help people find matching job roles using their profile.",
    llm=llm
)

# Define task with a direct prompt
job_search_task = Task(
    description="Analyze the following LinkedIn summary and suggest 3-5 job titles:\n\n'{profile_summary}'",
    agent=job_search_agent,
    expected_output="A list of 3-5 relevant job titles based on the provided LinkedIn summary"
)

# Define the crew
crew = Crew(agents=[job_search_agent], tasks=[job_search_task])

# Sample input
profile_summary = "I am a software engineer with 3 years of experience in Python and JavaScript."

# Run the agent
result = crew.kickoff(inputs={"profile_summary": profile_summary})

# Show output
print(result)
