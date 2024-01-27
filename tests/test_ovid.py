import sys
import unittest
from PyQt6.QtWidgets import QApplication
from PyQt6.QtTest import QTest
from ovid.Ovid import Ovid

app = QApplication([])


class TestOvid(unittest.TestCase):
    def setUp(self):
        self.ovid = Ovid()

    def test_default_values(self):
        self.assertEqual(Ovid.defaultFontFamily, "Arial")
        self.assertEqual(Ovid.defaultFontSize, 25)
        self.assertEqual(Ovid.defaultMargin, 20)

    def test_init(self):
        self.assertIsNotNone(self.ovid.textEditor)
        self.assertIsNotNone(self.ovid.sidebar)


if __name__ == "__main__":
    unittest.main()
