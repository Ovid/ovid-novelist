import unittest
from unittest.mock import Mock, MagicMock
from PyQt6.QtGui import QFont, QTextCharFormat
from ovid.ui.OvidFont import OvidFont


class TestOvidFont(unittest.TestCase):
    def setUp(self):
        self.ovid = Mock()
        self.ovid.textEditor = Mock()
        self.ovid.textEditor.textCursor = MagicMock()
        self.ovid.textEditor.currentCharFormat = MagicMock()
        self.ovid.textEditor.setCurrentCharFormat = MagicMock()
        self.font = OvidFont(self.ovid)

    def test_setBoldText(self):
        self.font.setBoldText()
        self.ovid.textEditor.setFontWeight.assert_called()

    def test_setItalicText(self):
        self.font.setItalicText()
        self.ovid.textEditor.textCursor().mergeCharFormat.assert_called()

    def test_setUnderlineText(self):
        self.font.setUnderlineText()
        self.ovid.textEditor.textCursor().mergeCharFormat.assert_called()

    def test_setStrikeThroughText(self):
        self.font.setStrikeThroughText()
        self.ovid.textEditor.textCursor().mergeCharFormat.assert_called()

    def test_setFontFamily(self):
        self.font.setFontFamily("Arial")
        self.ovid.textEditor.setCurrentCharFormat.assert_called()

    def test_setFontSize(self):
        self.font.setFontSize(12)
        self.assertTrue(
            self.ovid.textEditor.textCursor().setCharFormat.called
            or self.ovid.textEditor.textCursor().mergeCharFormat.called
        )


if __name__ == "__main__":
    unittest.main()
