from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont, QPalette, QColor, QTextBlockFormat, QTextCharFormat

class OvidTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        
        # Set the font
        self.font = QFont("Arial", 25)
        self.setFont(self.font)

        # Set the text color
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Text, QColor("black"))
        self.setPalette(palette)

        # Set the indent for new paragraphs
        self.format = QTextBlockFormat()
        self.format.setTextIndent(50)
        self.format.setIndent(0)

        # Set the background color
        self.setStyleSheet("background-color: white;")

        # Set the margins
        self.setViewportMargins(parent.defaultMargin, parent.defaultMargin, parent.defaultMargin, parent.defaultMargin)

    def insertFromMimeData(self, source):
        cursor = self.textCursor()

        # Create a QTextCharFormat and set its font
        format = QTextCharFormat()
        format.setFont(self.font)

        # Apply the QTextCharFormat and QTextBlockFormat to the QTextCursor
        cursor.setCharFormat(format)
        cursor.setBlockFormat(self.format)

        # Check the MIME type of the incoming data
        if source.hasFormat('text/plain'):
            print("text/plain")
            text = source.text()
            cursor.insertText(text)
        elif source.hasFormat('text/html'):
            print("text/html")
            html = source.html()
            # Strip the HTML tags
            text = re.sub('<[^<]+?>', '', html)
            cursor.insertText(text)