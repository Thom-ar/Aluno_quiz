# quiz_app.py
import streamlit as st
import time

st.set_page_config(page_title="Quiz de Conservação e Nutrição", page_icon="🎯", layout="centered")

st.markdown("""
    <h1 style='text-align:center; color:#2E8B57;'>🎯 Quiz sobre Tecnologias de Conservação de Alimentos e Nutrição para Diabéticos</h1>
    <p style='text-align:center; color:gray;'>Responda as perguntas abaixo e veja seu desempenho!</p>
""", unsafe_allow_html=True)

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

score = 0

for i, q in enumerate(questions, start=1):
    st.markdown(f"### 🧩 Pergunta {i}: {q['question']}")
    resposta = st.radio("Escolha sua resposta:", q["options"], key=i)
    if st.button(f"Confirmar resposta {i}"):
        if resposta == q["correct"]:
            st.success("✅ Correto!")
            score += 1
        else:
            st.error(f"❌ Incorreto! A resposta certa é: {q['correct']}")
        time.sleep(1)

if st.button("Ver resultado final"):
    total = len(questions)
    percent = (score / total) * 100
    st.markdown("---")
    st.markdown(f"## 🏁 Pontuação final: **{score}/{total} ({percent:.1f}%)**")

    if percent == 100:
        st.success("🏆 Expert – Excelente! Você dominou o conteúdo!")
    elif percent >= 80:
        st.success("🥇 Avançado – Parabéns! Você tem ótimo conhecimento!")
    elif percent >= 60:
        st.info("🥈 Intermediário – Bom desempenho! Continue praticando!")
    else:
        st.warning("🥉 Iniciante – Estude um pouco mais e tente novamente!")

