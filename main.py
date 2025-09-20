from RAGPipeline.BootPipe import initialize_pipeline
from RAGPipeline.InitPipe import run_query
import logging 
import streamlit as st

def interface():

    st.set_page_config(page_title = "Thesis defense  Assistant")

    st.title("Thesis defense assistant")
    st.write("Ask question related to my thesis")


    # Query input
    query = st.text_input("Enter you question:")

    # Get the answer
    

    if st.button("submit"):
        if query.strip():
            st.success(f"Your question: {query}")
            st.info("Answer will appear here (hook up retriever)")
        else:
            st.warning("Please enter a question before submitting.")
            






if __name__ == "__main__":
    llm_str = "llama3.1"
    retriever, llm = initialize_pipeline(doc_path="./static/pdf/thesis.pdf", llm_str=llm_str)  # run once
   

    # Ensure that the RAG pipeline is only booted once not every time we have a query
    while True:
        
        my_query = input("Enter your query (or 'exit' to quit): ")
        if my_query.lower() == "exit":
            break
        answer = run_query(retriever, my_query, llm=llm)
        logging.basicConfig(level=logging.WARNING)  
        print("Answer:", answer.response)


    