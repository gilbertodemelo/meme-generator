"""This abstract class has the objective of creating a standardized
way to parse different type of text file."""

from .Quote import Quote
from abc import ABC, abstractmethod
from typing import List


class IngestorInterface(ABC):
    """Class for parsing text files.

    It uses two methods to verifty the type of file and
    to parse the text.
    """

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine a file extension."""
        extension = path.split('.')[-1].lower()
        if __name__ == '__main__':
            return extension in cls.allowed_extensions


    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        """Parses the content of the file."""
        pass
