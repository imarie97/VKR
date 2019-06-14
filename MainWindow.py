import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QWidget, QPushButton, QMessageBox
from PyQt5.uic import loadUi

from genetic_for_mass import ga
from visualize import vizualize


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self);
        self.btnCalc.clicked.connect(self.btnCalc_clicked)
        self.btnDefault.clicked.connect(self.btnDefault_clicked)

    @pyqtSlot()
    def btnCalc_clicked(self):
        try:
            a = float(self.txa.text())
            b = float(self.txb.text())
            c = float(self.txc.text())
            try:
                alpha = int(self.txbA.text())
                beta = int(self.txbB.text())
                gamma = int(self.txbG.text())
                crop = int(self.txbChr.text())  # кол-во хромосом
                epoch = int(self.txbEpo.text()) # кол-во эпох
                L = int(self.txL.text())

                if not self.CheckAngle(alpha) or not self.CheckAngle(beta) or not self.CheckAngle(gamma):
                    self.ShowEror('Ошибка',"Некорректное значение угла",'Значение угла должно быть больше 0 '
                                                                        'и меньше 180 градусов')
                else:
                    l1 = L/2 - a/2
                    l2 = L/2 - b/2
                    l3 = L/2 - c/2
                    limit = [l1, l2, l3,  alpha, beta, gamma]
                    v = ga(limit, -l1, l1, -l2, l2, -l3, l3, crop, epoch, a, b, c)
                    vizualize(v, 'Optimal zone')

            except Exception:
                self.ShowEror('Ошибка','Введены некорректные данные','Проверьте значения полей - '
                                                                     'все значения (кроме а) должны быть целым числом')
        except Exception:
            self.ShowEror('Ошибка', 'Введены некорректные данные',
                          'поле "a" должно быть числом')

    @pyqtSlot()
    def btnDefault_clicked(self):
        self.SetDef()

    def SetDef(self):
        self.txbA.setText('20')
        self.txbB.setText('20')
        self.txbG.setText('20')
        self.txbChr.setText('500')
        self.txbEpo.setText('7')
        self.txL.setText('2')
        self.txa.setText('0.8')
        self.txb.setText('0.8')
        self.txc.setText('0.8')

    def ShowEror(self, title,text,details):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(text)
        msg.setInformativeText(details)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def CheckAngle(self, angle):
        return angle > 0 and angle < 180


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = App()
    widget.SetDef()
    widget.show()
    sys.exit(app.exec_())
