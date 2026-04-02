"""Auto-generated from tax_types.json."""

from supplies_contracts._choices import TextChoices


class TaxTypes(TextChoices):
    __slots__ = ()

    SIMPLIFIED_5 = "SIMPLIFIED_5", "УСН 5%"
    SIMPLE = "SIMPLE", "УСН 6%"
    SIMPLIFIED_7 = "SIMPLIFIED_7", "УСН 7%"
    SIMPLE_15 = "SIMPLE_15", "УСН 15%"
    COMMON = "COMMON", "Общая"
    AUTOMATED_8 = "AUTOMATED_8", "АУСН 8%"
    AUTOMATED_20 = "AUTOMATED_20", "АУСН 20%"
    PATENT = "PATENT", "ПСН"
