from PyQt6.QtWidgets import QFontComboBox

class OvidFontComboBox(QFontComboBox):
    defaultFonts = ['Arial', 'Times New Roman', 'Courier New', 'Verdana', 'Courier']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clear()
        self.addItems(self.defaultFonts)