class Author:
    def __init__(self, name, email=None, bio=None):
        """
        Initializes an Author object.

        :param name: str - The name of the author.
        :param email: str, optional - The email address of the author.
        :param bio: str, optional - A brief biography of the author.
        """
        self.name = name
        self.email = email
        self.bio = bio

    def __str__(self):
        """
        String representation of the Author object.
        """
        return f"Author(Name: {self.name}, Email: {self.email}, Bio: {self.bio})"

    def update_email(self, new_email):
        """
        Updates the email address of the author.

        :param new_email: str - The new email address.
        """
        self.email = new_email

    def update_bio(self, new_bio):
        """
        Updates the biography of the author.

        :param new_bio: str - The new biography.
        """
        self.bio = new_bio
