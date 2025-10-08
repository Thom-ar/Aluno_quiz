# -- coding: utf-8 --
import streamlit as st
import time

# 🎯 Configurações da página
st.set_page_config(
    page_title="Quiz de Conservação e Nutrição",
    page_icon="🍎",
    layout="centered"
)

# 🧠 Dados do quiz
questions = [
    {
        "question": "Qual é a principal função da refrigeração na conservação dos alimentos?",
        "options": [
            "Alterar o sabor dos alimentos",
            "Reduzir a atividade microbiana e enzimática",
            "Eliminar totalmente os microrganismos",
            "Aumentar valor nutricional"
        ],
        "correct": "Reduzir a atividade microbiana e enzimática"
    },
    {
        "question": "Qual das tecnologias abaixo é considerada uma forma moderna de conservação de alimentos?",
        "options": ["Defumação", "Irradiação de alimentos", "Salga", "Fermentação natural"],
        "correct": "Irradiação de alimentos"
    },
    {
        "question": "Qual é o principal objetivo da embalagem em atmosfera modificada (MAP)?",
        "options": [
            "Melhorar apenas a aparência dos alimentos",
            "Substituir totalmente a refrigeração",
            "Alterar gases da embalagem para prolongar a vida útil",
            "Adicionar conservantes químicos"
        ],
        "correct": "Alterar gases da embalagem para prolongar a vida útil"
    },
    {
        "question": "Quais são alguns dos principais benefícios proporcionados pelas tecnologias de conservação de alimentos?",
        "options": [
            "Reduzir desperdícios e prolongar a vida útil",
            "Garantir maior segurança alimentar",
            "Facilitar transporte e distribuição",
            "Todas as alternativas estão corretas"
        ],
        "correct": "Todas as alternativas estão corretas"
    },
    {
        "question": "Qual é o principal nutriente que deve ser controlado na alimentação de pessoas com diabetes?",
        "options": ["Proteínas", "Gorduras", "Carboidratos", "Fibras"],
        "correct": "Carboidratos"
    },
    {
        "question": "Qual dessas opções é mais adequada para um lanche saudável para um diabético?",
        "options": [
            "Refrigerante diet e bolacha",
            "Suco natural e pão branco",
            "Iogurte natural e frutas frescas",
            "Batata frita e suco industrializado"
        ],
        "correct": "Iogurte natural e frutas frescas"
    }
]

# 🧩 Estado da sessão
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "times" not in st.session_state:
    st.session_state.times = []
if "finished" not in st.session_state:
    st.session_state.finished = False

# 🚀 Função para avançar
def next_question(correct):
    elapsed = time.time() - st.session_state.start_time
    st.session_state.times.append(round(elapsed, 2))
    st.session_state.start_time = time.time()

    if correct:
        st.session_state.score += 1
    st.session_state.question_index += 1

    if st.session_state.question_index >= len(questions):
        st.session_state.finished = True

# 🎨 Estilo visual com alto contraste
st.markdown("""
    <style>
        .title {
            text-align:center;
            color:#2E8B57;
            font-size:32px;
            font-weight:bold;
            margin-bottom:10px;
        }
        .subtitle {
            text-align:center;
            color:#555;
            margin-bottom:30px;
        }
        .question-box {
            background-color:#e6