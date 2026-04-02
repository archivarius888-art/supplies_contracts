"""Auto-generated from beneficiaries_info_mode.json."""

from supplies_contracts._choices import TextChoices


class BeneficiariesInfoMode(TextChoices):
    __slots__ = ()

    REQUIRED = "REQUIRED", "REQUIRED"
    NO_INFO = "NO_INFO", "NO_INFO"
    REFUSAL = "REFUSAL", "REFUSAL"
    SAME_AS_FOUNDERS = "SAME_AS_FOUNDERS", "SAME_AS_FOUNDERS"
