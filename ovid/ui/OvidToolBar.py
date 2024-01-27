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
        defaultFont = self.parent.defaultFontFamily
        defaultFontSize = self.parent.defaultFontSize

        # Add actions for text formatting
        bold_button = QToolButton()
        bold_button.setText("B")
        bold_button.setFont(QFont(defaultFont, defaultFontSize, QFont.Weight.Bold))
        bold_button.setToolTip("Bold")
        bold_button.clicked.connect(self.parent.fonts.setBoldText)
        self.addWidget(bold_button)

        italic_button = QToolButton()
        italic_button.setText("I")
        italic_font = QFont(defaultFont, defaultFontSize)
        italic_font.setItalic(True)
        italic_button.setFont(italic_font)
        italic_button.setToolTip("Italic")
        italic_button.clicked.connect(self.parent.fonts.setItalicText)
        self.addWidget(italic_button)

        underline_button = QToolButton()
        underline_button.setText("U")
        underline_font = QFont(defaultFont, defaultFontSize)
        underline_font.setUnderline(True)
        underline_button.setFont(underline_font)
        underline_button.setToolTip("Underline")
        underline_button.clicked.connect(self.parent.fonts.setUnderlineText)
        self.addWidget(underline_button)

        strikethrough_button = QToolButton()
        strikethrough_button.setText("S")
        strikethrough_font = QFont(defaultFont, defaultFontSize)
        strikethrough_font.setStrikeOut(True)
        strikethrough_button.setFont(strikethrough_font)
        strikethrough_button.setToolTip("Strikethrough")
        strikethrough_button.clicked.connect(self.parent.fonts.setStrikeThroughText)
        self.addWidget(strikethrough_button)

        clearformatting_button = QToolButton()
        clearformatting_button.setText("C")
        clearformatting_button.setFont(QFont(defaultFont, defaultFontSize))
        clearformatting_button.setToolTip("Clear Formatting")
        clearformatting_button.clicked.connect(self.parent.fonts.clearFormatting)
        self.addWidget(clearformatting_button)

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