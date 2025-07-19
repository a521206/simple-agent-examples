import os
import json
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo-preview")

memory = [
    {
        'input': "Suggest a lunch for weight loss",
        'output': "Try a salad with grilled chicken and lots of veggies.",
        'feedback': "Too generic"
    }
]

def find_similar_llm(query, memory):
    if not memory:
        return None
    prompt = ChatPromptTemplate.from_template("""
Given a user query and a list of past queries, select the most similar past query.

User query: {query}
Past queries:
{past_queries}

Respond with the exact text of the most similar past query.
""")
    past_queries = "\n".join(f"- {m['input']}" for m in memory)
    response = llm.invoke(prompt.format(query=query, past_queries=past_queries)).content.strip()
    for m in memory:
        if response.lower() in m['input'].lower() or m['input'].lower() in response.lower():
            return m
    return memory[0]

def reflect_llm(query, similar):
    if not similar:
        return "No similar past interaction found."
    prompt = ChatPromptTemplate.from_template("""
Given a new user query and a similar past interaction (with response and feedback), suggest how to improve the response for the new query. If the feedback was positive, say 'No improvement needed.'

User query: {query}
Similar past input: {input}
Similar past response: {output}
Feedback: {feedback}

Suggestion:
""")
    return llm.invoke(prompt.format(query=query, input=similar['input'], output=similar['output'], feedback=similar['feedback'])).content.strip()

def generate_response_llm(query):
    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer the following user query as clearly and specifically as possible.

User query: {query}

Response:
""")
    return llm.invoke(prompt.format(query=query)).content.strip()

if __name__ == "__main__":
    print("Minimal memory+reflection demo (Diet/Health scenario).\n")
    user_query = "What should I eat for dinner if I want to lose weight?"
    print(f"User query: {user_query}")
    similar = find_similar_llm(user_query, memory)
    if similar:
        print("Most similar past response:", similar['output'])
        print("Reflection:", reflect_llm(user_query, similar))
    else:
        print("No similar past interaction found.")
    response = generate_response_llm(user_query)
    print("Assistant response:", response)
