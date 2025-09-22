# from RAGPipeline.BootPipe import initialize_pipeline
from RAGPipeline.InitPipe import run_query
import logging 








def ragResponse(query, status, retriever, llm):
    
    # if not_first == False:
    #     llm_str = "llama3.1"
    #     retriever, llm = initialize_pipeline(doc_path="./static/pdf/thesis.pdf", 
    #                                         llm_str=llm_str)  # run once
    
    # Ensure that the RAG pipeline is only booted once not every time we have a query
    while status:
        # my_query = input("Enter your query (or 'exit' to quit): ")
        if query.lower() == "Thank you":
            return "Have a good day!!"
            
        answer = run_query(retriever, query, llm=llm) 
        # print("Answer:", answer.response)
        return answer.response

    