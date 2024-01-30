import unittest
from ovid.model.Chapter import Chapter


class TestChapter(unittest.TestCase):
    def test_init(self):
        chapter = Chapter("Chapter 1", None, None, "This is the content of chapter 1.")

        self.assertEqual(chapter.title, "Chapter 1")
        self.assertIsNone(chapter.previous_chapter)
        self.assertIsNone(chapter.next_chapter)
        self.assertEqual(chapter.contents, "This is the content of chapter 1.")

    def test_str(self):
        chapter = Chapter("Chapter 1", None, None, "This is the content of chapter 1.")

        self.assertEqual(str(chapter), "Chapter 1")


if __name__ == "__main__":
    unittest.main()
