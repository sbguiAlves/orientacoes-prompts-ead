import streamlit as st

def ler_variaveis(nome_arquivo):
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


def criar_botao(texto, tipo_botao, variaveis, container, chave_variavel):
    if st.button(texto, use_container_width=True, type=tipo_botao):
        container.code(variaveis.get(chave_variavel, "Código não encontrado"), language="None", wrap_lines=True)


def taxonomia_bloom(variaveis, container):
    criar_botao("Compreensão", "secondary", variaveis, container, "tax_compreensao")
    criar_botao("Aplicação", "secondary", variaveis, container, "tax_aplicacao")
    criar_botao("Análise", "secondary", variaveis, container, "tax_analise")
    criar_botao("Avaliação", "secondary", variaveis, container, "tax_avaliacao")

def tipo_discursiva(variaveis, container):
    criar_botao("Problema Matemático", "secondary", variaveis, container, "tipomatemático")
    criar_botao("Conceitual", "secondary", variaveis, container, "tipoconceitual")
    criar_botao("Processual Sistêmica", "secondary", variaveis, container, "tipoprocessual")
    criar_botao("Redação Livre", "secondary", variaveis, container, "tiporedação")
    criar_botao("Julgamento de Veracidade", "secondary", variaveis, container, "tipojulgamento")
    criar_botao("Análise de Valor de Procedimentos", "secondary", variaveis, container, "tipoprocedimental")
    criar_botao("Posicionamento Crítico à Conduta", "secondary", variaveis, container, "tipoposicionamento")

# Inicializa o session state
if 'tipo_discursiva' not in st.session_state:
    st.session_state.tipo_selecionado = None
if 'taxonomia_selecionada' not in st.session_state:
    st.session_state.taxonomia_selecionada = None

variaveis = ler_variaveis('txt/questoes/prompts_questoes_discursiva.txt')

st.title("Questão Discursiva")
st.divider()
st.markdown("""<h3 style="color: #5219A1">1º Prompt: Contextualize!</h3>""", unsafe_allow_html=True)
st.code(variaveis["intro_discursiva"], language="None", wrap_lines=True)

st.markdown("""<h3 style="color: #5219A1">2º Prompt: Especifique pela Taxonomia de Bloom!</h3>""", unsafe_allow_html=True)
container_bloom = st.container(border=True)

st.markdown("""<h3 style="color: #5219A1">3º Prompt: Especifique e Exemplifique pelo Tipo da Questão!</h3>""", unsafe_allow_html=True)
container_tipo = st.container(border=True)

with container_bloom:
    taxonomia_bloom(variaveis, container_bloom)

with container_tipo:
    tipo_discursiva(variaveis, container_tipo)

# Exibe as opções selecionadas
if st.session_state.tipo_selecionado:
    st.code(variaveis.get(st.session_state.tipo_discursiva, "Código não encontrado"), language="None", wrap_lines=True)
if st.session_state.taxonomia_selecionada:
    st.code(variaveis.get(st.session_state.taxonomia_selecionada, "Código não encontrado"), language="None",
            wrap_lines=True)