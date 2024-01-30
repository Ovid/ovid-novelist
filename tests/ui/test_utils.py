import unittest
from unittest.mock import Mock
from PyQt6.QtWidgets import QApplication
from ovid.ui.Utils import setNovel
from ovid.model.Novel import Novel
from ovid.model.Chapter import Chapter
from ovid.Ovid import Ovid

app = QApplication([])


class TestSetNovel(unittest.TestCase):
    def setUp(self):
        self.ovid = Ovid()
        self.novel = Novel()
        chapter1 = Chapter("Chapter 1", "Contents 1")
        self.novel.add_chapter(Chapter("Chapter 1", contents="Contents 1"))
        self.novel.add_chapter(Chapter("Chapter 2", contents="Contents 2"))

    def test_set_novel(self):
        setNovel(self.ovid, self.novel)
        self.assertEqual(self.ovid.novel, self.novel)
        self.assertEqual(self.ovid.chapterList.count(), len(self.novel.chapters))
        self.assertEqual(self.ovid.textEditor.toHtml(), self.novel.chapters[0].contents)

    def test_set_novel_with_current_chapter(self):
        self.novel.currentChapter = self.novel.chapters[1]
        setNovel(self.ovid, self.novel)
        self.assertEqual(self.ovid.novel, self.novel)
        self.assertEqual(self.ovid.chapterList.count(), len(self.novel.chapters))
        self.assertEqual(
            self.ovid.textEditor.toHtml(), self.novel.currentChapter.contents
        )


if __name__ == "__main__":
    unittest.main()
