from view import Ui_PortScanner
from PyQt5.QtWidgets import *
import sys
import socket

'''
Simple Port Scanner
Adapted from:
https://www.youtube.com/watch?v=d3D8PAZV51g
***Added port range functionality
***Created GUI
***Cleaned up code
'''

class Scanner(QMainWindow, Ui_PortScanner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.scanButton.clicked.connect(
            lambda: self.port_scanner(self.hostBox.toPlainText(), self.startBox.toPlainText(), self.endBox.toPlainText()))
        self.resetButton.clicked.connect(lambda: self.reset())

    def port_scanner(self, host, a, b):
        a = int(a)
        b = int(b)
        try:
            for port in range(a, b):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex((host, port))
                if result == 0:
                    self.listWidget.addItem("Port {} is open".format(port))
                    s.close()
                else:
                    self.listWidget.addItem("No response on port: {}".format(port))
                    s.close()
        except KeyboardInterrupt:
            print("You pressed Ctrl+C!")
            sys.exit()

    def reset(self):
        self.hostBox.clear()
        self.startBox.clear()
        self.endBox.clear()
        self.listWidget.clear()