# 🚀 Introdução Prática ao Streamlit

Este repositório contém um projeto acadêmico desenvolvido para demonstrar os conceitos fundamentais e o uso prático da biblioteca **Streamlit** em Python. Através de exemplos progressivos, o projeto apresenta desde o "Hello World" básico até a construção de dashboards interativos e aplicações com inteligência artificial usando LLMs.

---

## 📋 Conteúdo do Projeto

O projeto é dividido em três exemplos práticos e independentes:

### 1. `hello_world.py` — Configurações Básicas e Layout
* **Objetivo:** Primeiro contato com a interface do Streamlit.
* **Conceitos demonstrados:**
  * Configuração da página (`st.set_page_config`).
  * Formatação de títulos e textos (`st.title`, `st.subheader`, `st.write`).
  * Caixas de mensagens informativas (`st.info`).

### 2. `iterative_example.py` — Dashboard e Interatividade
* **Objetivo:** Apresentar a captura de dados e a reatividade do framework.
* **Conceitos demonstrados:**
  * Organização em colunas (`st.columns`).
  * Entradas de dados (`st.text_input`, `st.number_input`, `st.slider`).
  * Visualização de dados dinâmicos com gráficos (`st.line_chart`) integrados a `pandas` e `numpy`.
  * Elementos condicionais acionados por botões (`st.button`).

### 3. `chat.py` — Chatbot Educacional com a API Groq
* **Objetivo:** Desenvolver uma aplicação completa de Chatbot streaming consumindo um modelo de linguagem (LLM).
* **Conceitos demonstrados:**
  * Gerenciamento de estado de sessão (`st.session_state`) para manter o histórico da conversa.
  * Componentes de interface de chat (`st.chat_message`, `st.chat_input`).
  * Exibição de resposta em tempo real por *streaming* (`st.write_stream`).
  * Integração com a API da **Groq** utilizando um *system prompt* didático.

---

## 🛠️ Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

### Instalação de Dependências

Instale as bibliotecas necessárias via `pip`:

```bash
pip install streamlit pandas numpy groq
```

---

## 🔑 Configuração de Chave de API (Groq)

Para executar o arquivo `chat.py`, você precisa de uma chave de API gratuita fornecida pela [Groq](https://console.groq.com/).

> ⚠️ **Aviso de Segurança:** Recomenda-se utilizar variáveis de ambiente ou o arquivo `.streamlit/secrets.toml` para armazenar suas chaves de API com segurança, evitando inseri-las diretamente no código-fonte.

Exemplo de uso com `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "sua-chave-aqui"
```

No código Python:
```python
import streamlit as st

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
```

---

## 🏃‍♂️ Como Executar os Exemplos

Navegue até a pasta do projeto no terminal e execute o arquivo desejado utilizando o comando `streamlit run`:

### 1. Executando o Hello World
```bash
streamlit run hello_world.py
```

### 2. Executando o Dashboard Interativo
```bash
streamlit run iterative_example.py
```

### 3. Executando o Chatbot Groq
```bash
streamlit run chat.py
```

Por padrão, a aplicação será aberta no navegador no endereço `http://localhost:8501`.

> 💡 **Dica:** Para alterar a porta padrão de execução, utilize o parâmetro `--server.port`:
> ```bash
> streamlit run hello_world.py --server.port 8080
> ```

---

## 📚 Links Úteis e Referências

* 📖 [Documentação Oficial do Streamlit](https://docs.streamlit.io/develop/api-reference)
* 🚀 [Conceitos Principais do Streamlit](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
* ⚡ [Documentação e API da Groq](https://console.groq.com/docs/quickstart)
* 😃 [Tabela de Emojis para Streamlit](https://getemoji.com/)