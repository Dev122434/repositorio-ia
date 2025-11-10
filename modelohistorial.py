from groq import Groq

class ModeloHistorial:
    def __init__(self):
        pass

    def modeloHistorial(self, historial):
        cliente = Groq(api_key='')
        
        # Inicializar el historial del sistema
        historial = [{"role": "system", "content": "Eres un asistente útil y amigable."}]
        
        print("Chat iniciado. Escribe 'salir' para terminar.\n")
        while True:
            pregunta = input("Tú: ")
            
            if pregunta.lower() == 'salir':
                print("Chat terminado.")
                break
            # Agregar la pregunta del usuario al historial
            historial.append({"role": "user", "content": pregunta})
            
            # llamada al API de Groq
            respuesta = cliente.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=historial  # Aquí se envía el historial completo
            )
            # Obtener la respuesta del chatbot
            respuesta_chatbot = respuesta.choices[0].message.content
            print("Chatbot:" + respuesta_chatbot + "\n")
            # Agregar la respuesta del chatbot al historial
            historial.append({"role": "assistant", "content": respuesta_chatbot})


