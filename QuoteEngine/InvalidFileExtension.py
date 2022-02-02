"""A class that implements an exception on the file extension."""


class InvalidFileExtension(Exception):
    """Implementation class of the file extension exception."""

    def __init__(self, *args):
        """Constructor."""
        self.default_msg = 'The file is not valid.'
        self.input_msg = ''
        for value in args:
            self.input_msg = value

    def __repr__(self):
        """Shows the class in string format."""
        if len(self.input_msg) > 0:
            return self.input_msg
        else:
            return self.default_msg
