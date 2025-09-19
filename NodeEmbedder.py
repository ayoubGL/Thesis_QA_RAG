from llama_index.core.schema import TextNode
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings


"""
Generate a node embeddings for each data note for each generated chunk,
using an embedding model from FastEmebedding

    Chunking the document into chunks, we will chose SentenceSplitter
    Args:
        nodes: datanode
        embedding model: an embedding model 
    return:
        Text Nodes with metadata
"""
class NodeEmbedder:
    
    def __init__(
        nodes: TextNode,
        embedding_model: str,
        self
        ):
        
        self._nodes = nodes
        self._embedding_model = embedding_model
    

    # get the emebbeding for each datanode
    def node_embeddings(self):
        embedding_model = FastEmbedEmbeddings(model_name=self._embedding_model)
        
        for node in self.nodes:
            node_embeddings = self.embedding_model.embed_documents(
                node.get_content(metadata_mode = "all")
            )

            node.embedding = node_embeddings[0]
        return self.nodes