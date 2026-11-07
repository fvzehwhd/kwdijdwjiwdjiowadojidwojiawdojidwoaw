from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from random import randint




app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Rufier")
main_win.resize(400, 200)
ventana2 = QWidget()
ventana2.setWindowTitle("Pagina 2")
ventana2.resize(400, 200)
ventana3 = QWidget()
ventana3.setWindowTitle("Pagina 3")
ventana3.resize(400, 200)

but1 = QPushButton("Siguiente Pagina")
but2 = QPushButton("Comenzar la primera prueba")
but3 = QPushButton("Comenzar a hacer sentadillas")
but4 = QPushButton("Hacer el test final")
but5 = QPushButton("Enviar los resultado")
text = QLabel("Prueba de Rufier")
text2 = QLabel("Por favor escriba los datos necesarios en la siguiente pagina")
text3 = QLabel("3")
text4 = QLabel("4")
text5 = QLabel("5")
text6 = QLabel("6")
text7 = QLabel("5")
text8 = QLabel("6")
instertarinfo1 = QLineEdit("0")
instertarinfo2 = QLineEdit("0")
instertarinfo3 = QLineEdit("0")
instertarinfo4 = QLineEdit("0")
instertarinfo5 = QLineEdit("0")


line = QVBoxLayout()

line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(text2, alignment = Qt.AlignCenter)
line.addWidget(but1, alignment = Qt.AlignCenter)

main_win.setLayout(line)


#Ventana 2


line2 = QVBoxLayout()

line2.addWidget(text3, alignment = Qt.AlignCenter)
line2.addWidget(instertarinfo1, alignment = Qt.AlignCenter)
line2.addWidget(text4, alignment = Qt.AlignCenter)
line2.addWidget(instertarinfo2, alignment = Qt.AlignCenter)
line2.addWidget(text6, alignment = Qt.AlignCenter)
line2.addWidget(but2, alignment = Qt.AlignCenter)
line2.addWidget(instertarinfo3, alignment = Qt.AlignCenter)
line2.addWidget(text7, alignment = Qt.AlignCenter)
line2.addWidget(but3, alignment = Qt.AlignCenter)
line2.addWidget(text8, alignment = Qt.AlignCenter)
line2.addWidget(but4, alignment = Qt.AlignCenter)
line2.addWidget(instertarinfo4, alignment = Qt.AlignCenter)
line2.addWidget(instertarinfo5, alignment = Qt.AlignCenter)

ventana2.setLayout(line2)


def mostrarventana2():
    main_win.hide()
    ventana2.show()
    print("Hola")

def mostrarventana3():
    ventana2.hide()
    ventana3.show()





but1.clicked.connect(mostrarventana2)

main_win.show()
app.exec_()


