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
    #
    # Github: https://github.com/Ovid/ovid-novelist/issues/1
    def clearFormatting(self):
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Weight.Normal)
        fmt.setFontItalic(False)
        fmt.setFontUnderline(False)
        fmt.setFontStrikeOut(False)
        self.textEditor.textCursor().setCharFormat(fmt)

    def setBoldText(self):
        cursor = self._getCursor()

        # Check if the text (either selected or where the cursor is) is bold
        is_bold = cursor.charFormat().fontWeight() == QFont.Weight.Bold

        # Apply the new weight based on the current state
        new_weight = QFont.Weight.Normal if is_bold else QFont.Weight.Bold
        self.textEditor.setFontWeight(new_weight)

    def setItalicText(self):
        cursor = self._getCursor()
        fmt = QTextCharFormat()
        if not cursor.charFormat().fontItalic():
            fmt.setFontItalic(True)
        else:
            fmt.setFontItalic(False)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setUnderlineText(self):
        cursor = self._getCursor()
        fmt = QTextCharFormat()
        if not cursor.charFormat().fontUnderline():
            fmt.setFontUnderline(True)
        else:
            fmt.setFontUnderline(False)
        self.textEditor.textCursor().mergeCharFormat(fmt)

    def setStrikeThroughText(self):
        cursor = self._getCursor()
        fmt = QTextCharFormat()
        if not cursor.charFormat().fontStrikeOut():
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

    def _getCursor(self):
        # If there's a selection, and the cursor is not at the block start and
        # at the beginning of the selection, move the cursor to the end of the
        # selection
        cursor = self.textEditor.textCursor()
        if (
            cursor.hasSelection()
            and not cursor.atBlockStart()
            and cursor.position() == cursor.selectionStart()
        ):
            cursor.setPosition(cursor.selectionEnd())
        return cursor
