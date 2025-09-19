# from Chunker import TextChunker
# from NodeEmbedder import Embedder
# from DBConnect import Connector
# from configparser import ConfigParser
# import time
# from Retriever import Retriever
# from QueryEngine import QueryEngine

    


# def main():


#     doc_path = "./pdf/thesis.pdf"
#     chunk_size = 1024

#     print("Chunking docs...")
#     chunker = TextChunker(doc_path, chunk_size)
#     text_nodes = chunker._Data_node()
#     time.sleep(1)

    

    
#     print("Constructing and building text embeddings...")
#     embedding_model = "BAAI/bge-small-en"
#     embedder = Embedder(text_nodes, embedding_model)
#     vector_nodes, emb_model = embedder._node_embeddings() 
    
#     print(" Storing in Vector Database...")
    
    
#     # Database configuration
#     config = ConfigParser()
#     config.read("db_config.ini")
    
#     db_name = config["database"]["databasename"]
#     host = config["database"]["host"]
#     password = config["database"]["password"]
#     port = config["database"]["port"]
#     user = config["database"]["user"]
#     table_name = config["database"]["table_name"]
   

#     # Initialize, create and store nodes in vector database
#     # DBconnect = Connector()
#     connect = Connector(db_name,host, 
#               password, 
#               port, 
#               user, 
#               table_name,
#               vector_nodes)
    
#     vector_store = connect._connect_storeVector()
#     # print(vector_store)
      
#     retriever = Retriever(
#         vector_store,
#         emb_model,
#         query_mode = "default",
#         similarity_top_k = 20   
#     )
    
#     my_query = "What is a best recommender system"
    
#     answer = QueryEngine(
#         llm = "llama3.1",
#         retriever=retriever,
#         query=my_query
#     )
#     print(str(answer._response()))

# if __name__ == "__main__":
  
#     main()


# query_pipeline.py
from QueryEngine import QueryEngine
from bootPipe import initialize_pipeline

def run_query(retriever, query, llm="llama3.1"):
    engine = QueryEngine(
        llm=llm,
        retriever=retriever,
        query=query
    )
    answer = engine.get_response()  # assuming you renamed _response → get_response
    return answer


if __name__ == "__main__":
    retriever = initialize_pipeline()  # run once

    while True:
        my_query = input("Enter your query (or 'exit' to quit): ")
        if my_query.lower() == "exit":
            break
        answer = run_query(retriever, my_query)
        print("Answer:", answer)
