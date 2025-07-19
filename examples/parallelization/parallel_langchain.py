from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel
import os
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4-turbo-preview")

# 1. Define processing chains
summary_chain = ChatPromptTemplate.from_template(
    "Summarize this: {text}"
) | model

sentiment_chain = ChatPromptTemplate.from_template(
    "Analyze sentiment: {text}"
) | model

# 2. Run in parallel
parallel_chain = RunnableParallel(
    summary=summary_chain,
    sentiment=sentiment_chain
)

# 3. Execute with input
if __name__ == "__main__":
    # Read input from file (edit input_text.txt to try your own text)
    input_file = os.path.join(os.path.dirname(__file__), "input_text.txt")
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = f.read().strip()

    results = parallel_chain.invoke({"text": input_text})
    print("Summary\n" + "="*50)
    print(results["summary"].content)
    print("\nSentiment\n" + "="*50)
    print(results["sentiment"].content) 