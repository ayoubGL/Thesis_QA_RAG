from llama_index.core import QueryBundle
from llama_index.core.retrievers import BaseRetriever
from typing import Any, List
from llama_index.vector_stores.postgres import PGVectorStore
from llama_index.core.vector_stores import VectorStoreQuery
from llama_index.core.schema import NodeWithScore

class Retriever(BaseRetriever):
    """Retriever over a postgres vector store."""
    
    def __init__(
        self, 
        vector_store: PGVectorStore,
        embed_model: Any,
        query_mode: str = "default",
        similarity_top_k : int = 20
    )-> None:
        """Init parameter """
        self._vector_Store = vector_store,
        self._embed_model = embed_model,
        self._query_mode = query_mode
        self._similarity_top_k = similarity_top_k
        super().__init__()
        
    def _retrieve(self, query_bundel: QueryBundle):
        """Retriever"""
        query_embeddings = self._embed_model.embed_query(
            query_bundel.query_str
        )
        
        vector_store_query = VectorStoreQuery(
            query_embedding=query_embeddings,
            similarity_top_k=self._similarity_top_k,
            mode = self._query_mode,
        )
        query_results = self._vector_store.query(vector_store_query)

        nodes_with_scores = []
        
        for index, node in enumerate(query_results.nodes):
            
            if query_results.similarities is not None:
                score = query_results.similarities[index]
            nodes_with_scores.append(NodeWithScore(node=node, score=score))

        return nodes_with_scores
