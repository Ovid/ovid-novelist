import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction

class Ovid(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ovid')
        self.setGeometry(100, 100, 800, 600)

        # Create Menu Bar
        menu_bar = self.menuBar()

        # Add menus
        file_menu = menu_bar.addMenu('File')
        edit_menu = menu_bar.addMenu('Edit')
        view_menu = menu_bar.addMenu('View')

        # Add actions to File menu
        new_action = QAction('New', self)
        open_action = QAction('Open...', self)
        save_action = QAction('Save', self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)

        # Similarly, you can add actions to Edit and View menus
        # ...

def main():
    app = QApplication(sys.argv)
    ex = Ovid()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

