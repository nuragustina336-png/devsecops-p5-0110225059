import unittest
from expense_service import add_expense, list_expenses, total_expenses
from expense_utils import format_rupiah
from expense_report import create_summary


class TestExpenseApp(unittest.TestCase):
    def test_add_valid_expense(self):
        expenses = []
        self.assertTrue(add_expense(expenses, "Makan", 20000))
        self.assertEqual(len(expenses), 1)

    def test_reject_empty_name(self):
        expenses = []
        self.assertFalse(add_expense(expenses, "   ", 20000))
        self.assertEqual(expenses, [])

    def test_reject_zero_or_negative_amount(self):
        self.assertFalse(add_expense([], "Transport", 0))
        self.assertFalse(add_expense([], "Transport", -5000))

    def test_total_expenses(self):
        expenses = [{"name": "Makan", "amount": 20000},
                    {"name": "Transport", "amount": 10000}]
        self.assertEqual(total_expenses(expenses), 30000)

    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(30000), "Rp30.000")

    def test_create_summary(self):
        expenses = [{"name": "Makan", "amount": 20000}]
        summary = create_summary(expenses)
        self.assertEqual(summary["count"], 1)
        self.assertEqual(summary["total"], 20000)


if __name__ == "__main__":
    unittest.main()
