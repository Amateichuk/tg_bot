from langgraph.graph import StateGraph, END

from app.graph.state import OrderState
from app.graph.nodes import (
    extract_order,
    classify_message,
    route_message,
    check_order,
)


def create_order_graph():
    graph = StateGraph(OrderState)

    graph.add_node(
        "extract_order",
        extract_order,
    )

    graph.add_node(
        "classify_message",
        classify_message,
    )

    graph.add_node(
        "check_order",
        check_order,
    )

    graph.set_entry_point("extract_order")

    graph.add_edge(
        "extract_order",
        "classify_message",
    )

    graph.add_conditional_edges(
        "classify_message",
        route_message,
        {
            "order": "check_order",
            "question": END,
        },
    )

    graph.add_edge(
        "check_order",
        END,
    )

    return graph.compile()