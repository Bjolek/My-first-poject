import random

from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500 , 500)

firstText = QLabel("Тицни,щоб дізнатися пкркможця")
WinText = QLabel("Переможуць")
knopka =QPushButton("Визначи переможця")

line = QHBoxLayout()
line.addWidget(firstText)
line.addWidget(WinText)
line.addWidget(knopka)

window.setLayout(line)
window.show()

def a():
    b = str(random.randint(0 , 100))
    WinText.setText(b)

knopka.clicked.connect(a)
app.exec()

