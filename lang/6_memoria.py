from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os
import logging

def ejecutar_con_memoria(texto, prompt, llm, memory):
    """Ejecuta el modelo conservando la memoria entre llamadas."""
    # Cargar historial previo desde la memoria
    history = memory.load_memory_variables({}).get("history", [])
    
    # Crear el chain moderno (RunnableSequence)
    chain = prompt | llm
    
    # Invocar el modelo con historial e input actual
    response = chain.invoke({"history": history, "input": texto})
    
    # Guardar el intercambio actual en la memoria
    memory.save_context({"input": texto}, {"output": response.content})
    
    # Retornar texto limpio
    return response.content.strip()

def resultado(contexto: str, input: str):
    # Silenciar logs
    os.environ["GRPC_VERBOSITY"] = "NONE"
    os.environ["GRPC_CPP_VERBOSITY"] = "NONE"
    logging.getLogger("absl").setLevel(logging.ERROR)
    logging.getLogger("grpc").setLevel(logging.ERROR)

    # Cargar variables de entorno
    load_dotenv()
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

    # Modelo
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)

    # Prompt con espacio para el historial
    prompt = ChatPromptTemplate.from_messages([
        ("system", contexto),
        ("placeholder", "{history}"),
        ("human", "{input}")
    ])

    # Crear la memoria
    memory = ConversationBufferMemory(return_messages=True)


