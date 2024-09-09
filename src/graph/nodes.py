from src.chains.decomposer import query_analyzer
from src.chains.vector_graph_chain import get_vector_graph_chain

def decomposer(state: GraphState):
    
    '''Returns a dictionary of at least one of the GraphState'''    
    '''Decompose a given question to sub-queries'''
    
    question = state["question"]
    subqueries = query_analyzer.invoke(question)
    return {"subqueries": subqueries, "question":question}

def vector_search(state: GraphState):
    
    ''' Returns a dictionary of at least one of the GraphState'''
    ''' Perform a vector similarity search and return article id as a parsed output'''

    question = state["question"]
    queries = state["subqueries"]
    
    vector_graph_chain = get_vector_graph_chain()
    
    chain_result = vector_graph_chain.invoke({
        "query": queries[0].sub_query},
    )
    # Convert the result to a list of DocumentModel instances
    documents = [DocumentModel(**doc.dict()) for doc in chain_result['source_documents']]
    extracted_data = [{"title": doc.extract_title(), "article_id": doc.metadata.article_id} for doc in documents]
    article_ids = [("article_id", doc.metadata.article_id) for doc in documents]
    
    return {"article_ids": article_ids, "documents": extracted_data, "question":question, "subqueries": queries}
