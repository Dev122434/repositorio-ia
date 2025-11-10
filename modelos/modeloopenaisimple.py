from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv

class ModeloOpenAI:
    def __init__(self):
        pass

    def modeloSimple(self, pregunta):
        #cliente = Groq(api_key='')
        #respuesta = cliente.chat.completions.create(
            #model="llama-3.1-8b-instant",
            #messages=[{
                #"role": "user","content": pregunta}
        #    ]
        #)
        #return respuesta.choices[0].message.content

        cliente = OpenAI(api_key='')
        respuesta = cliente.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{
                "role": "user", "content": pregunta
            }]
        )
        return respuesta.choices[0].message.content
