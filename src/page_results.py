import streamlit as st
import pandas as pd

def user_interface():

    text =  """
            # Y estas son las respuestas
            ¿Habrá funcionado?
            """
    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed


def logic():

    try:
        nlp = st.session_state['nlp_model']
        context = st.session_state['context_text']
        questions = st.session_state['questions_text']

    except KeyError:

        text =  """
                Completa los pasos en orden, porfi.

                Necesitamos configurar un modelo, unas preguntas y un contexto antes de seguir.
                """
        st.write(text)
        return

    results = []

    for question in questions:

        inp = {
                  "question": question,
                  "context": context
              }

        res = nlp(inp)

        results.append(res)

    # Formatting results
    results_df = pd.DataFrame(results)
    results_df['question'] = questions
    selected_cols = ['score', 'question', 'answer']
    results_df = results_df[selected_cols]

    st.dataframe(results_df)

    # For manual inspection
    text = "Texto de la intranet"
    expander = st.expander(text)
    expander.write(context)


def results():

    pressed = user_interface()

    if pressed:
        logic()