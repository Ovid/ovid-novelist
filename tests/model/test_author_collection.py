import unittest
from ovid.model.Author import Author
from ovid.model.AuthorCollection import AuthorCollection


class TestAuthorCollection(unittest.TestCase):
    def setUp(self):
        self.author1 = Author("Jane Doe", "janedoe@example.com", "Jane is a writer.")
        self.author2 = Author("John Smith", "johnsmith@example.com", "John is a poet.")
        self.collection = AuthorCollection()

    def test_add_author(self):
        self.collection.add_author(self.author1)
        self.assertIn(self.author1, self.collection.authors)

    def test_remove_author(self):
        self.collection.add_author(self.author1)
        self.collection.remove_author(self.author1)
        self.assertNotIn(self.author1, self.collection.authors)

    def test_reorder_authors(self):
        self.collection.add_author(self.author1)
        self.collection.add_author(self.author2)
        self.collection.reorder_authors([self.author2, self.author1])
        self.assertEqual([self.author2, self.author1], self.collection.authors)

    def test_reorder_authors_invalid_input(self):
        self.collection.add_author(self.author1)
        with self.assertRaises(ValueError):
            self.collection.reorder_authors([self.author2, self.author1])

    def test_author_collection_str(self):
        self.collection.add_author(self.author1)
        self.assertIn("Jane Doe", str(self.collection))


if __name__ == "__main__":
    unittest.main()
