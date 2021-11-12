import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(300, 550)
    w.move(300, 300) #960x540 - Центр экрана (На центр экрана встает верхний левый угол)
    w.setWindowTitle('Tetris by Ars')
    w.show()

    sys.exit(app.exec_())