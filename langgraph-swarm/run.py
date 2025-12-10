# run.py

from src.graph_build import build_graph
from src.state import WorkflowState

def main():
    topic = input("Enter topic to research: ")
    
    # Create state as a dictionary
    initial_state = {
        "topic": topic,
        "research": None,
        "draft": None,
        "review": None,
        "next_step": "supervisor"
    }
    
    graph = build_graph()
    result = graph.invoke(initial_state)   # Run the workflow
    
    print("\n===== Workflow completed! =====")
    print("Research:", result.get("research"))
    print("Draft:", result.get("draft"))
    print("Review:", result.get("review"))

if __name__ == "__main__":
    main()