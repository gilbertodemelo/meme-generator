"""To ingest PDF files."""

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from typing import List
from .InvalidFileExtension import InvalidFileExtension
from subprocess import call


class PdfIngestor(IngestorInterface):
    """Class that parses PDF files."""

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses a pdf file."""
        quotes = []
        try:
            file = open(path)
            if cls.can_ingest(path):
                txt_from_pdf = 'text.txt'
                pdf_to_txt = call(['pdftotext', '-simple', path, txt_from_pdf])
                with open(txt_from_pdf, 'r') as infile:
                    file = infile.readlines()
                    for row in file:
                        if row not in ('\n', '\x0c'):
                            text, author = row.split(' - ')
                            quotes.append(Quote(text.strip(), author.strip()))
                        else:
                            pass
            else:
                raise InvalidFileExtension('The file extension is not .pdf')
        except FileNotFoundError:
            print('The file has not been found.')

        return quotes