# Примеры агентов GigaChain для Streamlit

В этом разделе вы найдете примеры агентов GigaChain для работы со Streamlit.

Streamlit — библиотека, ускоряющая разработку веб-приложений работающих с большими языковыми моделями (LLM).

Пример веб-приложения с чат-ботом на основе GigaChat:

<iframe loading="lazy" src="https://gigachat-streaming.streamlit.app/?embed=true&embed_options=light_theme"
    style={{ width: 100 + '%', border: 'none', marginBottom: 1 + 'rem', height: 600 }}
    allow="camera;clipboard-read;clipboard-write;"
></iframe>

## Установка

Для установки Streamlit используйте команду:

```sh
pip install langchain streamlit
```

Подробную инструкцию по работе с библиотекой ищите в [официальной документации.](https://docs.streamlit.io/library/get-started)

## Список примеров

В настоящий момент доступен только один пример — [Чат-бот на базе GigaChat с потоковой генерацией и разными видами авторизации](./gigachat_streaming.py).

> [!NOTE]
> Список примеров будет пополняться.

<!--
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/langchain-ai/streamlit-agent?quickstart=1)

This repository contains reference implementations of various LangChain agents as Streamlit apps including:

- `basic_streaming.py`: Simple streaming app with `langchain.chat_models.ChatOpenAI` ([View the app](https://langchain-streaming-example.streamlit.app/))
- `basic_memory.py`: Simple app using `StreamlitChatMessageHistory` for LLM conversation memory ([View the app](https://langchain-st-memory.streamlit.app/))
- `mrkl_demo.py`: An agent that replicates the [MRKL demo](https://python.langchain.com/docs/modules/agents/how_to/mrkl) ([View the app](https://langchain-mrkl.streamlit.app))
- `minimal_agent.py`: A minimal agent with search (requires setting `OPENAI_API_KEY` env to run)
- `search_and_chat.py`: A search-enabled chatbot that remembers chat history ([View the app](https://langchain-chat-search.streamlit.app/))
- `simple_feedback.py`: A chat app that allows the user to add feedback on responses using [streamlit-feedback](https://github.com/trubrics/streamlit-feedback), and link to the traces in [LangSmith](https://docs.smith.langchain.com/) ([View the app](https://langsmith-simple-feedback.streamlit.app/))
- `chat_with_documents.py`: Chatbot capable of answering queries by referring custom documents ([View the app](https://langchain-document-chat.streamlit.app/))
- `chat_with_sql_db.py`: Chatbot which can communicate with your database ([View the app](https://langchain-chat-sql.streamlit.app/))
- `chat_pandas_df.py`: Chatbot to ask questions about a pandas DF (Note: uses `PythonAstREPLTool` which is vulnerable to arbitrary code execution,
  see [langchain #7700](https://github.com/langchain-ai/langchain/issues/7700))

Apps feature LangChain 🤝 Streamlit integrations such as the
[Callback integration](https://python.langchain.com/docs/modules/callbacks/integrations/streamlit) and
[StreamlitChatMessageHistory](https://python.langchain.com/docs/integrations/memory/streamlit_chat_message_history).

## More great app examples

Check out some other full examples of apps that utilize LangChain + Streamlit:

- [Auto-graph](https://auto-graph.streamlit.app/) - Build knowledge graphs from user-input text ([Source code](https://github.com/langchain-ai/langchain-benchmarks/blob/main/extraction/streamlit_app.py))
- [Web Explorer](https://web-explorer.streamlit.app/) - Retrieve and summarize insights from the web ([Source code](https://github.com/langchain-ai/web-explorer))
- [LangChain Teacher](https://lang-teacher.streamlit.app/) - Learn LangChain from an LLM tutor ([Source code](https://github.com/langchain-ai/langchain-teacher))
- [Text Splitter Playground](https://langchain-text-splitter.streamlit.app/) - Play with various types of text splitting for RAG ([Source code](https://github.com/langchain-ai/text-split-explorer))
- [Tweet Generator](https://elon-twitter-clone.streamlit.app/) - Fine tune GPT-3.5 on tweets ([Source code](https://github.com/langchain-ai/twitter-finetune))

## Setup

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```shell
# Create Python environment
$ poetry install

# Install git pre-commit hooks
$ poetry shell
$ pre-commit install
```

## Running

```shell
# Run mrkl_demo.py or another app the same way
$ streamlit run streamlit_agent/mrkl_demo.py
```

# Running with Docker

This project includes `Dockerfile` to run the app in Docker container. In order to optimise the Docker Image is optimised for size and building time with cache techniques.

To generate Image with `DOCKER_BUILDKIT`, follow below command

```DOCKER_BUILDKIT=1 docker build --target=runtime . -t langchain-streamlit-agent:latest```

1. Run the docker container directly

``docker run -d --name langchain-streamlit-agent -p 8051:8051 langchain-streamlit-agent:latest ``

2. Run the docker container using docker-compose (Recommended)

Edit the Command in `docker-compose` with target streamlit app

``docker-compose up``

## Contributing

We plan to add more agent and chain examples over time and improve the existing ones - PRs welcome! 🚀
-->