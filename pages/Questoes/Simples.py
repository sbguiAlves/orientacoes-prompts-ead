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
    """Cria os botões para a taxonomia de Bloom."""
    criar_botao("Compreensão", "secondary", variaveis, container, "taxonomia_compreensao")
    criar_botao("Aplicação", "secondary", variaveis, container, "taxonomia_aplicacao")
    criar_botao("Análise", "secondary", variaveis, container, "taxonomia_analise")
    criar_botao("Avaliação", "secondary", variaveis, container, "taxonomia_avaliacao")


# Inicializa o session state
if 'tipo_selecionado' not in st.session_state:
    st.session_state.tipo_selecionado = None
if 'taxonomia_selecionada' not in st.session_state:
    st.session_state.taxonomia_selecionada = None

variaveis = ler_variaveis('txt/questoes/prompts_questoes.txt')

st.title("Prompts para Múltipla Escolha Simples")
st.divider()
st.markdown("""
<p class='section-text'> Utilize o primeiro prompt a seguir para contextualizar a IA:</p>""", unsafe_allow_html=True)
st.code(variaveis["intro_simples"], language="None", wrap_lines=True)

container_bloom = st.container(border=True)

with container_bloom:
    container_bloom.write("Escolha o Taxonomia de Bloom:")
    taxonomia_bloom(variaveis, container_bloom)

st.divider()

# Exibe as opções selecionadas
if st.session_state.tipo_selecionado:
    st.code(variaveis.get(st.session_state.tipo_selecionado, "Código não encontrado"), language="None", wrap_lines=True)
if st.session_state.taxonomia_selecionada:
    st.code(variaveis.get(st.session_state.taxonomia_selecionada, "Código não encontrado"), language="None",
            wrap_lines=True)
