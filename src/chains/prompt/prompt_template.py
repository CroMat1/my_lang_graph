from langchain_community.vectorstores import Neo4jVector
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

load_dotenv(dotenv_path="config/.env")

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    HuggingFaceEmbeddings(),
    Neo4jVector,
    url = neo4j_url,
    username = neo4j_user,
    password = neo4j_password,
    k=3,
    input_keys=["question"],
)

example_prompt = PromptTemplate.from_template(
    "User input: {question}\nCypher query: {query}"
)

def create_few_shot_prompt_with_context(state: GraphState):

    calculationView = state["calculationView"]

    prefix="""
    You are a Neo4j expert. 
    Given an input question, create a syntactically correct Cypher query to run.
    Here is the schema information\n{schema}. 
    Don't add any preambles, just return the correct cypher query",
    
    The context is correct Calculation View
    Here are the contexts: {context}

    Using the context above create cypher statements and use that to query with the graph
    Below are a number of examples of questions and their corresponding Cypher queries.     
    """

    dynamic_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix="User input: {question}\nCypher query: ",
        input_variables=["question", "schema"],
    )

    return dynamic_prompt
