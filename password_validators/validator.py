"""Abstract class for validators"""
# system module
from abc import ABC, abstractmethod


class Validator(ABC):
    """Interface for validators"""
    @abstractmethod
    def __init__(self, password: str | None):
        """
        :param password:
        :type password: str | None
        """
        self.password = password
        self._strong: int = 0
        self.is_valid: bool = self._is_valid()

    @abstractmethod
    def __bool__(self):
        """Force implementing __bool__ method"""

    @abstractmethod
    def _is_valid(self) -> bool:
        """Force implementing _is_valid method"""

    @abstractmethod
    def info(self) -> str:
        """Force implementing info method"""

    @abstractmethod
    def get_strong(self) -> int:
        """Force implementing get_strong method"""
