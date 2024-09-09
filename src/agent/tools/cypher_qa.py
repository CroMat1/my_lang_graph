from langchain.chains import GraphCypherQAChain
from src.conn.llm import llm
from src.conn.neo4jGraph import Neo4jGraph
from graph import graph

from langchain.chains import GraphCypherQAChain
from src.agent.prompt import prompt_template

cypher_qa = GraphCypherQAChain.from_llm(
    cypher_llm = llm,
    qa_llm = llm,
    validate_cypher= True,
    graph=Neo4jGraph,
    verbose=False,
    cypher_prompt=prompt,
    return_direct = True
)
