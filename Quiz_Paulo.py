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
            background-color:#e6ffe6;
            color:#111;
            padding:20px;
            border-radius:15px;
            box-shadow:0 0 8px #cdeccd;
            margin-bottom:20px;
        }
        .stRadio > label {
            color:#222 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 🧭 Cabeçalho
st.markdown("<div class='title'>🍎 Quiz de Conservação e Nutrição</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Responda as perguntas e veja seu desempenho!</div>", unsafe_allow_html=True)

# 🧩 Perguntas
if not st.session_state.finished:
    i = st.session_state.question_index
    q = questions[i]

    st.markdown(f"<div class='question-box'><b>Pergunta {i+1}/{len(questions)}:</b><br>{q['question']}</div>", unsafe_allow_html=True)
    resposta = st.radio("Escolha sua resposta:", q["options"], key=i)

    if st.button("Confirmar resposta", use_container_width=True):
        correct = resposta == q["correct"]
        next_question(correct)
        st.rerun()

else:
    # 🏁 Resultados
    total = len(questions)
    score = st.session_state.score
    percent = (score / total) * 100

    st.markdown("## 🎉 Resultado Final")
    st.success(f"Pontuação: **{score}/{total} ({percent:.1f}%)**")

    # Níveis
    if percent == 100:
        st.balloons()
        st.success("🏆 Expert — Excelente! Você dominou o conteúdo!")
    elif percent >= 80:
        st.success("🥇 Avançado — Parabéns! Você tem ótimo conhecimento!")
    elif percent >= 60:
        st.info("🥈 Intermediário — Bom desempenho! Continue praticando!")
    else:
        st.warning("🥉 Iniciante — Estude um pouco mais e tente novamente!")

    # ⏱ Tempos
    st.markdown("### ⏱ Tempos de resposta:")
    for i, t in enumerate(st.session_state.times, start=1):
        st.write(f"Pergunta {i}: {t:.2f} segundos")

    # 🔄 Reiniciar
    if st.button("🔄 Reiniciar quiz", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()