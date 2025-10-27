from PyQt5 import QtWidgets, uic

class LoadVentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Carga la interfaz grafica
        uic.loadUi('interfaces/ventana_principal.ui', self)
        # Maximizar la ventana
        self.showMaximized()
        # Hacer referencia al item del menu
        self.actionSalir.triggered.connect(self.cerrarVentana)

    def cerrarVentana(self):
        self.close()