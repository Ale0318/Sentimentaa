from textblob import TextBlob
import streamlit as st
from googletrans import Translator

st.set_page_config(page_title="Análisis de Sentimiento")

st.title('Análisis de Sentimiento')

st.image(
    "emoticones.jpg",
    width=250
)

st.subheader(
    "Por favor escribe en el campo de texto la frase que deseas analizar"
)

translator = Translator()

# SIDEBAR
with st.sidebar:

    st.subheader("Polaridad y Subjetividad")

    st.write("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# ANALIZADOR
with st.expander('Analizar texto'):

    text = st.text_input('Escribe por favor: ')

    if text:

        # Traducir
        translation = translator.translate(
            text,
            src="es",
            dest="en"
        )

        trans_text = translation.text

        # Analizar
        blob = TextBlob(trans_text)

        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)

        # POSITIVO
        if polarity > 0:

            st.success('Es un sentimiento Positivo 😊')

            st.image(
                "feliz.png",
                width=220
            )

        # NEGATIVO
        elif polarity < 0:

            st.error('Es un sentimiento Negativo 😔')

            st.image(
                "triste.png",
                width=220
            )

        # NEUTRAL
        else:

            st.warning('Es un sentimiento Neutral 😐')

            st.image(
                "neutral.png",
                width=220
            )
