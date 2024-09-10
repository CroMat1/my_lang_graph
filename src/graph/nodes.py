from src.chains.decomposer import query_analyzer
from src.chains.vector_graph_chain import get_vector_graph_chain
from src.chains.cypher_qa import get_graph_qa_chain_with_context

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
    
    result = neo4j_cv_vector_index.similarity_search_with_score(queries[0].sub_query, k=1)
    
    Document, score = result[0]
    uri = re.search(r'uri:\s*(.+)', Document.page_content).group(1)

    return {"calculationView": uri, "question": question, "subqueries": queries}

def prompt_template_with_context(state: GraphState):

    '''Returns a dictionary of at least one of the GraphState'''
    '''Create a dynamic prompt template for graph qa with context chain'''
    
    question = state["question"]
    queries = state["subqueries"]

    # Create a prompt template
    prompt_with_context = create_few_shot_prompt_with_context(state)
    
    return {"prompt_with_context": prompt_with_context, "question":question, "subqueries": queries}

def cypher_qa_with_context(state: GraphState):

    question = state["question"]
    queries = state["subqueries"]

    graph_qa_chain = get_graph_qa_chain_with_context(state)

    result = graph_qa_chain.invoke(
        {
            "query": queries[1].sub_query,
        },
    )

    return {"result": result, "prompt_with_context":prompt_with_context, "subqueries": queries}
