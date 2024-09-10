import os
import datetime
from typing import Literal, Optional, Tuple

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate

from src.conn.llm import llm

class SubQuery(BaseModel):
    """Decompose a given question/query into sub-queries"""

    sub_query: str = Field(
        ...,
        description="A unique paraphrasing of the original questions.",
    )

system = """You are an expert at converting user questions into Neo4j Cypher queries. \

Perform query decomposition. Given a user question, break it down into two distinct subqueries that \
you need to answer in order to answer the original question.

For the given input question, create a query for similarity search and create a query to perform neo4j graph query.

Instructions:
CV, calc view, c view refers to Calculation View

Here is example:
Question: Give me the fields of Calculation View CVHB001.
Answers:
sub_query1 : Find calculation view CVHB001.
sub_query2 : Give me the fields of Calculation View CVHB001
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

llm_with_tools = llm.bind_tools([SubQuery])
parser = PydanticToolsParser(tools=[SubQuery])
query_analyzer = prompt | llm_with_tools | parser