import unittest

from checkout import apply_student_discount


class StudentDiscountTests(unittest.TestCase):
    def test_student_receives_ten_percent_discount(self):
        self.assertEqual(apply_student_discount(100, True), 90)

    def test_non_student_pays_original_total(self):
        self.assertEqual(apply_student_discount(100, False), 100)

    def test_discount_rounds_to_two_decimal_places(self):
        self.assertEqual(apply_student_discount(19.99, True), 17.99)

    def test_negative_total_is_rejected(self):
        with self.assertRaises(ValueError):
            apply_student_discount(-1, True)


if __name__ == "__main__":
    unittest.main()
