from PyQt6.QtWidgets import QToolBar, QToolButton, QComboBox, QLabel, QWidgetAction
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from .OvidFontComboBox import OvidFontComboBox
from .OvidOutlineWidget import OvidOutlineWidget


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
        for i in range(8, 31):
            self.fontSizeComboBox.addItem(str(i))
        self.fontSizeComboBox.setCurrentText(str(self.parent.defaultFontSize))
        self.fontSizeComboBox.setEditable(True)
        self.fontComboBox.setCurrentText(self.parent.defaultFontFamily)

        # Connect font and font size combobox
        self.fontComboBox.currentTextChanged.connect(self.parent.fonts.setFontFamily)
        self.fontSizeComboBox.currentTextChanged.connect(self.parent.fonts.setFontSize)
    
        # temporarily remove this until we can debug it
        if False:
            # Add a label for the mode select combo box
            mode_label = QLabel("Mode:")
            mode_label_action = QWidgetAction(self)
            mode_label_action.setDefaultWidget(mode_label)
            self.addAction(mode_label_action)

            # Add a combo box for selecting between "Novel" and "Outline"
            mode_select = QComboBox()
            mode_select.addItem("Novel")
            mode_select.addItem("Outline")
            mode_select.currentTextChanged.connect(self.onModeChanged)
            mode_select_action = QWidgetAction(self)
            mode_select_action.setDefaultWidget(mode_select)
            self.addAction(mode_select_action)

            # # Create the outline widget and add it to the layout, but hide it initially
            self.outlineWidget = OvidOutlineWidget(self)
            self.outlineWidget.hide()

            # Create a QWidgetAction for the outline widget and add it to the toolbar
            outline_widget_action = QWidgetAction(self)
            outline_widget_action.setDefaultWidget(self.outlineWidget)
            self.addAction(outline_widget_action)

    def onModeChanged(self, text):
        if text == "Novel":
            self.outlineWidget.hide()
            self.parent.setCentralWidget(self.parent.textEditor)
            self.parent.textEditor.show()
        elif text == "Outline":
            self.outlineWidget.setNovel(self.parent.novel)
            self.parent.textEditor.hide()
            self.parent.setCentralWidget(self.outlineWidget)
            self.outlineWidget.show()