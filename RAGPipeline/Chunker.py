from langchain_community.document_loaders import PyPDFLoader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import TextNode
from pathlib import Path
from llama_index.readers.file import PyMuPDFReader





class TextChunker:
    
    """
    Chunking the Pdf document and return all the chunks.

    Args:
        doc_path : The path of document 
        chunk_size : The size of chunks

    Returns:
        list[TextNode]: Nodes with embeddings stored in node.embedding
    """

    
    def __init__(self, doc_path: str, chunk_size: int):
        self._doc_path = doc_path
        self._chunk_size = chunk_size
        
    def _load_doc(self):
        loader = PyMuPDFReader()
        documents = loader.load(file_path=self._doc_path)  # Load docs using path
        return documents
    
    def _chunk_doc(self):
        text_parser = SentenceSplitter(chunk_size=self._chunk_size)
        documents = self._load_doc()
        
        text_chunk = []
        doc_idxs = []
        
        for doc_idx, docs in enumerate(documents):
            cur_text_chunk = text_parser.split_text(docs.text)
            text_chunk.extend(cur_text_chunk)
            doc_idxs.extend([doc_idx] * len(cur_text_chunk))
        
        return text_chunk, doc_idxs
    
    def _data_node(self):
        nodes = []
        text_chunk, doc_idxs = self._chunk_doc()
        docs = self._load_doc()
        
        for idx, chunk in enumerate(text_chunk):
            node = TextNode(text=chunk)
            node.metadata = docs[doc_idxs[idx]].metadata
            nodes.append(node)
        
        return nodes
