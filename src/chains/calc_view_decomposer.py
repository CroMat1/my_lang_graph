import os
import datetime
from typing import Literal, Optional, Tuple

from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticToolsParser
from langchain_core.prompts import ChatPromptTemplate

from src.conn.llm import llm

class GetCalcView(BaseModel):
    """Decompose a given question/query into sub-queries"""

    sub_query: str = Field(
        ...,
        description="A unique paraphrasing of the original questions.",
    )

system = """
You are an expert on extracting calculation view name from the question.
Perform the calculation view name extraction. Given a user question extract name and package from it.

Instructions:
CV, calc view, c view refers to Calculation View

Here is example:
Question: Give me the fields of Calculation View CVHB001.
Answers:
CalculationView : calculation view CVHB001
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "{question}"),
    ]
)

llm_with_tools = llm.bind_tools([GetCalcView])
parser = PydanticToolsParser(tools=[GetCalcView])
calcView = prompt | llm_with_tools | parser