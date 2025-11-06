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
    criar_botao("Compreensão", "secondary", variaveis, container, "tax_compreensao")
    criar_botao("Aplicação", "secondary", variaveis, container, "tax_aplicacao")
    criar_botao("Análise", "secondary", variaveis, container, "tax_analise")
    criar_botao("Avaliação", "secondary", variaveis, container, "tax_avaliacao")


# Inicializa o session state
if 'tipo_selecionado' not in st.session_state:
    st.session_state.tipo_selecionado = None
if 'taxonomia_selecionada' not in st.session_state:
    st.session_state.taxonomia_selecionada = None

variaveis = ler_variaveis('txt/questoes/prompts_questoes.txt')

st.title("Múltipla Escolha Simples")
st.divider()
st.markdown("""
<p class='section-text'> Utilize o primeiro prompt a seguir para contextualizar a IA:</p>""", unsafe_allow_html=True)
st.code(variaveis["intro_simples"], language="None", wrap_lines=True)
st.markdown("""<p>Para adequar o enunciado diante da instrução/ordem a ser abordada, selecione uma da Taxonomia a seguir</p>""")

container_bloom = st.container(border=True)

with container_bloom:
    taxonomia_bloom(variaveis, container_bloom)

st.markdown("""<p>Caso queira adequar a questão para a estrutura padrão recomendada, utilize o prompt a seguir como exemplificação: </p>""")
st.code("""\"TEXTO-BASE: Devido à composição, os microfones dinâmicos apresentam maior robustez e resistência a altos volumes e são recomendados para situações com muita movimentação ou presença de ruídos indesejados. Em contrapartida, os microfones condensadores são mais sensíveis, possuindo diafragmas leves capazes de captar detalhes muito sutis. 

ENUNCIADO: Considerando os critérios de robustez e sensibilidade dos microfones na escolha do equipamento ideal, para gravar diálogos em estúdio deve-se usar 

ALTERNATIVAS:
A. um microfone dinâmico, pois oferece maior segurança estrutural em ambiente de captação. 
B. um microfone condensador, pois a necessidade de alimentação de corrente contínua estabiliza o circuito em ambientes externos ruidosos. 
C. um microfone dinâmico, enquanto a sensibilidade do condensador deve ser reservada para captar sons ambientes abertos. 
D. um microfone condensador para a dublagem da voz principal e um microfone dinâmico para gravação de esforços físicos. 
E. um microfone omnidirecional em todas as situações, independentemente do tipo para garantir que a direcionalidade não atenue sons relevantes. 

RESOLUÇÃO COMENTADA
Alternativa Correta: “um microfone condensador para a dublagem da voz principal e um microfone dinâmico para gravação de esforços físicos”. Para a dublagem da voz principal em estúdio, um ambiente controlado onde se deseja a máxima riqueza de detalhes, o microfone condensador é a escolha ideal devido à sua alta sensibilidade. Para gravar socos e quedas intensas (efeitos de esforço físico), que envolvem altos volumes e possível movimentação, a maior robustez e resistência a volumes altos do microfone dinâmico o tornam o equipamento mais adequado. 

um microfone dinâmico, pois oferece maior segurança estrutural em ambiente de captação. INCORRETA. Em um estúdio, a prioridade é a riqueza de detalhes e a captação de sutilezas. O microfone condensador é o equipamento projetado para esse fim, e não o dinâmico. Embora o dinâmico seja mais robusto, a robustez é menos crítica do que a sensibilidade em um ambiente isolado. 

um microfone condensador, pois a necessidade de alimentação de corrente contínua estabiliza o circuito em ambientes externos ruidosos. INCORRETA. A necessidade de alimentação elétrica de corrente contínua é um requisito técnico para o funcionamento por capacitância do condensador, mas isso não o torna mais estável ou robusto em ambientes ruidosos ou com altos volumes. Na verdade, os dinâmicos são os recomendados para situações com ruído intenso. 

um microfone dinâmico, enquanto a sensibilidade do condensador deve ser reservada para captar sons ambientes abertos. INCORRETA. Estúdios de gravação fornecem isolamento e controle de reverberação precisamente para permitir o uso de microfones sensíveis (condensadores) na captação de detalhes. Reservar o condensador para ambientes abertos e o dinâmico (menos sensível) para o estúdio anula o propósito de se usar um ambiente controlado para gravações de alta fidelidade como narrações e dublagens. 

um microfone omnidirecional em todas as situações, independentemente do tipo para garantir que a direcionalidade não atenue sons relevantes. INCORRETA. Embora a direcionalidade seja um fator relevante, em muitas situações (como gravação de diálogo isolado), é crucial usar microfones direcionais para atenuar ruídos indesejados. Além disso, a direcionalidade não é o critério que define a escolha primária entre robustez (dinâmico) ou sensibilidade (condensador).\" 
            """, language="None", wrap_lines=True)

# Exibe as opções selecionadas
if st.session_state.tipo_selecionado:
    st.code(variaveis.get(st.session_state.tipo_selecionado, "Código não encontrado"), language="None", wrap_lines=True)
if st.session_state.taxonomia_selecionada:
    st.code(variaveis.get(st.session_state.taxonomia_selecionada, "Código não encontrado"), language="None",
            wrap_lines=True)
