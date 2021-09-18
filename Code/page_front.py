import streamlit as st

def front():

    text =  """
            # ¡Oh, un modelo de ML, vamos a desplegarlo! - Machine learning para adultos 
            
            ¡Enhorabuena por llegar a uno de los talleres más molones de la PyConEs 2021.!
            
            Hoy vas a trastear con:

            1. NLP, que son las siglas de Natural Language Processing. No tiene nada que ver con Neuro-Linguistic Programming.
            2. Arquitecturas de redes neurolanes basadas en Transformers (usando la famosa librería HuggingFace).
            3. Resolviendo la tarea conocida como "**Extractive Question Answering**".
            """
    st.write(text)


    image_huggingface_url = "https://avatars.githubusercontent.com/u/25720743?s=200"
    st.image(image_huggingface_url)

    text = "HuggingFace"
    url = "https://huggingface.co/"
    link = "[%s](%s)" % (text, url)
    st.write(link)