import streamlit as st

variaveis = {}

def ler_variaveis(nome_arquivo):
    """Lê as variáveis de um arquivo de texto."""
    variaveis = {}
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if linha.startswith("#") or not linha:  # Ignora comentários e linhas em branco
                    continue
                if ":" in linha:
                    partes = linha.split(":", 1)  # Divide a linha em no máximo 2 partes
                    chave = partes[0]
                    valor = partes[1] if len(partes) > 1 else ""  # Valor vazio se não houver segundo valor
                    variaveis[chave] = valor
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {nome_arquivo}")
    return variaveis

variaveis = ler_variaveis('txt/ptc/prompts_encerramento.txt')

st.title("Orientações para Template Encerramento")
st.divider()
st.header(":green[Videoaula: Recomendação Alta]")
st.code(variaveis["videoaula"], language="None", wrap_lines=True)

st.divider()
st.header(":green[Ponto de Chegada: Recomendação Alta]")
st.code(variaveis["chegada1"], language="None", wrap_lines=True)
st.code(variaveis["chegada2"], language="None", wrap_lines=True)

st.divider()
st.header(":orange[É Hora de Praticar: Recomendação Média]")
st.code(variaveis["praticar1"], language="None", wrap_lines=True)
st.code(variaveis["praticar2"], language="None", wrap_lines=True)

st.divider()
st.header(":green[Dê o Play: Recomendação Alta]")
st.code(variaveis["play1"], language="None", wrap_lines=True)
st.code(variaveis["play2"], language="None", wrap_lines=True)

st.divider()
st.header(":orange[Assimile: Recomendação Média]")
st.code(variaveis["assimile1"], language="None", wrap_lines=True)
st.code(variaveis["assimile2"], language="None", wrap_lines=True)

st.markdown("""
<p>O Cogna IA não produz mapas mentais, infográficos, tirinhas, linhas do tempo, etc. Utilize outras ferramentas para criar o objeto, como:</p>
<ul>
    <li><a href="https://www.napkin.ai/" target="_blank">Napkin: Esquemas visuais a partir de um texto.</a></li>
    <li><a href="https://www.canva.com/" target="_blank">Canva: Kit de criação visual. </a></li>
    <li><a href="https://claude.ai/" target="_blank">Claude: Criação de esquemas visuais via HTML</a></li>
</ul>
""", unsafe_allow_html=True)
