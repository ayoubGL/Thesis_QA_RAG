# query_pipeline.py
from QueryEngine import QueryEngine
from typing import Any, List


def run_query(retriever, query, llm:Any):
    
    engine = QueryEngine(
        llm=llm,
        retriever=retriever,
        query=query
    )
    answer = engine.get_response()  
    return answer


