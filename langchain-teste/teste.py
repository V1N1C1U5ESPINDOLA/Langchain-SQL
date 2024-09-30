from dotenv import load_dotenv
import os
import psycopg2
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import gradio as gr

load_dotenv()
key = os.getenv("OPENAI_API_KEY")

def consulta_cursos(pergunta_usuario):
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
        
        cursor = conn.cursor()

        prompt_template = PromptTemplate(
            input_variables=["input_text"],
            template="Crie uma consulta SQL sabendo da existencia da tabela cursos com colunas nome_curso, nota_corte e instituto para a seguinte pergunta: {input_text}"
        )

        llm = OpenAI(api_key=key)
        chain = LLMChain(llm=llm, prompt=prompt_template)

        consulta_sql = chain.run(input_text=pergunta_usuario)

        if "SELECT" not in consulta_sql.upper():
            return "Consulta SQL gerada invalida."

        cursor.execute(consulta_sql)
        resultados = cursor.fetchall()
        
        output = "\n".join(" - ".join(map(str, resultado)) for resultado in resultados)
        
        return output if output else "Nenhum resultado encontrado."

    except Exception as e:
        return f"Ocorreu um erro ;-; -> {e}"

    finally:
        cursor.close()
        conn.close()

iface = gr.Interface(
    fn=consulta_cursos,
    inputs="text",
    outputs="text",
    title="Consulta de Cursos",
    description="Digite sua pergunta acerca dos cursos da UFG:"
)

if __name__ == "__main__":
    iface.launch()
