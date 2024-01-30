import unittest
from PyQt6.QtWidgets import QApplication
from ovid.ui.OvidDockWidget import OvidDockWidget
from ovid.model.Novel import Novel
from ovid.Ovid import Ovid

app = QApplication([])


class TestOvidDockWidget(unittest.TestCase):
    def setUp(self):
        self.parent = Ovid()
        self.widget = OvidDockWidget(self.parent)

    def test_initial_state(self):
        self.assertIsInstance(self.widget.novel, Novel)
        self.assertEqual(self.widget.maximumWidth(), 200)
        self.assertIsNotNone(self.widget.sidebar_widget)
        self.assertIsNotNone(self.widget.sidebar_layout)
        self.assertIsNotNone(self.widget.add_chapter_button)

    @unittest.skip("Creates an input dialog. I need to learn how to test this.")
    def test_add_chapter_button(self):
        # Assuming add_chapter method is defined in the parent class
        add_chapter = self.parent.add_chapter
        self.parent.add_chapter = lambda: add_chapter(self.parent, "New Chapter")
        initial_count = self.widget.parent().chapterList.count()
        self.widget.add_chapter_button.click()
        self.assertEqual(self.widget.parent().chapterList.count(), initial_count + 1)


if __name__ == "__main__":
    unittest.main()
