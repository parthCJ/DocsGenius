from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st

uploadFile = st.file_uploader("Upload the PDF",
                              type="pdf",
                              accept_multiple_files=False
                              )

user_query = st.text_area("Enter your propmt: ", height=150, placeholder="Ask me anything.")

ask_question = st.button("Ask the AI Lawyer")

if ask_question:

    if uploadFile:
        st.chat_message("user").write()


        retrieved_docs = retrieve_docs(user_query)  # Store the retrieved documents first
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)  # Use retrieved_docs
        st.chat_message("AI Lawyer").write(response)
    
    else:
        st.error("Kindly upload a legit PDF file.")