import streamlit as st

def user_interface():

    text =  """
            # Nos descargamos un modelo que pueda hacer frente a esta tarea
            """
    st.write(text)
    
    defaul_model_name = ""
    model_name = "Escoge el modelo que quieres usar"
    
    user_input = st.text_input(model_name, defaul_model_name)
    
    text = """
           Te recomendamos este: 
           
           deepset/roberta-base-squad2

           Más información aquí: https://huggingface.co/deepset/roberta-base-squad2
           """
    st.write(text)

    return user_input


def logic(user_input):

    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
    
    try:
        nlp = pipeline("question-answering", model=user_input, tokenizer=user_input)
        text = "Modelo correctamente descargado"
        st.write(text)

        st.session_state['nlp_model'] = nlp

    except OSError:
            text = "Modelo no encontrado"
            st.write(text)

def download_model():

    user_input = user_interface()

    if user_input:

            text = "Descargar modelo"
            pressed = st.button(text)

            if pressed:
                return logic(user_input)
