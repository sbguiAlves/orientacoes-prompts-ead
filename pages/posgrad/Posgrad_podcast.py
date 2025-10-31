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
variaveis = ler_variaveis('txt/posgrad/prompts_podcast.txt')

st.title("Orientações para Podcast")
st.divider()
st.write("O podcast deve incluir um relato de experiência, uma evolução, curiosidade, ou boas práticas. Escolha o caminho que melhor se adeque à sua disciplina.")
st.code(variaveis["podcast1"],language="None", wrap_lines=True)
st.code(variaveis["podcast2"],language="None", wrap_lines=True)

st.write("Converse com a IA durante todo o processo, sempre pedindo melhorias. Você é o responsável pelos textos, ela deve apenas te auxiliar com avanços. Fique à vontade para não utilizar a IA também, trazendo sua bagagem profissional que possa contribuir e ensinar o máximo possível aos alunos.")

st.write("Todos os passos são sugestões, apenas. As questões são de sua autoria e você deve cria-las de acordo com sua experiência como profissional.")

st.code(variaveis["podcast3"],language="None", wrap_lines=True)

st.divider()

st.write("Aguarde a IA responder, escolha um dos itens da sua resposta.")

st.code(variaveis["podcast4"],language="None", wrap_lines=True)

st.page_link("pages/Index.py", label="Home", icon="🏠")
