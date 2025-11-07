from PyQt5 import QtWidgets, uic

from load.load_ventana_modelos_basicos import LoadVentanaModelosBasicos
from load.load_ventana_modelos_langchain import LoadVentanaLangchain

class LoadVentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga la interfaz grafica
        uic.loadUi("interfaces/ventana_principal.ui", self)
        # Maximizar la ventana
        self.showMaximized()
        # Hacer referencia al item del menu
        self.actionBasicos.triggered.connect(self.abrirVentanaBasicos)
        self.actionLangChain.triggered.connect(self.abrirVentanaLangchain)
        self.actionSalir.triggered.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.close()

    def abrirVentanaBasicos(self):
        self.basicos = LoadVentanaModelosBasicos()
        self.basicos.exec_()

    def abrirVentanaLangchain(self):
        self.lang_chain = LoadVentanaLangchain()
        self.lang_chain.exec_()