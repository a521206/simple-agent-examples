from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo-preview")

# Prompts
answer_prompt = ChatPromptTemplate.from_template("""
Answer the following user question as best as you can:

Question: {query}
""")

critique_prompt = ChatPromptTemplate.from_template("""
You are a critical reviewer. Given the following answer to a user question, provide a brief critique. If the answer can be improved, say 'IMPROVE' and explain why. If it is already good, say 'OK' and explain why.

Question: {query}
Answer: {answer}

Critique:
""")

improve_prompt = ChatPromptTemplate.from_template("""
Given the user question and the previous answer, and the following critique, improve the answer accordingly.

Question: {query}
Previous Answer: {answer}
Critique: {critique}

Improved Answer:
""")

def generate_answer(query):
    return llm.invoke(answer_prompt.format(query=query)).content.strip()

def reflect_on(query, answer):
    return llm.invoke(critique_prompt.format(query=query, answer=answer)).content.strip()

def improve_answer(query, answer, critique):
    return llm.invoke(improve_prompt.format(query=query, answer=answer, critique=critique)).content.strip()

if __name__ == "__main__":
    user_query = "Why is the sky blue?"
    max_reflections = 3
    response = generate_answer(user_query)
    print(f"Initial Answer:\n{response}\n")

    for i in range(max_reflections):
        critique = reflect_on(user_query, response)
        print(f"Reflection {i+1} Critique:\n{critique}\n")
        if critique.strip().upper().startswith("IMPROVE"):
            response = improve_answer(user_query, response, critique)
            print(f"Improved Answer {i+1}:\n{response}\n")
        else:
            print("No further improvements suggested.\n")
            break
    print("Final Answer:\n" + response) 