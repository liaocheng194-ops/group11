"""Checkout calculations for the online shopping exercise."""

STUDENT_DISCOUNT_RATE = 0.10


def apply_student_discount(total: float, is_student: bool) -> float:
    """Return the total after applying the eligible student discount.

    Args:
        total: Original purchase total, in pounds.
        is_student: Whether the customer is eligible for the student discount.

    Raises:
        ValueError: If total is negative.
    """
    if total < 0:
        raise ValueError("total must be non-negative")
    if is_student:
        return round(total * (1 - STUDENT_DISCOUNT_RATE), 2)
    return round(total, 2)
