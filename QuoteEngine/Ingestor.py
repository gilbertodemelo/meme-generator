"""A module that encapsulate all ingestors."""

from .Quote import Quote
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor
from typing import List


class Ingestor(IngestorInterface):
    """A class that puts all ingestors together."""

    ingestors = [TextIngestor, DocxIngestor, PdfIngestor, CsvIngestor]

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses the input file."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)