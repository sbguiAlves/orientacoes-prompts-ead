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

variaveis = ler_variaveis('txt/prompts_podcast.txt')

st.title("Orientações para Podcast")
st.divider()
st.markdown("""<h3 style="color: #5219A1">1º Prompt: Contextualize!</h3>
<p>O podcast partir de uma contextualização que inclua um relato de experiência, uma evolução, curiosidade, ou boas práticas.
 Escolha o caminho que melhor se adeque à sua disciplina.</p>""", unsafe_allow_html=True)
st.code(variaveis["intropodcast"],language="None", wrap_lines=True)

st.markdown("""<h3 style="color: #5219A1">2º Prompt: Especifique!</h3>""", unsafe_allow_html=True)
st.code(variaveis["meiopodcast"],language="None", wrap_lines=True)

st.markdown("""<h3 style="color: #5219A1">3º Prompt: Restrinja!</h3>""", unsafe_allow_html=True)
st.code(variaveis["fimpodcast"],language="None", wrap_lines=True)