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

variaveis = ler_variaveis('txt/posgrad/prompts_quiz.txt')

st.title("Orientações para Podcast")
st.divider()
st.write("O podcast deve incluir um relato de experiência, uma evolução, curiosidade, ou boas práticas. Escolha o caminho que melhor se adeque à sua disciplina.")
st.code("Insira a ementa da disciplina na IA e peça vários exemplos de aplicação de prática profissional nesse conteúdo, escolha o exemplo que mais contribua com a aprendizagem do aluno e desenvolva ele.",language="None", wrap_lines=True)
st.code("Use essa mesma estrutura e peça exemplos de curiosidades relacionadas à disciplina que contribuam com sua aprendizagem em algum conteúdo.",language="None", wrap_lines=True)

st.write("Converse com a IA durante todo o processo, sempre pedindo melhorias. Você é o responsável pelos textos, ela deve apenas te auxiliar com avanços. Fique à vontade para não utilizar a IA também, trazendo sua bagagem profissional que possa contribuir e ensinar o máximo possível aos alunos.")

st.write("todos os passos são sugestões, apenas. As questões são de sua autoria e você deve cria-las de acordo com sua experiência como profissional.")

st.code("Considere que você é um <engenheiro ambiental>, especialista em <hidrologia e recursos hídricos>. Você irá elaborar um texto para gravação de podcast que foque o podcast em apenas uma das seguintes situações: Evolução: descreva uma atualização jurídica, uma mudança nos meios de produção, uma atualização de software. Nesse caso, não use a palavra “atualmente” ou derivados; utilize as datas corretas. Exemplo: “em 2020, foi implementada a Lei X após tal evento...”; ou “Eram utilizados os meios de transporte X, mas, em 1990, passaram a ser utilizados o Y”. Curiosidades: curiosidades em qualquer área do conhecimento que contribuam para o pensamento crítico do aluno. Exemplo: Batalha das correntes entre Tesla e Thomas Edison, o que pode explicar as diferenças entre corrente contínua e corrente alternada. Boas práticas: apresente processos, ferramentas, metodologias, softwares, cases etc. Dentre essas orientações, liste dez possíveis sugestões de conteúdo para esse texto. ", language="None", wrap_lines=True)

st.divider()

st.write("Aguarde a IA responder, escolha um dos itens da sua resposta.")

st.code("Use o <tema escolhido> para provocar reflexão nos alunos da disciplina de <Hidrologia Aplicada a Engenharia Ambiental>, do curso de pós-graduação em <Engenharia ambiental e sustentabilidade>, falando sobre <Qualidade da água, poluição difusa e Mudanças Climáticas>. Construa o texto, equivalente a aproximadamente 9.000 caracteres, sem espaços.", language="None", wrap_lines=True)

st.page_link("pages/Index.py", label="Home", icon="🏠")
