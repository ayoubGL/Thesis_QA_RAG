from RAGPipeline.BootPipe import initialize_pipeline
from RAGPipeline.InitPipe import run_query
import logging 
import streamlit as st
import time
import random
from RAGPipeline.BootPipe import boot_pipe
from mainAssist import ragResponse



    


# page config

st.set_page_config(page_title = "Thesis defense  Assistant")

st.title("Thesis defense assistant")
st.write("Ask question related to my thesis")



# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    print("------ Booting -----")
    retriever_, llm_ = boot_pipe()
    print(" --- llm booted ---")
    st.session_state['retriever'] = retriever_
    st.session_state['llm'] = llm_
    
# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("Questions about my thesis"):
    # Display user messages in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # add to the session
    st.session_state.messages.append({"role":"user", "content":prompt})

print("--- User prompt---", prompt)
# Display
if prompt :
    retriever_ = st.session_state['retriever']
    llm_ = st.session_state['llm']
    answer = ragResponse(query =prompt, status = True, 
              retriever=retriever_, llm= llm_)
    time.sleep(2)
    # response = "The RAG will answer you soon"
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role":"assistant", "content":answer})