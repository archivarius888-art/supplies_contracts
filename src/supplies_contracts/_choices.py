from __future__ import annotations

from enum import StrEnum
from typing import ClassVar, Self


class TextChoices(StrEnum):
    label: str
    choices: ClassVar[tuple[tuple[str, str], ...]]
    TITLE_BY_CODE: ClassVar[dict[str, str]]

    def __new__(cls, value: str, label: str) -> Self:
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        return obj

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def __init_subclass__(cls, **kwargs: object) -> None:
        super().__init_subclass__(**kwargs)
        cls.choices = tuple((item.value, item.label) for item in cls)
        cls.TITLE_BY_CODE = {item.value: item.label for item in cls}
