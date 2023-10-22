import streamlit as st
import pandas as pd
import json

# Para menor uso de memoria se limita la app en la fase de desarrollo
limite_recetas = 10


# se ajustan los datos para utilizarlos en las funciones
def cargar_recetas(ruta):
    with open(ruta, encoding='utf8') as contenido:
        return pd.DataFrame(json.load(contenido))


# Aqui se despliega el login y el registro de la pagina
def desplegar_form(option):
    col1, col2 = st.columns(2)

    # Este es para el registro de la pagina
    if option == 'registro':
        with st.form(key='registration_form'):
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            confirm_password = st.text_input('Confirmar contraseña', type='password')
            register_button = st.form_submit_button('Registrarse')

            # Para llamar a la funcion de registro
            if register_button:
                utils.registro(username, password, confirm_password)

    # Este es para el login de la pagina
    elif option == 'ingreso':
        with st.form(key='login_form'):
            col2.header('Iniciar Sesión')
            username = st.text_input('Nombre de usuario')
            password = st.text_input('Contraseña', type='password')
            login_button = st.form_submit_button('Iniciar Sesión')

            # Para llamar a la funcion de login
            if login_button:
                utils.ingreso(username, password)


# Visualizacion de cada receta
def detalles_abiertos(receta):
    # Verifica si se debe mostrar los detalles de esta receta
    # if receta['id'] in detalles_abiertos and detalles_abiertos[receta['id']]:
    with st.expander(f"Ver Detalles de {receta['name']}"):
        st.subheader(receta["name"])

        # Detalles de la receta (puedes usar un bucle para iterar sobre los datos)
        st.header("Detalles de la Receta")
        st.write(f"**Descripción:** {receta['description']}")
        st.write(f"**Autor:** {receta['author']}")
        st.write(f"**Calificación:** {receta['rattings']}")

        # Ingredientes
        st.header("Ingredientes")
        for i, ingrediente in enumerate(receta["ingredients"]):
            st.write(f"{i + 1}. {ingrediente}")

        # Pasos
        st.header("Pasos")
        for i, paso in enumerate(receta["steps"]):
            st.write(f"{i + 1}. {paso}")

        # Tiempos
        st.header("Tiempos")
        preparacion = receta['times'].get('Preparation', 'No Time')
        cocina = receta['times'].get('Cooking', 'No Time')
        st.write(f"**Preparación:** {preparacion}")
        st.write(f"**Cocción:** {cocina}")

        # Otros detalles
        st.header("Otros Detalles")
        st.write(f"**Porciones:** {receta['serves']}")
        st.write(f"**Dificultad:** {receta['difficult']}")
        st.write(f"**Conteo de votos:** {receta['vote_count']}")
        st.write(f"**Subcategoría:** {receta['subcategory']}")
        st.write(f"**Tipo de platillo:** {receta['dish_type']}")
        st.write(f"**Categoría principal:** {receta['maincategory']}")


# else:
#      # Si no se debe mostrar, muestra solo el nombre de la receta como enlace
#      st.write(f"**Receta:** [{receta['name']}]({receta['url']})")

# Aqui estan las recetas

def recetas_saludables():
    # Ruta del archivo recetas saludables json temporal para usar en consola local
    ruta_saludable = '..\\datos\\saludables.json'
    df_recetas_saludables = cargar_recetas(ruta_saludable)

    # Aqui se despliegan las recetas saludables
    st.title("Recetas saludables")

    if limite_recetas:
        aux_limite = limite_recetas
    else:
        aux_limite = len(df_recetas_saludables)

    for index, receta in df_recetas_saludables.iterrows():

        if aux_limite > 0:
            aux_limite -= 1
        else:
            break

        # Mostrar la imagen previa con borde
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Crear un elemento expansible con los detalles de la receta
        # with st.expander(f"Ver Detalles de {receta['name']}"):
        #     # Cuando se hace clic en el botón, actualiza la variable de estado
        #     if st.button(f"Ver Detalles de {receta['name']}"):
        #         detalles_abiertos = receta['id']

        #     # Llama a la función para mostrar los detalles
        detalles_abiertos(receta)


def recetas_presupuesto():
    # Ruta del archivo recetas presupuesto json temporal para usar en consola local
    ruta_presupuesto = '..\\datos\\presupuesto.json'
    df_recetas_presupuesto = cargar_recetas(ruta_presupuesto)

    # Aqui se despliegan las recetas de presupuesto
    st.title("Recetas sencillas")
    for index, receta1 in df_recetas_presupuesto.iterrows():
        # Aqui van a ir las recetas de presupuesto
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta1['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta1)


def recetas_horneados():
    # Ruta del archivo recetas presupuesto json temporal para usar en consola local
    ruta_horneados = '..\\datos\\horneados.json'
    df_recetas_horneados = cargar_recetas(ruta_horneados)

    # Aqui se despliegan las recetas de presupuesto
    st.title("Recetas horneadas")
    for index, receta2 in df_recetas_horneados.iterrows():
        # Aqui van a ir las recetas de presupuesto
        st.markdown(
            f"""
            <div style="border: 2px solid #ccc; padding: 5px; text-align: center;">
                <img src="{receta2['image']}" alt="Imagen de la receta" style="max-width: 100%; border-radius: 5px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
        detalles_abiertos(receta2)


# Pie de pagina aqui se van a mirar el contacto y los desarrolladores
def footer():
    st.markdown("""
    <style>
    .reportview-container .main footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <footer style='position: fixed; bottom: 0; width: 100%; height: 50px; background-color: #f5f5f5; text-align: left; padding-top: 15px; padding-left: 10px;'>
        Desarrollado por: Daniel Garzon Y Luis Moreno | Contacto: dgarzonac@unal.edu.co</a> Y lumorenoc@unal.edu.co</a>
    </footer>
    """, unsafe_allow_html=True)
