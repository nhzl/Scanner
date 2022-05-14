from scanner import *


def main():
    app = QApplication([])
    window = Scanner()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
