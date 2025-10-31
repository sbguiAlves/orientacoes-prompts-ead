import streamlit as st

pages = {
    "Introdução":
        [
            st.Page("pages/Index.py", title="Menu Principal")
        ],
    "Prompts para Graduação": [
        st.Page("pages/graduacao/Grad_Aula.py", title="Template Aula", icon="1️⃣"),
        st.Page("pages/graduacao/Grad_Enc.py", title="Template Encerramento", icon="2️⃣"),
        st.Page("pages/graduacao/Grad_Questoes.py", title="Questões", icon="3️⃣")
    ],
    "Prompts para Pós-Graduação": [
        st.Page("pages/posgrad/Posgrad_podcast.py", title="Podcast", icon="🔈"),
        st.Page("pages/posgrad/Posgrad_questoes.py", title="Questões", icon="2️⃣"),
        st.Page("pages/posgrad/Posgrad_quiz.py", title="Quiz", icon="3️⃣")
    ]
}

pg = st.navigation(pages)
pg.run()

