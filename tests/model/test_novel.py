import unittest
from ovid.model.Chapter import Chapter
from ovid.model.Novel import Novel

class TestNovel(unittest.TestCase):
    def setUp(self):
        self.novel = Novel()
        print("We are in setUp()")
    
    def test_add_chapter(self):
        print("We are in test_add_chapter()")
        self.novel.add_chapter("Chapter 1", "This is the first chapter.")
        self.assertEqual(len(self.novel.get_chapters()), 1)
        self.assertEqual(self.novel.get_chapters()[0].title, "Chapter 1")

    def test_delete_chapter(self):
        print("We are in test_delete_chapter()")
        chapter1 = self.novel.add_chapter("Chapter 1", "This is the first chapter.")
        chapter2 = self.novel.add_chapter("Chapter 2", "This is the second chapter.")
        self.novel.delete_chapter(chapter1)
        self.assertEqual(len(self.novel.get_chapters()), 1)
        self.assertEqual(self.novel.get_chapters()[0].title, "Chapter 2")
        self.assertIsNone(self.novel.get_chapters()[0].previous_chapter)

    def test_get_chapters(self):
        print("We are in test_get_chapters()")
        self.novel.add_chapter("Chapter 1", "This is the first chapter.")
        self.novel.add_chapter("Chapter 2", "This is the second chapter.")
        chapters = self.novel.get_chapters()

        for chapter in chapters:
            self.assertIsInstance(chapter, Chapter)
            print(chapter.title)
        self.assertEqual(len(chapters), 2)
        self.assertEqual(chapters[0].title, "Chapter 1")
        self.assertEqual(chapters[1].title, "Chapter 2")

if __name__ == '__main__':
    unittest.main()
