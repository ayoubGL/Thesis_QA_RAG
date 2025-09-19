from llama_index.core.schema import TextNode
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings


class Embedder:
    """
    Generate embeddings for each TextNode using FastEmbed.

    Args:
        nodes (list[TextNode]): The list of nodes to embed
        embedding_model (str): The embedding model name

    Returns:
        list[TextNode]: Nodes with embeddings stored in node.embedding
    """

    def __init__(self, nodes: list[TextNode], embedding_model: str):
        self._nodes = nodes
        self._embedding_model = embedding_model

    def _node_embeddings(self):
        try:
            embd_model = FastEmbedEmbeddings(model_name=self._embedding_model)

            # Extract texts for all nodes
            texts = [node.get_content(metadata_mode="all") for node in self._nodes]

            # Embed all at once (faster than looping)
            all_embeddings = embd_model.embed_documents(texts)

            # Attach embeddings back to nodes
            for node, embedding in zip(self._nodes, all_embeddings):
                node.embedding = embedding

            print("Embeddings successfully created for all nodes.")
            return self._nodes, embd_model

        except Exception as e:
            print(f"Failed to create embeddings: {e}")
            return []
