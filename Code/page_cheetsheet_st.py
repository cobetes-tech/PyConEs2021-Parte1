import streamlit as st

def cheetsheet_st():

    st.write("""
            # Comandos que nos pueden ser de ayuda:

            1. Button
            2. Expand
            3. El crusaito
            """
            )


"""
Referencias de codigo
"""

"""
option = st.sidebar.selectbox("Escoge", [1, 2, 3, 4])


if option == 1:

    with st.expander("Saber más"):
        st.write("habia una vez un circo")
else:
    st.write("pepino")
"""

"""
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
"""


"""
Notas

Con el st.sidebar metemos cosas en la barra lateral, por ejemplo st.sidebar.selectbox
con el expander lo que metemos es un menú desplegable, una caja que se amplía y muestra el contenido, como la de los spoilers
con button tenemos un boton que recogemos un booleano
y con el st.columns(n) podemos generar n columnas. una vez creados los objetos, tendrían las mismas propiedades que st

"""