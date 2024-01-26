from PyQt6.QtWidgets import QFontComboBox


class OvidFontComboBox(QFontComboBox):
    defaultFonts = ["Arial", "Times New Roman", "Courier New", "Verdana"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clear()
        self.addItems(self.defaultFonts)
        self.currentFontChanged.connect(self.moveFontToTop)

    def moveFontToTop(self, font):
        self.currentFontChanged.disconnect(self.moveFontToTop)
        index = self.findText(font.family())
        if index >= 0:
            self.removeItem(index)
            self.insertItem(0, font.family())
            self.setCurrentIndex(0)
        self.currentFontChanged.connect(self.moveFontToTop)
