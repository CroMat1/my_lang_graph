from dotenv import load_dotenv
import os

# tag::Neo4jGraph[]
from langchain_community.graphs import Neo4jGraph

load_dotenv(dotenv_path="config/.env")

graph = Neo4jGraph(
    url=os.getenv("NEO4J_URI"),
    username=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
)


#end::Neo4jGraph[]