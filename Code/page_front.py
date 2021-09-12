import streamlit as st

def front():

    image_huggingface_url = "https://avatars.githubusercontent.com/u/25720743?s=200"

    text =  """
            # Question Answering

            NLP con transformers

            PyConEs 2021
            """


    st.write(text)
    st.image(image_huggingface_url)