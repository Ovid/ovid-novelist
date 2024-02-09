import unittest
from ovid.model.Chapter import Chapter
from ovid.model.Novel import Novel


class TestNovel(unittest.TestCase):
    def setUp(self):
        self.novel = Novel()
        self.chapter1 = Chapter("Chapter 1", "This is the first chapter.")
        self.chapter2 = Chapter("Chapter 2", "This is the second chapter.")

    def test_init(self):
        novel = Novel(title="My Novel", genre="Fantasy")
        self.assertTrue(novel.hasNoChapters())
        self.assertEqual(novel.title, "My Novel")
        self.assertEqual(novel.genre, "Fantasy")
        self.assertEqual(novel.chapters, [])

    def test_add_chapter(self):
        self.assertTrue(self.novel.hasNoChapters())
        self.novel.add_chapter(self.chapter1)
        self.assertFalse(self.novel.hasNoChapters())
        self.assertEqual(len(self.novel.get_chapters()), 1)
        self.assertEqual(self.novel.get_chapters()[0].title, "Chapter 1")

    def test_delete_chapter(self):
        self.novel.add_chapter(self.chapter1)
        self.novel.add_chapter(self.chapter2)
        self.novel.delete_chapter(self.chapter1)
        self.assertEqual(len(self.novel.get_chapters()), 1)
        self.assertEqual(self.novel.get_chapters()[0].title, "Chapter 2")
        self.assertIsNone(self.novel.get_chapters()[0].previous_chapter)

    def test_get_chapters(self):
        self.novel.add_chapter(self.chapter1)
        self.novel.add_chapter(self.chapter2)
        chapters = self.novel.get_chapters()

        for chapter in chapters:
            self.assertIsInstance(chapter, Chapter)
        self.assertEqual(len(chapters), 2)
        self.assertEqual(chapters[0].title, "Chapter 1")
        self.assertEqual(chapters[1].title, "Chapter 2")

    def test_set_current_chapter(self):
        self.novel.set_current_chapter(self.chapter1)
        self.assertEqual(self.novel.currentChapter, self.chapter1)

        self.novel.set_current_chapter(self.chapter2)
        self.assertEqual(self.novel.currentChapter, self.chapter2)

    def test_add_outline(self):
        self.novel.add_outline(self.chapter1, "Introduction")
        self.assertIn("Introduction", self.novel.outline.get_section(self.chapter1))
        self.assertEqual(self.novel.outline.get_section(self.chapter1), "Introduction")
    
    def test_sync_with_novel(self):
        novel = self.novel
        chapter = Chapter("Test Chapter")
        novel.add_chapter(chapter)
        self.assertEqual(novel.get_outline(chapter), None)

        novel.add_outline(chapter, "Test Section")
        self.assertEqual(novel.get_outline(chapter), "Test Section")

        novel.delete_chapter(chapter)
        self.assertEqual(novel.get_outline(chapter), None)


if __name__ == "__main__":
    unittest.main()
