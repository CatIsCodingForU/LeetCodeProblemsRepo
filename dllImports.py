from ctypes import cdll
import ctypes
import sys
import operatorsUI
from PyQt5 import QtWidgets


def init_dll():
    lib = cdll.LoadLibrary("D:\\DEV\\C++\\Projects\\4 sem\\EVM-test\\Dll-exersises-3\\MyLibrary3\\Debug\\MyLibrary3.dll")

    lib.addFloat.argtypes = [ctypes.c_float, ctypes.c_float]
    lib.addFloat.restype = ctypes.c_float

    lib.subFloat.argtypes = [ctypes.c_float, ctypes.c_float]
    lib.subFloat.restype = ctypes.c_float

    lib.divFloat.argtypes = [ctypes.c_float, ctypes.c_float]
    lib.divFloat.restype = ctypes.c_float

    lib.mulFloat.argtypes = [ctypes.c_float, ctypes.c_float]
    lib.mulFloat.restype = ctypes.c_float

    return lib


class ExampleApp(QtWidgets.QMainWindow, operatorsUI.Ui_Dialog):
    def __init__(self):


        super().__init__()
        self.setupUi(self)

        self.add_btn.clicked.connect(self.add_btn_click)
        self.mul_btn.clicked.connect(self.mul_btn_click)
        self.div_btn.clicked.connect(self.div_btn_click)
        self.sub_btn.clicked.connect(self.sub_btn_click)

        self.lib = init_dll()

    def add_btn_click(self):
        self.lineRes.setText(str(self.lib.addFloat(float(self.lineA.text()), float(self.lineB.text()))))

    def mul_btn_click(self):
        self.lineRes.setText(str(self.lib.mulFloat(float(self.lineA.text()), float(self.lineB.text()))))

    def div_btn_click(self):
        self.lineRes.setText(str(self.lib.divFloat(float(self.lineA.text()), float(self.lineB.text()))))

    def sub_btn_click(self):
        self.lineRes.setText(str(self.lib.subFloat(float(self.lineA.text()), float(self.lineB.text()))))



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
'''

func = lib['_ZN11TestLibrary4calcEv']  #my func is double myFunc(double);
func.restype = ctypes.c_int

value = func()
print(value)

'''




