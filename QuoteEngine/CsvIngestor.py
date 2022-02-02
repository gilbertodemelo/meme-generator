"""To ingest csv files."""

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from csv import reader


class CsvIngestor(IngestorInterface):
    """Class that parses CSV files."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses a CSV file."""
        quotes = []
        try:
            file = open(path)
            if cls.can_ingest(path):
                with open(path, 'r') as infile:
                    file = reader(infile)
                    for row in file:
                        if len(row) > 0:
                            text, author = row[0], row[1]
                            quotes.append(Quote(text.strip(), author.strip()))
                        else:
                            pass
            else:
                raise InvalidFileExtension('The file extension is not .csv')
        except FileNotFoundError:
            print('The file has not been found.')

        return quotes
