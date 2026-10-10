import streamlit as st

# Configuração do título da página no navegador
st.set_page_config(page_title="streamlit", page_icon="🚀")

# Criando um título principal na tela
st.title("Sei lá 🧟")

# Adicionando um subtítulo
st.subheader("Bem-vindos à aula de Streamlit!")

# Escrevendo um texto comum
st.write("Este é o nosso primeiro aplicativo web criado inteiramente em Python.")

# Uma caixa de texto informativa (visual diferente)
st.info("O Streamlit atualiza a tela automaticamente sempre que você salva o código!")



# streamlit run hello_world.py

# streamlit run hello_world.py --server.port 8080  (a porta padrão é 8501)

# Documentação do framework: https://docs.streamlit.io/develop/api-reference

# Para encontrar os emoji de forma simples: https://getemoji.com/ ou https://emojipedia.org/
