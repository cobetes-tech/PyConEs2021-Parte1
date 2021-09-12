import streamlit as st

def user_interface():

    text =  """
            # Y estas son las respuestas
            ¿Habremos tenido suerte?
            """

    st.write(text)

    text = "Calcular resultados"
    pressed = st.button(text)

    return pressed


def logic(result):

    st.write(result.keys())

    nlp = result['3. Descargar un modelo']
    context = result['4. Contexto']
    questions = result['5. Preguntas']

    # Debug
    st.write(nlp)
    st.write(context)
    st.write(questions)

    for question in questions:

        inp = {
                  "question": question,
                  "context": context
              }

        res = nlp(inp)

        st.write(res)


def results(result):

    pressed = user_interface()

    if pressed:
        logic(result)