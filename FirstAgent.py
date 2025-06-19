from langchain_ollama import OllamaLLM
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain.tools import tool

# 1. Define a simple tool (required for agent)
@tool
def dummy_tool(info: str) -> str:
    """Returns a canned response for demonstration."""
    return "This is a dummy tool response."

tools = [dummy_tool]

# 2. Create the LLM
llm = OllamaLLM(model="llama3.1:8b")

# 3. Create a simple agent prompt
prompt = PromptTemplate(
    input_variables=["input", "tools", "tool_names", "agent_scratchpad"],
    template=(
        "You are a career advisor. Read a LinkedIn profile summary and suggest 3–5 relevant job titles. "
        "Respond only with job titles, each on a new line. When you are done, write 'Final Answer:' and then the list of job titles, one per line. "
        "If you need more information, use the available tools.\n\n"
        "{input}\n"
        "Available tools: {tool_names}\n"
        "{agent_scratchpad}\n"
        "{tools}"
    )
)

# 4. Create the agent and executor
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 5. Run the agent
profile_summary = (
    "I am a software engineer with 3 years of experience in Python and JavaScript, "
    "focusing on backend development, cloud services, and microservices architecture."
)

print("\nSuggested Job Titles:\n")
try:
    result = agent_executor.invoke({"input": profile_summary})
    print("\nResults:")
    print("="*50)
    print(result["output"])
except Exception as e:
    print(f"An error occurred during agent execution: {e}")
