from langchain.chains import GraphCypherQAChain
from src.conn.llm import llm
from src.conn.neo4jGraph import Neo4jGraph

from langchain.chains import GraphCypherQAChain
from src.agent.prompt import prompt_template

def get_graph_qa_chain_with_context(state: GraphState):
    
    """Create a Neo4j Graph Cypher QA Chain. Using this as GraphState so it can access state['prompt']"""
    
    prompt_with_context = state["prompt_with_context"] 
    
    graph_qa_chain = GraphCypherQAChain.from_llm(
        graph=Neo4jGraph,
        cypher_llm=llm,
        qa_llm=llm,
        cypher_prompt=prompt_with_context,
        verbose=True,
        validate_cypher = True,
        #return_direct=True,
        exclude_types = ["Session","Message","Chunk"],
        use_function_response=True,
        function_response_system="Respond as gentlemen!",
        )
    return graph_qa_chain
