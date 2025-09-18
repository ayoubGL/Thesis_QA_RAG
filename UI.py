import streamlit as st

# page config

st.set_page_config(page_title = "Thesis defense  Assistant")

st.title("Thesis defense assistant")
st.write("Ask question related to my thesis")


# Query input
query = st.text_input("Enter you question:")

# Catsh & Display

if st.button("submit"):
    if query.strip():
        st.success(f"Your question: {query}")
        st.info("Answer will appear here (hook up retriever)")
    else:
        st.warning("Please enter a question before submitting.")
        

