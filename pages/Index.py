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
        font-size: 24px;
        color: #2E2E2E;
    }
    /* Texto abaixo da seção */
    .section-text {
        font-size: 24px; /* Mesmo tamanho dos links */
        color: #2E2E2E;
        text-align: justify;
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

# Cabeçalho com logo e título
col1, col2 = st.columns([1, 8])
with col1:
    st.image("Cogna-01.png", width=400)
with col2:
    st.markdown("""<h1 class='title'>CognaIA - Prompts para Conteudistas EaD</h1>""", unsafe_allow_html=True)

st.markdown("""
    <div class='links-container'>
        <p class='main-link' style="text-align: center">Acesse o Cogna IA: 
            <a href='https://ia.tech.cogna.com.br/' target='_blank'>Clique aqui</a>
        </p>
    </div>
""", unsafe_allow_html=True)

# Seção de utilização do Cogna IA
st.markdown("<h2 class='section-header'> 📚 Como utilizar o Cogna IA? </h2>", unsafe_allow_html=True)
st.markdown("""
<div class='section-text'>
    <ul style="font-size: 16px;">
        <li>Utilize os prompts exclusivamente no Cogna IA para garantir que informações permaneçam protegidas dentro da instituição.</li>
        <li>Os prompts são sugestões baseadas em boas práticas; adapte-os conforme a necessidade da produção acadêmica.</li>
        <li>Transponha manualmente o texto gerado, ao invés de apenas copiar e colar.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

ct = st.container(border=True)

col1, col2, col3 = ct.columns(3)

with col1:
    st.subheader("Textos")
    st.page_link("pages/graduacao/Grad_Aula.py", label="Aula Textual", icon="📝")
    st.page_link("pages/graduacao/Grad_Enc.py", label="Aula Encerramento", icon="📝")

with col2:
    st.subheader("Questões")
    st.page_link("pages/Questoes/Simples.py", label="Escolha Simples", icon="❓")
    st.page_link("pages/Questoes/Complexa.py", label="Escolha Complexa", icon="❓")
    st.page_link("pages/Questoes/Assercao-Razao.py", label="Asserção-Razão", icon="❓")
    st.page_link("pages/Questoes/Incompleta.py", label="Afirmação Incompleta", icon="❓")
    st.page_link("pages/Questoes/Discursiva.py", label="Questão Discursiva", icon="❓")

with col3:
    st.subheader("Multimídia")
    st.page_link("pages/Podcast.py", label="Roteiro Podcast", icon="🎙️")

# Texto final com justificativa e estilo
st.markdown("""
<p class='section-text'>
    Os prompts acima são sugestões baseadas em boas práticas; adapte-os conforme a necessidade da sua produção acadêmica. 
    Evite a IA para sugerir <u>Referências Bibliográficas</u> devido a possibilidade de gerar fontes inexistentes (alucinações).
    Utilize como auxílio para formatar as referências ou organizar a ordem alfabética, conforme a norma que está sendo utilizada.
    <br><br>
    Para demais informações, consulte as trilhas a seguir:
</p>
""", unsafe_allow_html=True)