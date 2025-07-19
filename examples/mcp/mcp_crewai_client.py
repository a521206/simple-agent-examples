import warnings
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import MCPServerAdapter

# Load environment variables from .env file
load_dotenv()

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", message=".*Using extra keyword arguments on `Field` is deprecated.*", category=DeprecationWarning)

def get_server_config():
    """Get server configuration from environment"""
    server_url = os.getenv("MCP_SERVER_URL")
    
    if not server_url:
        print("Missing MCP_SERVER_URL")
        print("💡 Run ngrok and add MCP_SERVER_URL to .env")
        exit(1)
    
    if not server_url.endswith('/mcp'):
        server_url = server_url.rstrip('/') + '/mcp'
    
    return {
        "url": server_url,
        "transport": "streamable-http"
    }

server_config = get_server_config()

with MCPServerAdapter(server_config) as currency_tools:

    # Create agent that uses the MCP tools
    currency_agent = Agent(
        role="Currency Exchange Expert",
        goal="Help with currency conversions and exchange rate information",
        backstory="You're a knowledgeable financial assistant with access to real-time currency conversion tools.",
        tools=currency_tools,  # <- Pass the list of actual tool instances
        verbose=False
    )

    # Define a task for the agent
    task = Task(
        description="Convert 100 USD to EUR using your currency conversion tools.",
        agent=currency_agent,
        expected_output="The conversion result showing 100 USD in EUR."
    )

    # Create the crew and run
    crew = Crew(
        agents=[currency_agent],
        tasks=[task],
        verbose=False,
    )

    crew_result = crew.kickoff()
    print("✅ Final result:\n", crew_result)