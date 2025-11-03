from openai import OpenAI
class ModeloHistorial:
    def __init__(self):
        pass

    def modelo_historial(self, historial):
        cliente = OpenAI(api_key='')
        historial: list = [{
            "role": "system",
            "content": "Eres un asistente util y amigable"
        }]

        while True:
            pregunta = input('Tu: ')

            if pregunta.lower() == 'salir':
                break

        historial.append({"role": 'user', 'content': pregunta})


        respuesta = cliente.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=historial
        )

        respuesta_chatbot = respuesta.choices[0].message.content
        historial.append({'role': 'assistant', 'content': respuesta_chatbot})