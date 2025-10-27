from PyQt5 import QtWidgets, uic

class LoadVentanaModelosBasicos(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # Carga la interfaz grafica
        uic.loadUi('interfaces/ventana_modelos_basicos.ui', self)
        # Hacer referencia al item del menu
        self.boton_cerrar.clicked.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.close()