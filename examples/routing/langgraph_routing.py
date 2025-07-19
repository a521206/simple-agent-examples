from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo-preview")

class AgentState(TypedDict):
    messages: List[Dict[str, str]]
    next: str

# Agent functions
def support_agent(state: AgentState) -> AgentState:
    return {"messages": state["messages"] + [{"role": "assistant", "content": "[SUPPORT] How can I help?"}], "next": "end"}

def order_agent(state: AgentState) -> AgentState:
    return {"messages": state["messages"] + [{"role": "assistant", "content": "[ORDER] I can help with orders."}], "next": "end"}

def product_agent(state: AgentState) -> AgentState:
    return {"messages": state["messages"] + [{"role": "assistant", "content": "[PRODUCT] I can help with products."}], "next": "end"}

# Router function
def router(state: AgentState) -> AgentState:
    message = state["messages"][-1]["content"]
    
    response = llm.invoke([
        {"role": "system", "content": "Route to: support_agent (general), order_agent (orders/tracking), product_agent (products). Respond with agent name only."},
        {"role": "user", "content": f"Route this message: {message}"}
    ])
    
    agent = response.content.strip().lower()
    if "order" in agent:
        next_agent = "order_agent"
    elif "product" in agent:
        next_agent = "product_agent"
    else:
        next_agent = "support_agent"
    
    print(f"'{message}' → {next_agent}")
    return {"messages": state["messages"], "next": next_agent}

# Create workflow
def create_workflow():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("router", router)
    workflow.add_node("support_agent", support_agent)
    workflow.add_node("order_agent", order_agent)
    workflow.add_node("product_agent", product_agent)
    
    workflow.add_conditional_edges("router", lambda state: state["next"], {
        "support_agent": "support_agent",
        "order_agent": "order_agent", 
        "product_agent": "product_agent"
    })
    
    workflow.add_edge("support_agent", END)
    workflow.add_edge("order_agent", END)
    workflow.add_edge("product_agent", END)
    
    workflow.set_entry_point("router")
    return workflow.compile()

# Test
if __name__ == "__main__":
    app = create_workflow()
    
    test_queries = [
        "What's my order status?",
        "Tell me about iPhone features",
        "I need help with my account",
        "Can I return this item?",
        "Compare these products"
    ]
    
    print("=== LangGraph Routing ===\n")
    
    for query in test_queries:
        result = app.invoke({"messages": [{"role": "user", "content": query}], "next": ""})
        response = result["messages"][-1]["content"]
        print(f"Response: {response}\n") 