import streamlit as st

def questions(result):

    text =  """
            # ¿Qué queremos preguntar?
            """

    st.write(text)


    question1_text = "Pregunta 1: "
    question2_text = "Pregunta 2: "
    question3_text = "Pregunta 3: "
    default_text = ""

    question1 = st.text_input(question1_text, default_text)
    question2 = st.text_input(question2_text, default_text)
    question3 = st.text_input(question3_text, default_text)
    questions = [question1, question2, question3]

    text = """
           Preguntas de ejemplo:

           * When is the reduced day?
           * What is the training budget?
           * What are the social benefits?
           """

    st.write(text)

    return questions