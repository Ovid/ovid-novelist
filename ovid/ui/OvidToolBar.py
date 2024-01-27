from PyQt6.QtWidgets import QToolBar, QToolButton, QComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from .OvidFontComboBox import OvidFontComboBox

class OvidToolBar(QToolBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initToolBar()

    def initToolBar(self):

        # Add actions for text formatting
        bold_button = QToolButton()
        bold_button.setText("B")
        bold_button.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        bold_button.setToolTip("Bold")
        bold_button.clicked.connect(self.parent.fonts.setBoldText)
        self.addWidget(bold_button)

        italic_button = QToolButton()
        italic_button.setText("I")
        italic_font = QFont("Arial", 16)
        italic_font.setItalic(True)
        italic_button.setFont(italic_font)
        italic_button.setToolTip("Italic")
        italic_button.clicked.connect(self.parent.fonts.setItalicText)
        self.addWidget(italic_button)

        underline_button = QToolButton()
        underline_button.setText("U")
        underline_font = QFont("Arial", 16)
        underline_font.setUnderline(True)
        underline_button.setFont(underline_font)
        underline_button.setToolTip("Underline")
        underline_button.clicked.connect(self.parent.fonts.setUnderlineText)
        self.addWidget(underline_button)

        strikethrough_button = QToolButton()
        strikethrough_button.setText("S")
        strikethrough_font = QFont("Arial", 16)
        strikethrough_font.setStrikeOut(True)
        strikethrough_button.setFont(strikethrough_font)
        strikethrough_button.setToolTip("Strikethrough")
        strikethrough_button.clicked.connect(self.parent.fonts.setStrikeThroughText)
        self.addWidget(strikethrough_button)

        # Add all the toolbar logic here
        # For example:
        #strikethrough_button = QToolButton(self)
        #strikethrough_button.setToolTip("Strikethrough")
        #strikethrough_button.clicked.connect(self.parent.fonts.setStrikeThroughText)
        #self.addWidget(strikethrough_button)

        # Add font selection dropdown
        self.fontComboBox = OvidFontComboBox(self)
        self.addWidget(self.fontComboBox)

        # Add font size selection dropdown
        self.fontSizeComboBox = QComboBox(self)
        self.addWidget(self.fontSizeComboBox)
        for i in range(8, 30):
            self.fontSizeComboBox.addItem(str(i))

        self.fontSizeComboBox.setCurrentText(str(self.parent.defaultFontSize))
        self.fontSizeComboBox.setEditable(True)
        self.fontComboBox.setCurrentText(self.parent.defaultFontFamily)

        # Connect font and font size combobox
        self.fontComboBox.currentTextChanged.connect(self.parent.fonts.setFontFamily)
        self.fontSizeComboBox.currentTextChanged.connect(self.parent.fonts.setFontSize)