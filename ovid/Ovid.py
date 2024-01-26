import sys
from PyQt6.QtWidgets import QTextEdit, QToolButton, QApplication, QMainWindow, QToolBar, QComboBox, QDockWidget, QListWidget, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QAction, QFont, QTextCursor, QTextCharFormat, QShortcut, QKeySequence
from PyQt6.QtCore import Qt
from ovid.ui.OvidFontComboBox import OvidFontComboBox
from ovid.ui.OvidFont import OvidFont

class Ovid(QMainWindow):
    defaultFontFamily = 'Arial'
    defaultFontSize = 16

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Ovid')
        self.setGeometry(100, 100, 1200, 800)
        # Create the text editor area
        self.textEditor = QTextEdit()
        self.setCentralWidget(self.textEditor)
        self.fonts = OvidFont(self)
        self.fonts.setFontSize(Ovid.defaultFontSize)

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

        # Add actions to Edit menu
        bold_action = QAction('Bold', self)
        italic_action = QAction('Italic', self)
        underline_action = QAction('Underline', self)
        strikethrough_action = QAction('Strikethrough', self)

        edit_menu.addAction(bold_action)
        edit_menu.addAction(italic_action)
        edit_menu.addAction(underline_action)
        edit_menu.addAction(strikethrough_action)

        # Create Toolbar
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        # Add actions for text formatting
        bold_button = QToolButton()
        bold_button.setText('B')
        bold_button.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        bold_button.setToolTip('Bold')
        bold_button.clicked.connect(self.fonts.setBoldText)
        self.toolbar.addWidget(bold_button)

        italic_button = QToolButton()
        italic_button.setText('I')
        italic_font = QFont('Arial', 16)
        italic_font.setItalic(True)
        italic_button.setFont(italic_font)
        italic_button.setToolTip('Italic')
        italic_button.clicked.connect(self.fonts.setItalicText)
        self.toolbar.addWidget(italic_button)

        underline_button = QToolButton()
        underline_button.setText('U')
        underline_font = QFont('Arial', 16)
        underline_font.setUnderline(True)
        underline_button.setFont(underline_font)
        underline_button.setToolTip('Underline')
        underline_button.clicked.connect(self.fonts.setUnderlineText)
        self.toolbar.addWidget(underline_button)

        strikethrough_button = QToolButton()
        strikethrough_button.setText('S')
        strikethrough_font = QFont('Arial', 16)
        strikethrough_font.setStrikeOut(True)
        strikethrough_button.setFont(strikethrough_font)
        strikethrough_button.setToolTip('Strikethrough')
        strikethrough_button.clicked.connect(self.fonts.setStrikeThroughText)
        self.toolbar.addWidget(strikethrough_button)

        # Add font selection dropdown
        self.fontComboBox = OvidFontComboBox(self)
        self.toolbar.addWidget(self.fontComboBox)

        # Add font size selection dropdown
        self.fontSizeComboBox = QComboBox(self)
        self.toolbar.addWidget(self.fontSizeComboBox)
        for i in range(8, 30):
            self.fontSizeComboBox.addItem(str(i))
            
        self.fontSizeComboBox.setCurrentText(str(Ovid.defaultFontSize))
        self.fontSizeComboBox.setEditable(True)
        self.fontComboBox.setCurrentText(Ovid.defaultFontFamily)
        
        # Shortcuts for text formatting
        QShortcut(QKeySequence('Ctrl+B'), self, self.fonts.setBoldText)
        QShortcut(QKeySequence('Ctrl+I'), self, self.fonts.setItalicText)
        QShortcut(QKeySequence('Ctrl+U'), self, self.fonts.setUnderlineText)
        QShortcut(QKeySequence('Ctrl+T'), self, self.fonts.setStrikeThroughText)

        # Create the dockable sidebar
        self.sidebar = QDockWidget("Chapters", self)
        self.sidebar.setMaximumWidth(200)  # Set a preferred width for the sidebar
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.sidebar)

        # Create a widget to hold the list and the button
        self.sidebarWidget = QWidget()
        self.sidebarLayout = QVBoxLayout(self.sidebarWidget)

        # Create the QListWidget for chapters
        self.chapterList = QListWidget()
        self.sidebarLayout.addWidget(self.chapterList)

        # Create the button to add new chapters
        self.addChapterButton = QPushButton("Add Chapter")
        self.addChapterButton.clicked.connect(self.addChapter)
        self.sidebarLayout.addWidget(self.addChapterButton)

        # Set the widget to the dock
        self.sidebar.setWidget(self.sidebarWidget)

        # Add toggle action for sidebar in view menu
        view_menu = self.menuBar().addMenu('View')
        toggleSidebarAction = QAction('Toggle Sidebar', self)
        toggleSidebarAction.triggered.connect(self.toggleSidebar)
        view_menu.addAction(toggleSidebarAction)

        # Connect font and font size combobox
        self.fontComboBox.currentTextChanged.connect(self.fonts.setFontFamily)
        self.fontSizeComboBox.currentTextChanged.connect(self.fonts.setFontSize)

    def addChapter(self):
        # This function will be called when the button is clicked
        # Here, you can add logic to add a new chapter to the chapterList
        new_chapter_name = f"Chapter {self.chapterList.count() + 1}"
        self.chapterList.addItem(new_chapter_name)
    
    def toggleSidebar(self):
        self.sidebar.setVisible(not self.sidebar.isVisible())

def main():
    app = QApplication(sys.argv)
    ex = Ovid()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()