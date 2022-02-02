"""Defines a Quote object.

This is a Python module that defines a Quote object,
which contains a text and the author of the text.
"""


class Quote:
    """The class which defines the Quote object.

    The __repr__ method is overridden
    """

    def __init__(self, text, author):
        """Construct the class."""
        self.text = text
        self.author = author

    def __repr__(self):
        """Representation of the Quote object."""
        return f'{self.text} - {self.author}'
