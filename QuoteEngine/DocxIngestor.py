"""To ingest docx files."""

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from docx import Document


class DocxIngestor(IngestorInterface):
    """Class that parses docx files."""

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses a docx file."""
        quotes = []
        try:
            file = open(path)
            if cls.can_ingest(path):
                infile = Document(path)
                for row in infile.paragraphs:
                    if len(row.text) > 0:
                        text, author = row.text.split('-')
                        quotes.append(Quote(text.strip(), author.strip()))
                    else:
                        pass
            else:
                raise InvalidFileExtension('The file extension is not .docx')
        except FileNotFoundError:
            print('The file has not been found.')

        return quotes