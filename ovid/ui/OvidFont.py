from PyQt6.QtGui import QFont, QTextCharFormat

class OvidFont:
    def __init__(self, ovid) -> None:
        self.textEditor = ovid.textEditor

    def setBoldText(self):
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Bold)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setItalicText(self):
        fmt = QTextCharFormat()
        fmt.setFontItalic(True)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setUnderlineText(self):
        fmt = QTextCharFormat()
        fmt.setFontUnderline(True)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setStrikeThroughText(self):
        fmt = QTextCharFormat()
        fmt.setFontStrikeOut(True)
        self.textEditor.textCursor().mergeCharFormat(fmt)  # Connect actions

    def setFontFamily(self, font):
        fmt = self.textEditor.currentCharFormat()
        fmt.setFontFamily(font)
        self.textEditor.setCurrentCharFormat(fmt)

    def setFontFamily(self, font):
        fmt = self.textEditor.currentCharFormat()
        fmt.setFontFamily(font)
        self.textEditor.setCurrentCharFormat(fmt)

    def setFontSize(self, size):
        cursor = self.textEditor.textCursor()

        if not cursor.hasSelection():
            # If no text is selected, change the font size for future text
            fmt = cursor.charFormat()
            fmt.setFontPointSize(float(size))
            cursor.setCharFormat(fmt)
        else:
            # If text is selected, change the font size for the selection
            fmt = QTextCharFormat()
            fmt.setFontPointSize(float(size))
            cursor.mergeCharFormat(fmt)