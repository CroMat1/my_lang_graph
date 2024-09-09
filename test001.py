from src.chains.decomposer import query_analyzer

question = "How many fields are in cv CB8892"

print(query_analyzer.invoke(question))
