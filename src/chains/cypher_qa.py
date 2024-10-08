from langchain.chains import GraphCypherQAChain
from src.conn.llm import llm
from src.conn.neo4jGraph import graph
from src.graph.state import GraphState

def get_graph_qa_chain_with_context(state: GraphState):
    
    """Create a Neo4j Graph Cypher QA Chain. Using this as GraphState so it can access state['prompt']"""
    
    prompt_with_context = state["prompt_with_context"] 
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
        graph=graph,
        cypher_llm=llm,
        qa_llm=llm,
        cypher_prompt=prompt_with_context,
        verbose=True,
        validate_cypher = True,
        return_direct=True,
        exclude_types = ["Session","Message","Chunk"],
        use_function_response=True,
        function_response_system="Respond as Hana Calculation View Expert",
        )
        
    return graph_qa_chain
