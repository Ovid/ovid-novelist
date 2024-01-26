import unittest
from ovid.ui.OvidFontComboBox import OvidFontComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

app = QApplication([])

class TestOvidFontComboBox(unittest.TestCase):
    def setUp(self):
        self.font_combo_box = OvidFontComboBox()

    def test_default_fonts(self):
        for font in OvidFontComboBox.defaultFonts:
            index = self.font_combo_box.findText(font)
            self.assertNotEqual(index, -1, f"{font} not found in combo box")

    def test_move_font_to_top(self):
        font = QFont("Verdana")
        self.font_combo_box.moveFontToTop(font)
        self.assertEqual(self.font_combo_box.currentText(), "Verdana")

if __name__ == "__main__":
    unittest.main()