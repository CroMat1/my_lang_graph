from typing import List, TypedDict


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        documents: result of chain
        calculationView: calculation view target
        prompt: prompt template object
        prompt_with_context: prompt template with context from vector search
        subqueries: decomposed queries
    """

    question: str
    documents: dict
    calculationView: List[str]
    prompt: object
    prompt_with_context: object
    subqueries: object