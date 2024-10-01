# Consulta de Cursos

Este projeto implementa uma aplica��o que permite aos usu�rios realizar consultas SQL em uma tabela de cursos utilizando a biblioteca Langchain para gerar as consultas a partir de perguntas em linguagem natural. A aplica��o tamb�m utiliza Gradio para fornecer uma interface web interativa.

## Depend�ncias

Para executar este projeto, voc� precisar� instalar as seguintes depend�ncias:

- **python-dotenv**: Usado para carregar vari�veis de ambiente a partir de um arquivo `.env`.
- **psycopg2**: Um adaptador PostgreSQL para Python, que permite conectar e interagir com o banco de dados PostgreSQL.
- **langchain**: Uma biblioteca que simplifica o uso de modelos de linguagem (LLMs) para v�rias tarefas.
- **langchain-community**: Um conjunto de extens�es da biblioteca Langchain que inclui implementa��es de LLMs, como o OpenAI.
- **gradio**: Uma biblioteca que facilita a cria��o de interfaces web para aplica��es de machine learning.

Voc� pode instalar as depend�ncias necess�rias usando o seguinte comando:

```bash
pip install python-dotenv psycopg2 langchain langchain-community gradio

