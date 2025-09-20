import streamlit as st
import time


# page config

st.set_page_config(page_title = "Thesis defense  Assistant")

st.title("Thesis defense assistant")
st.write("Ask question related to my thesis")



# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
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

# response = None

# Display
if prompt :
    time.sleep(2)
    response = "The RAG will answer you soon"
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"RAG", "content":response})