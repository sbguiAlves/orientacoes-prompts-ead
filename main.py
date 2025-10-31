import streamlit as st

pages = {
    "Introdução":
        [
            st.Page("pages/Index.py", title="Menu Principal")
        ],
    "Textos": [
        st.Page("pages/graduacao/Grad_Aula.py", title="Template Aula"),
        st.Page("pages/graduacao/Grad_Enc.py", title="Template Encerramento")
    ],
    "Questões": [
        st.Page("pages/Questoes/Simples.py", title="Escolha Simples"),
        st.Page("pages/Questoes/Complexa.py", title="Escolha Complexa"),
        st.Page("pages/Questoes/Assercao-Razao.py", title="Asserção-Razão"),
        st.Page("pages/Questoes/Incompleta.py", title="Afirmação Incompleta"),
        st.Page("pages/Questoes/Discursiva.py", title="Discursiva")
    ]
}

pg = st.navigation(pages)
pg.run()

