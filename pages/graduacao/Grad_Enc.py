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

variaveis = ler_variaveis('txt/graduacao/prompts_encerramento.txt')

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
st.write(":red[Atenção!] O Cogna IA não produz mapas mentais, infográficos, tirinhas, linhas do tempo, etc. Utilize outras ferramentas para criar o objeto.")


st.divider()
st.header(":red[Referências: Recomendação Nula]")
st.write("Devido às :blue[alucinações], a IA pode referenciar materiais que não existem na Internet ou na Biblioteca Virtual. Além disso, a ferramenta não possui conhecimento atualizado sobre as normas ABNT.")

st.page_link("Index.py", label="Home", icon="🏠")
