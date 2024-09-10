from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        result: chain result
        question: question
        calculationView: calculation view target
        prompt: prompt template object
        prompt_with_context: prompt template with context from vector search
        subqueries: decomposed queries
    """
    result: str
    question: str
    calculationView: str
    prompt: object
    prompt_with_context: object
    subqueries: object