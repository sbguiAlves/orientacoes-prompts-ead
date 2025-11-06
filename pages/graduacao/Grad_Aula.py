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

variaveis = ler_variaveis('txt/graduacao/prompts_aula.txt')

st.title("Orientações para Template Aula")
st.divider()
st.header(":green[Videoaula: Recomendação Alta]")
st.code(variaveis["videoaula"], language="None", wrap_lines=True)

st.divider()
st.header(":green[Ponto de Partida: Recomendação Alta]")
st.code(variaveis["partida1"], language="None", wrap_lines=True)
st.code(variaveis["partida2"], language="None", wrap_lines=True)
st.code(variaveis["partida3"], language="None", wrap_lines=True)

st.divider()
st.header(":orange[Vamos Começar & Siga em Frente: Recomendação Média]")
st.code(variaveis["vc_sef"], language="None", wrap_lines=True)

st.divider()
st.header(":green[Vamos Exercitar: Recomendação Alta]")
st.code(variaveis["exercitar1"], language="None", wrap_lines=True)
st.code(variaveis["exercitar2"], language="None", wrap_lines=True)

st.divider()
st.header(":orange[Saiba Mais: Recomendação Média]")
st.code(variaveis["saiba_mais1"], language="None", wrap_lines=True)
st.code(variaveis["saiba_mais2"], language="None", wrap_lines=True)