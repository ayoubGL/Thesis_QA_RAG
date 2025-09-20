# setup_pipeline.py
from Chunker import TextChunker
from NodeEmbedder import Embedder
from DBConnect import Connector
from configparser import ConfigParser
from Retriever import Retriever
import time
from llama_index.llms.ollama import Ollama




def initialize_pipeline(doc_path:str,  llm_str:str, chunk_size=1024,):
    """"
        Pipeline initializer that ensure that everything done only once, not for every user query
        Args:
            docs_path : document path
            llm_str: LLM of choice, check Ollama
            Chunk_size: size of chunks for docs.
    
        return:
            retriever: retriver instance 
            llm: running instance of ollama
    """




    print("Chunking docs...")
    chunker = TextChunker(doc_path, chunk_size)
    text_nodes = chunker._Data_node()
    time.sleep(1)

    print("Constructing and building text embeddings...")
    embedding_model = "BAAI/bge-small-en"
    embedder = Embedder(text_nodes, embedding_model)
    vector_nodes, emb_model = embedder._node_embeddings()

    print("Storing in Vector Database...")
    config = ConfigParser()
    config.read("db_config.ini")

    connect = Connector(
        config["database"]["databasename"],
        config["database"]["host"],
        config["database"]["password"],
        int(config["database"]["port"]),
        config["database"]["user"],
        config["database"]["table_name"],
        vector_nodes
    )

    vector_store = connect._connect_storeVector()

    retriever = Retriever(
        vector_store,
        emb_model,
        query_mode="default",
        similarity_top_k=20
    )

    # Initialize the Ollama Model
    OllamaLm =  Ollama(
                model = llm_str,
                request_timeout = 120,
                context_window=8000
            )
    
    
    print("Pipeline initialized successfully!")
    
    
    
    
    return retriever, OllamaLm
