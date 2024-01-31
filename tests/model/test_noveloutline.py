import unittest
from ovid.model.Novel import Novel
from ovid.model.Chapter import Chapter
from ovid.model.NovelOutline import NovelOutline


class TestNovelOutline(unittest.TestCase):
    def setUp(self):
        self.novel = Novel(f"Test Novel {self._testMethodName}")
        self.novel_outline = NovelOutline(self.novel)

    def test_add_and_remove_section(self):
        outline = self.novel_outline
        chapter = Chapter("Test Chapter")
        outline.add_section(chapter, "Test Section")
        self.assertEqual(outline.get_section(chapter), "Test Section")
        outline.remove_section(chapter, "Test Section")
        self.assertEqual(outline.get_section(chapter), None)

    def test_sync_with_novel(self):
        novel = self.novel
        outline = self.novel_outline
        chapter = Chapter("Test Chapter")
        novel.add_chapter(chapter)
        outline.sync_with_novel()
        self.assertEqual(outline.get_section(chapter), None)
        novel.delete_chapter(chapter)
        outline.sync_with_novel()
        self.assertEqual(outline.get_section(chapter), None)


if __name__ == "__main__":
    unittest.main()
