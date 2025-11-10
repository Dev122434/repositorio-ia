from openai import OpenAI
class ModeloHistorial:
    def __init__(self):
        pass

    def modelo_historial(self, historial, pregunta):
        cliente = OpenAI(api_key='')
        historial: list = [{
            "role": "system",
            "content": "Eres un asistente util y amigable"
        }]

        historial.append({"role": 'user', 'content': pregunta})


        respuesta = cliente.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=historial
        )

        respuesta_chatbot = respuesta.choices[0].message.content
        historial.append({'role': 'assistant', 'content': respuesta_chatbot})