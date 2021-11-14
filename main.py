import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300, 550) # Данная комагда определяет размеры окна, а команда ниже его место расположенияя
    w.move(960-(300)/2, 540-(550)/2) #960x540 - Центр экрана (На центр экрана встает верхний левый угол)
    w.setWindowTitle('Tetris by Ars') # Задаем заголовок окна
    w.setWindowIcon(QIcon('icon image for tetris.png')) # Задает иконку приложения
    w.show() # показывает само окно приложения
    sys.exit(app.exec_())
