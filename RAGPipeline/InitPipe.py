# query_pipeline.py
from RAGPipeline.QueryEngine import QueryEngine
from typing import Any, List


def run_query(retriever, query, llm:Any):
    
    engine = QueryEngine(
        retriever=retriever,
        query=query,
        initOllama=llm,
    )
    answer = engine.get_response()  
    return answer


