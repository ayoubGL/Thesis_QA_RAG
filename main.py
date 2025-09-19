import NodeEmbedder, Chunker, DBConnect
import time
from configparser import ConfigParser





def main():


    doc_path = "./pdf/thesis.pdf"
    chunk_size = 1024

    print("chunking docs....")
    TextdataNodes = Chunker(doc_path, chunk_size)
    time.sleep(3)
    
    print("Construct and build text embeddings....")
    embedding_model = "BAAI/bge-small-en"
    vectorNodes = NodeEmbedder(TextdataNodes, embedding_model)
    
    print("Vector Store in DataBase...")
    time.sleep(3)  
    
    
    ## Database configuration
    config = ConfigParser()
    config.read("db_config.ini")
    
        db_name = config["database"][""]
         = config["database"][""]
        password = config["database"][""]
        port = config["database"][""]
        user = config["database"][""]
        table_name = config["database"][""]
        
      
    