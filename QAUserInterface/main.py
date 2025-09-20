from RAGPipeline.BootPipe import initialize_pipeline
from RAGPipeline.InitPipe import run_query





if __name__ == "__main__":
    llm_str = "llama3.1"
    retriever, llm = initialize_pipeline(doc_path="./static/pdf/thesis.pdf", llm_str)  # run once
   

    # Ensure that the RAG pipeline is only booted once not every time we have a query
    while True:
        my_query = input("Enter your query (or 'exit' to quit): ")
        if my_query.lower() == "exit":
            break
        answer = run_query(retriever, my_query, llm=llm)
        print("Answer:", answer)
