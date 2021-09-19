import streamlit as st

def user_interface():

    text =  """
            # Nos descargamos un modelo de Machine Learning que pueda hacer frente a esta tarea
            """
    st.write(text)
    
    text = "Escoge el modelo que quieres usar"
    st.write(text)

    defaul_model_name = ""
    model_name = "Modelo seleccionado"
    user_input = st.text_input(model_name, defaul_model_name)
    
    pressed = False
    
    if user_input:
        text = "Descargar modelo"
        pressed = st.button(text)

    text = "---"
    st.write(text)

    text = """
           # Te recomendamos este modelo: 
           
           deepset/roberta-base-squad2

           Más información aquí: https://huggingface.co/deepset/roberta-base-squad2
           """
    st.write(text)

    return pressed


def logic(user_input):

    from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
    
    try:
        nlp = pipeline("question-answering", model=user_input, tokenizer=user_input)
        text = "*¡Modelo correctamente descargado!*"
        st.write(text)

        st.session_state['nlp_model'] = nlp

    except OSError:
            text = "Modelo no encontrado"
            st.write(text)


def download_model():

    pressed = user_interface()

    if pressed:
        return logic(user_input)
