from llama_index.core.query_engine import RetrieverQueryEngine

from typing import Any, List


class QueryEngine:
    
    def __init__(
        self,
        llm: str,
        retriever: Any,
        query: str,
        initOllama: Any
       
    ):
        self._llm = llm
        self._retriever = retriever
        self._query = query
    
    def get_response(self):
        try:
            query_engine = RetrieverQueryEngine.from_args(self._retriever, 
                                            llm=self._initOllama)
            answer = query_engine.query(self._query)
            return answer
        except Exception as e:
            print(f"Something wrong {e}")
            return None