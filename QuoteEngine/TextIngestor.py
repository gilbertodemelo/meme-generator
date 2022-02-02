"""To ingest text files."""

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension


class TextIngestor(IngestorInterface):
    """Class that parses text files."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses a text file."""
        quotes = []
        try:
            file = open(path)
            if cls.can_ingest(path):
                with open(path, 'r') as infile:
                    file = infile.readlines()
                    for row in file:
                        print(row)
                        if row not in ('\n', '\x0c'):
                            text, author = row.split(' - ')
                            quotes.append(Quote(text.strip(), author.strip()))
                        else:
                            pass
            else:
                raise InvalidFileExtension('File extension is not .txt')
        except FileNotFoundError:
            print('The file has not been found.')

        return quotes
