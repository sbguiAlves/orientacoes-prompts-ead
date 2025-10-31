import streamlit as st

# Estilos CSS personalizados
st.markdown("""
<style>
    /* Centralizar o título */
    .title {
        text-align: left;
        color: #2E2E2E;
        margin-left: 50px; /* Espaço entre o logo e o título */
    }
    /* Estilizar os links principais */
    .main-link {
        font-size: 20px;
        color: #2E2E2E;
    }
    /* Centralizar os links */
    .links-container {
        text-align: center;
    }
    /* Texto abaixo da seção */
    .section-text {
        font-size: 20px; /* Mesmo tamanho dos links */
        color: #2E2E2E;
    }
    /* Ajuste da imagem do logo */
    .logo {
        width: 200px;
    }
    /* Estilização dos botões */
    .stButton>button {
        background-color: #D8BFD8; /* Lilás claro */
        color: black;
    }
    .stButton>button:hover {
        background-color: #D3D3D3; /* Cinza */
        color: black;
    }
    /* Remove o outline do botão quando clicado */
    .stButton>button:focus:not(:focus-visible) {
        outline: none;
    }
    /* Estilo dos títulos da seção */
    .section-header {
        color: #2E2E2E;
        font-size: 28px; /* Aumenta o tamanho do título */
    }
    /* Espaçamento entre os elementos */
    .spacer {
        margin-top: 10px; /* Diminui o espaço entre os elementos */
    }
    /* Ajusta a distância entre os links e a seção */
    .link-spacer {
        margin-bottom: 5px;
        margin-top: -5px;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho com logo à esquerda e título
col1, col2 = st.columns([1, 8])
with col1:
    st.image("Cogna-01.png", width=200)
with col2:
    st.markdown(""" <h1 class='title'>CognaIA - Prompts para Conteudistas EaD</h1>""", unsafe_allow_html=True)

st.markdown(""" <div class='links-container'> <p class='main-link'>Acesse o Cogna IA: <a href='https://ia.tech.cogna.com.br/' target='_blank'>Clique aqui</a></p> </div> """, unsafe_allow_html=True)


# Seção: Prompts de Utilização Cogna IA
st.markdown("<h2 class='section-header'> 📚 Como utilizar? </h2>", unsafe_allow_html=True)
st.markdown("<p class='section-text'>Clique na atividade, copie o texto, cole no Cogna IA e faça as alterações necessárias.</p>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
# Coluna 1
with col1:
    st.subheader("Textos")
    st.page_link("pages/graduacao/Grad_Aula.py", label="Aula Textual", icon="🏠")
    st.page_link("pages/graduacao/Grad_Enc.py", label="Aula Encerramento", icon="🏠")

# Coluna 2
with col2:
   st.subheader("Questões")
   st.page_link("pages/Questoes/Simples.py", label="Múltipla Escolha", icon="🏠")
   #st.page_link("pages/graduacao/Grad_Questoes.py", label="Discursiva", icon="🏠")

# Coluna 3
with col3:
    st.subheader("Multimídia")
    # st.page_link("pages/Podcast.py", label="Roteiro Podcast", icon="🏠")