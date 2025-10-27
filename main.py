from PyQt5 import QtWidgets
import sys
from load.load_ventana_principal import LoadVentanaPrincipal

def main():
    app = QtWidgets.QApplication(sys.argv)
    ventana = LoadVentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()