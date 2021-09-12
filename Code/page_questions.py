import streamlit as st

def questions(result):

    text =  """
            # ¿Qué queremos preguntar?
            """

    st.write(text)

    model_name = defaul_model_name = ""

    user_input = st.text_input("1", defaul_model_name)
    user_input = st.text_input("2", defaul_model_name)
    user_input = st.text_input("3", defaul_model_name)

    text = """
           Preguntas de ejemplo:

           * When is the reduced day?
           * What is the training budget?
           * What are the social benefits?
           """

    st.write(text)