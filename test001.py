from src.chains.vector_graph_chain import get_vector_graph_chain, neo4j_cv_vector_index
import re 

question = "Find Calculation View CVHSB06_0"

result = neo4j_cv_vector_index.similarity_search_with_score(question, k=2)

Document, score = result[0]
uri = re.search(r'uri:\s*(.+)', Document.page_content).group(1)

print(Document.metadata['name'])
print(Document.metadata['package'])
print(uri)
print(score)

print('*******')
#print(chain_result['source_documents'])

print('stop')