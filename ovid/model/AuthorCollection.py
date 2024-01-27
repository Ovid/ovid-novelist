class AuthorCollection:
    def __init__(self):
        """
        Initializes the AuthorCollection object with an empty list of authors.
        """
        self.authors = []

    def add_author(self, author):
        """
        Adds an Author object to the collection.

        :param author: Author - An instance of the Author class.
        """
        self.authors.append(author)

    def remove_author(self, author):
        """
        Removes an Author object from the collection.

        :param author: Author - An instance of the Author class to be removed.
        """
        self.authors.remove(author)

    def reorder_authors(self, new_order):
        """
        Reorders the authors in the collection based on the new order provided.

        :param new_order: list of Author - A list of Author objects in the desired order.
        """
        if set(new_order) == set(self.authors):
            self.authors = new_order
        else:
            raise ValueError("New order must contain the same authors as the current collection")

    def __str__(self):
        """
        String representation of the AuthorCollection object.
        """
        return "Authors in collection:\n" + "\n".join(str(author) for author in self.authors)

# Example usage
# author1 = Author("Jane Doe", email="janedoe@example.com", bio="Jane Doe is a novelist.")
# author2 = Author("John Smith", email="johnsmith@example.com", bio="John Smith is a poet.")
#
# collection = AuthorCollection()
# collection.add_author(author1)
# collection.add_author(author2)
#
# print(collection)
#
## Reorder authors
# collection.reorder_authors([author2, author1])
# print(collection)

