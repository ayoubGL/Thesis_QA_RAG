from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.llms.ollama import Ollama
from typing import Any, List


class QueryEngine:
    
    def __init__(
        self,
        llm: str,
        retriever: Any,
        query: str
       
    ):
        self._llm = llm
        self._retriever = retriever
        self._query = query
    
    def _response(self):
        try:
            # Call ollama model
            llm_ol = Ollama(
                model = self._llm,
                request_timeout = 120,
                context_window=8000
            )
            
            query_engine =RetrieverQueryEngine.from_args(self._retriever, 
                                            llm=llm_ol)
            answer = query_engine.query(self._query)
            return answer
        except Exception as e:
            print(f"Something wrong {e}")
            return None