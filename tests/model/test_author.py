import unittest
from ovid.model.Author import Author

class TestAuthor(unittest.TestCase):

    def test_author_initialization(self):
        author = Author("Jane Doe", "janedoe@example.com", "Jane is a writer.")
        self.assertEqual(author.name, "Jane Doe")
        self.assertEqual(author.email, "janedoe@example.com")
        self.assertEqual(author.bio, "Jane is a writer.")

    def test_author_email_update(self):
        author = Author("John Doe")
        author.update_email("johndoe@example.com")
        self.assertEqual(author.email, "johndoe@example.com")

    def test_author_bio_update(self):
        author = Author("Emily Doe")
        author.update_bio("Emily writes poetry.")
        self.assertEqual(author.bio, "Emily writes poetry.")

    def test_author_str_representation(self):
        author = Author("Mike Doe", "mikedoe@example.com", "Mike is a novelist.")
        self.assertIn("Mike Doe", str(author))
        self.assertIn("mikedoe@example.com", str(author))
        self.assertIn("Mike is a novelist.", str(author))

if __name__ == '__main__':
    unittest.main()
