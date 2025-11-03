from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QPropertyAnimation

class LoadVentanaModelosBasicos(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        # Carga la interfaz grafica
        uic.loadUi('interfaces/ventana_modelos_basicos.ui', self)
        # Configurar contenedores
        # Eliminar barra y de titulo - opacidad
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)

        # Cerrar la ventana
        self.boton_cerrar.clicked.connect(lambda: self.close())

        # Mover la ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana

        # Menu lateral
        self.boton_menu.clicked.connect(self.mover_menu)

        #Botones para cambiar de página
        self.boton_prompt.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_prompt))
        self.boton_memoria.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_memoria))
        self.boton_chat.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_chat))

    # 6.- mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        if self.isMaximized() == False:			
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)
                self.clickPosition = event.globalPos()
                event.accept()

        if event.globalPos().y() <=20:
            self.showMaximized()
        else:
            self.showNormal()

    #7.- Mover menú
    def mover_menu(self):
        if True:			
            width = self.frame_lateral.width()
            widthb = self.boton_menu.width()
            normal = 0
            if width==0:
                extender = 200
                self.boton_menu.setText("Menú")
            else:
                extender = normal
                self.boton_menu.setText("")
            
            self.animacion = QPropertyAnimation(self.frame_lateral, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()
        
            self.animacionb = QPropertyAnimation(self.boton_menu, b'minimumWidth')
    
            self.animacionb.setStartValue(width)
            self.animacionb.setEndValue(extender)
            self.animacionb.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacionb.start()