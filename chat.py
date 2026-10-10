import streamlit as st
from groq import Groq

# ------------------------------------------------------------------------------
# 1. Configurações: Cole sua chave ativa aqui
# ------------------------------------------------------------------------------
GROQ_API_KEY = "EntreComSuaChaveDaAPI"

# Modelo compatível com o endpoint da Groq
MODEL_NAME = "openai/gpt-oss-20b"

st.title("💬 Chatbot Groq")

# Inicializa o cliente com a chave direta em string
client = Groq(api_key=GROQ_API_KEY.strip())

# ------------------------------------------------------------------------------
# 2. Histórico de Mensagens
# ------------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens acumuladas no chat
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Gerador para processar as palavras transmitidas em tempo real
def stream_groq_response(stream):
    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            yield content

# ------------------------------------------------------------------------------
# 3. Interação do Usuário
# ------------------------------------------------------------------------------
if prompt := st.chat_input("Digite sua mensagem..."):
    # Exibe e armazena o prompt do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Define o contexto do modelo
    system_prompt = (
        "Você é um tutor educacional paciente e amigável. "
        "O usuário com quem você está falando é um aluno iniciante. "
        "Explique os conceitos de forma didática, simples, com exemplos práticos "
        "e evite termos técnicos complexos sem antes explicá-los."
        "a resposta deve ser dada em um único paragrafo."
    )

    # Constrói o histórico enviando a mensagem 'system' em primeiro lugar
    api_messages = [{"role": "system", "content": system_prompt}] + [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    # Gera e escreve a resposta
    with st.chat_message("assistant"):
        try:
            stream = client.chat.completions.create(
                model=MODEL_NAME,
                messages=api_messages,
                stream=True,
            )
            response = st.write_stream(stream_groq_response(stream))
            st.session_state.messages.append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Erro na chamada da API: {e}")
            
