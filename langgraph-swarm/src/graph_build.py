# src/graph_build.py

from langgraph.graph import StateGraph
from src.nodes import supervisor_node, researcher_node, writer_node, qa_node
from src.state import WorkflowState

def build_graph():
    graph = StateGraph(state_schema=WorkflowState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)
    graph.add_node("qa", qa_node)

    # Conditional edges from supervisor
    def route_supervisor(state):
        return state.next_step

    graph.add_conditional_edges(
        "supervisor",
        route_supervisor,
        {
            "researcher": "researcher",
            "writer": "writer",
            "qa": "qa",
            "end": "__end__"
        }
    )

    # Regular edges back to supervisor
    graph.add_edge("researcher", "supervisor")
    graph.add_edge("writer", "supervisor")
    graph.add_edge("qa", "supervisor")

    # Set entry point
    graph.set_entry_point("supervisor")

    return graph.compile()