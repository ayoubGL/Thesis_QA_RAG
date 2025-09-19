"""
    Chunking the document into chunks, we will chose SentenceSplitter
    Args:
        chunk_size: the token chunk size of each chunk
        chunk_overlap: Overlapping chunks to reserve the meaning and context
    return:
        Text Nodes with metadata
"""






from pathlib import Path
from networkx import nodes
from llama_index.readers.file import PyMuPDFReader
from llama_index.core.node_parser import SentenceSplitter





class Chunker:
    def __init__(
        doc_path: str,
        chunk_size: int,
        self,
    ):
        self._doc_path = doc_path,
        self._chunk_size = chunk_size
        
        
    def _load_doc(self):
        
        loader = PyMuPDFReader()
        documents = loader.load(file_path=self.doc_path) #Load the docs using path
        
        return documents
    
    def _chunk_doc(self):
        
        text_parser = SentenceSplitter(
            chunk_size = self.chunk_size
        )
        documents = self._load_doc() # the loaded doc
        
        text_chunk = [] # chunks from docs
        doc_idxs = []   # index of each chunk
        
        ## iterate over the doc and chunk using sentenceSplitter
        for doc_idx, docs in enumerate(documents):
            cur_text_chunk = text_parser.split_text(docs.text)
            text_chunk.extend(cur_text_chunk)
            doc_idxs.extend([doc_idx] * len(cur_text_chunk))
        
        return text_chunk, doc_idxs
    
    def _Data_node(self):
        
        nodes = []
        text_chunk, doc_idxs = self._chunk_doc()
        docs = self._load_doc()
        
        for idx, text_chunk in enumerate(text_chunk):
            
            node = TextNode(
                text = text_chunk

            )
            str_doc = docs[doc_idxs[idx]]
            node.metadata = str_doc.metadata
            nodes.append(node)
        
        return nodes
        
    
