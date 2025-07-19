"""
Planning is a pattern that enables AI agents to create and execute sequences of actions to achieve specific goals. By breaking down complex tasks into manageable steps and considering dependencies and constraints, this pattern enables systematic problem-solving and goal achievement.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo-preview")

ACTIONS = [
    {
        'name': 'research_market',
        'description': 'Research market conditions and opportunities.'
    },
    {
        'name': 'develop_strategy',
        'description': 'Develop business strategy based on market research.'
    },
    {
        'name': 'customize_strategy_healthcare',
        'description': 'Customize the business strategy for the healthcare sector.'
    },
    # Unrelated actions
    {
        'name': 'organize_team_building',
        'description': 'Plan a team-building event for employees.'
    },
    {
        'name': 'setup_office_wifi',
        'description': 'Install and configure WiFi in the new office.'
    },
    {
        'name': 'order_office_supplies',
        'description': 'Order pens, paper, and other office supplies.'
    },
    {
        'name': 'plan_company_retreat',
        'description': 'Organize a company retreat for relaxation and strategy.'
    }
]

def llm_plan(goal, available_actions):
    prompt = ChatPromptTemplate.from_template("""
Goal: {goal}
Available actions:
{actions}

Plan a sequence of actions (by name) to achieve the goal.
Only include actions that are strictly necessary for the goal.
Do NOT include unrelated or optional actions.
Respond with a comma-separated list of action names in order.
""")
    actions_list = "\n".join(f"- {a['name']}: {a['description']}" for a in available_actions)
    response = llm.invoke(prompt.format(goal=goal, actions=actions_list)).content.strip()
    plan = [name.strip() for name in response.split(",") if name.strip()]
    valid_names = {a['name'] for a in available_actions}
    return [name for name in plan if name in valid_names]

def execute_action(action_name):
    action = next((a for a in ACTIONS if a['name'] == action_name), None)
    if action:
        print(f"[EXECUTE] {action['name']}: {action['description']}")
    else:
        print(f"[EXECUTE] {action_name}: (Unknown action)")

def main():
    goal = "Develop a business strategy for a new startup in Healthcare."
    print(f"Goal: {goal}\n")
    print("Available actions:")
    for a in ACTIONS:
        print(f"- {a['name']}: {a['description']}")
    print("\nLLM is planning...")
    plan = llm_plan(goal, ACTIONS)
    print("\nPlanned sequence:", plan)
    print("\n--- Executing Plan ---")
    for action_name in plan:
        execute_action(action_name)
    print("\nPlanning and execution complete.")

if __name__ == "__main__":
    main() 