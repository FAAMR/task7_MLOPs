from src.graph_build import build_graph

try:
    # Build the graph
    graph = build_graph()
    
    # Generate the mermaid diagram code
    print("Copy the code below into your README.md or mermaid.live:\n")
    print("```mermaid")
    print(graph.get_graph().draw_mermaid())
    print("```")
    
except Exception as e:
    print(f"Error visualizing graph: {e}")