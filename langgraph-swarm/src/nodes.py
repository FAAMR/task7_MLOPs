import os
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables (for OPENAI_API_KEY)
load_dotenv()

llm = ChatOllama(model="llama3.2")

def supervisor_node(state):
    print("\n>>> Supervisor Running...")
    # Logic: Check what fields are empty to decide the next step
    if not state.research:
        next_step = "researcher"
    elif not state.draft:
        next_step = "writer"
    elif not state.review:
        next_step = "qa"
    else:
        next_step = "end"
    
    return {"next_step": next_step}

def researcher_node(state):
    print(">>> Researcher Running...")
    
    # Create the prompt
    prompt = f"You are a tech researcher. Provide 3 bullet points of key facts about: {state.topic}"
    messages = [SystemMessage(content="You are a researcher."), HumanMessage(content=prompt)]
    
    # Invoke LLM
    response = llm.invoke(messages)
    
    return {
        "research": response.content,
        "next_step": "supervisor"
    }

def writer_node(state):
    print(">>> Writer Running...")
    
    # Create the prompt using the research from the state
    prompt = f"Write a short paragraph draft about {state.topic} using these research notes: {state.research}"
    messages = [SystemMessage(content="You are a technical writer."), HumanMessage(content=prompt)]
    
    # Invoke LLM
    response = llm.invoke(messages)
    
    return {
        "draft": response.content,
        "next_step": "supervisor"
    }

def qa_node(state):
    print(">>> QA Running...")
    
    # Create the prompt using the draft from the state
    prompt = f"Review this draft for clarity and accuracy. Output 'APPROVED' or a short critique. Draft: {state.draft}"
    messages = [SystemMessage(content="You are a QA editor."), HumanMessage(content=prompt)]
    
    # Invoke LLM
    response = llm.invoke(messages)
    
    return {
        "review": response.content,
        "next_step": "supervisor"
    }