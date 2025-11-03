class Memoria():

    def obtener_entrada(self):
        input_user = self.input_prompt.text()
        self.output_response_memoria.setText(input_user)