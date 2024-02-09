from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import (
    QFont,
    QPalette,
    QColor,
    QTextBlockFormat,
    QTextCharFormat,
)


class OvidTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # Set the font
        self.font = QFont(self.parent.defaultFontFamily, self.parent.defaultFontSize)
        self.setFont(self.font)

        # Set the text color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor("black"))
        self.setPalette(palette)

        # Set the indent for new paragraphs
        self.paragraphFormat = QTextBlockFormat()
        self.paragraphFormat.setTextIndent(50)
        self.paragraphFormat.setIndent(0)

        # Set the background color
        self.setStyleSheet("background-color: white;")

        # Set the margins
        self.setViewportMargins(
            parent.defaultMargin,
            parent.defaultMargin,
            parent.defaultMargin,
            parent.defaultMargin,
        )

    # override the keyPressEvent to apply our formatting
    # Github: https://github.com/Ovid/ovid-novelist/issues/2
    # def keyPressEvent(self, event):
    #     if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
    #         cursor = self.textCursor()
    #         cursor.setBlockFormat(self.paragraphFormat)
    #         cursor.movePosition(QTextCursor.MoveOperation.End)
    #         self.setTextCursor(cursor)
    #     super().keyPressEvent(event)

    def insertFromMimeData(self, source):
        cursor = self.textCursor()

        # Create a QTextCharFormat and set its font
        format = QTextCharFormat()
        format.setFont(self.font)

        # Apply the QTextCharFormat and QTextBlockFormat to the QTextCursor
        cursor.setCharFormat(format)
        cursor.setBlockFormat(self.paragraphFormat)

        # Check the MIME type of the incoming data
        if source.hasFormat("text/plain"):
            print("text/plain")
            text = source.text()
            cursor.insertText(text)
        elif source.hasFormat("text/html"):
            print("text/html")
            html = source.html()
            # FIXME: Strip the HTML tags. I absolutely need to come back to this.
            text = re.sub("<[^<]+?>", "", html)
            cursor.insertText(text)
