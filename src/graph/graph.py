# Import Python Libraries
from langgraph.graph import START, END, StateGraph
from src.graph.state import GraphState
from src.graph.nodes import decomposer, vector_search, cypher_qa_with_context, prompt_template_with_context

workflow = StateGraph(GraphState)

# Nodes for graph qa with vector search
workflow.add_node("DECOMPOSER", decomposer)
workflow.add_node("VECTOR_SEARCH", vector_search)
workflow.add_node("PROMPT_TEMPLATE_WITH_CONTEXT", prompt_template_with_context)
workflow.add_node("GRAPH_QA_WITH_CONTEXT", cypher_qa_with_context)

# # Edges for graph qa with vector search
workflow.add_edge(START, "DECOMPOSER")
workflow.add_edge("DECOMPOSER", "VECTOR_SEARCH")
workflow.add_edge("VECTOR_SEARCH", "PROMPT_TEMPLATE_WITH_CONTEXT")
workflow.add_edge("PROMPT_TEMPLATE_WITH_CONTEXT", "GRAPH_QA_WITH_CONTEXT")
workflow.add_edge("GRAPH_QA_WITH_CONTEXT", END)

# # Set conditional entry point for vector search or graph qa
# workflow.set_conditional_entry_point(
#     route_question,
#     {
#         'decomposer': DECOMPOSER, # vector search
#         'prompt_template': PROMPT_TEMPLATE # for graph qa
#     },
# )

app = workflow.compile()

#app.get_graph().draw_mermaid_png(output_file_path="graph.png")