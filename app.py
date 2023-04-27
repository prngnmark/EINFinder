from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QPushButton, QMainWindow
import sys

dict = {}

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('EIN FINDER')
        self.setFixedSize(300, 150)
        self.UIComponents()


    def UIComponents(self):
        welcomeMsg = QLabel(parent=self)
        welcomeMsg.setText("<b>ENTER COMPANY OF EIN TO FIND</b>")
        welcomeMsg.setGeometry(45, 25, 250, 50)
        companyEdit = QLineEdit(self)
        companyEdit.setGeometry(50, 65, 200, 25)
        findButton = QPushButton('Search', self)
        findButton.setGeometry(100, 100, 100, 40)
        self.searchWindow = SearchWindow()
        findButton.clicked.connect(self.searchWindow.show)
        self.companyName = companyEdit.text

class SearchWindow(QWidget):
    def __init__(self):
        super(SearchWindow, self).__init__()
        self.setFixedSize(300, 150)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 400, 300)
        self.label.setText('EIN Window')
        self.label.setGeometry(20,20,100,100)

def read_file():
    count = 0
    with open("EIN.txt", 'r') as f:
        for line in f:
            line = line.strip()
            try:
                split = line.split('#')
                dict[split[0]] = split[1]
            except:
                print(f"ERROR. NO COMPANY FOUND for line {count + 1}")
            count += 1
    return dict

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    read_file()
    print(dict)
    sys.exit(app.exec())
