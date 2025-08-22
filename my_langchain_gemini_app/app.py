import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough


google_api_key = os.environ["GOOGLE_API_KEY"]

if google_api_key == "YOUR_GEMINI_API_KEY_HERE" or not google_api_key:
    print("Error: Please replace 'YOUR_GEMINI_API_KEY_HERE' with your actual Google API key in app.py.")
    exit()

# Initialize the Gemini model using LangChain's integration
# CHANGED MODEL NAME: from "gemini-pro" to "gemini-1.5-flash-latest" for better availability
# Added verbose=True to see more detailed logging from the LLM calls
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.7, google_api_key=google_api_key, verbose=True)

def simple_gemini_call(prompt: str):
    """
    Performs a basic call to the Gemini model with a single prompt via LangChain.
    """
    print(f"\n--- Simple LangChain Gemini Call ---")
    print(f"Prompt: {prompt}")
    
    response = llm.invoke(prompt)
    
    print(f"Response: {response.content}")
    print("-" * 30)

def chat_gemini_call(user_question: str):
    """
    Demonstrates a more structured chat interaction using LangChain's prompt template.
    """
    print(f"\n--- LangChain Chat Gemini Call ---")
    print(f"User Question: {user_question}")

    chat_template = ChatPromptTemplate.from_messages(
        [
            SystemMessage("You are a helpful AI assistant. Answer the user's questions concisely."),
            HumanMessage(content="{question}"),
        ]
    )

    # Removed: chain.verbose = True as it's not a valid attribute for RunnableSequence
    chain = chat_template | llm | StrOutputParser()

    response = chain.invoke({"question": user_question})

    print(f"Response: {response}")
    print("-" * 30)

def advanced_chain_example(topic: str):
    """
    Demonstrates a multi-step chain using LangChain's Runnable interface for more complex workflows.
    """
    print(f"\n--- LangChain Advanced Chain Example ---")
    print(f"Topic: {topic}")

    fact_template = ChatPromptTemplate.from_messages([
        SystemMessage("You are an expert. Answer the user question"),
        HumanMessage(content="Topic: {topic}")
    ])

    summary_template = ChatPromptTemplate.from_messages([
        SystemMessage("You are a summarization expert. "),
        HumanMessage(content="Facts: {facts}")
    ])

    # Removed: fact_generation_chain.verbose = True
    fact_generation_chain = fact_template | llm | StrOutputParser()

    full_chain = (
        {"topic": RunnablePassthrough()}
        | {"facts": fact_generation_chain, "topic": RunnablePassthrough()}
        | summary_template
        | llm
        | StrOutputParser()
    )
    # Removed: full_chain.verbose = True
    
    response = full_chain.invoke({"topic": topic})

    print(f"Summary of facts about '{topic}': {response}")
    print("-" * 30)


if __name__ == "__main__":
    simple_gemini_call("What is the capital of France?")

    # Changed prompt to be unambiguous
    chat_gemini_call("What is the main function of the heart in the human body?")

    # Changed topic to a well-known one
    advanced_chain_example("Jupiter")