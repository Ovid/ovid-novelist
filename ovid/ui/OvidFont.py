from PyQt6.QtGui import QFont, QTextCharFormat

class OvidFont:
    def __init__(self, ovid) -> None:
        self.textEditor = ovid.textEditor
    
    # Per https://www.riverbankcomputing.com/pipermail/pyqt/2024-January/045686.html
    # There appears to be a possible bug in MacOS and Linux PyQt6 where you can select
    # test, and apply formatting to it twice, and it will not remove the formatting.
    # The first time should apply the formatting (bold, italic, etc), and the second
    # time should remove it. This is not working in MacOS and Linux, but it is allegedly
    # working in Windows. This is a workaround for that bug.
    def clearFormatting(self):
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Normal)
        fmt.setFontItalic(False)
        fmt.setFontUnderline(False)
        fmt.setFontStrikeOut(False)
        self.textEditor.textCursor().setCharFormat(fmt)

    def setBoldText(self):
        fmt = QTextCharFormat()
        if self.textEditor.currentCharFormat().fontWeight() == QFont.Weight.Bold:
            fmt.setFontWeight(QFont.Weight.Normal)
        else:
            fmt.setFontWeight(QFont.Weight.Bold)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setItalicText(self):
        fmt = QTextCharFormat()
        if not self.textEditor.currentCharFormat().fontItalic():
            fmt.setFontItalic(True)
        else:
            fmt.setFontItalic(False)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setUnderlineText(self):
        fmt = QTextCharFormat()
        if not self.textEditor.currentCharFormat().fontUnderline():
            fmt.setFontUnderline(True)
        else:
            fmt.setFontUnderline(False)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setStrikeThroughText(self):
        fmt = QTextCharFormat()
        if not self.textEditor.currentCharFormat().fontStrikeOut():
            fmt.setFontStrikeOut(True)
        else:
            fmt.setFontStrikeOut(False)
        self.textEditor.textCursor().mergeCharFormat(fmt)

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