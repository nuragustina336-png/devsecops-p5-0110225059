def add_expense(expenses, name, amount):
    """Tambahkan pengeluaran jika nama dan nominal valid."""
    cleaned_name = name.strip() if isinstance(name, str) else ""
    if not cleaned_name or not isinstance(amount, int) or amount <= 0:
        return False

    expenses.append({"name": cleaned_name, "amount": amount})
    return True


def list_expenses(expenses):
    """Kembalikan salinan daftar pengeluaran."""
    return list(expenses)


def total_expenses(expenses):
    """Hitung total seluruh nominal pengeluaran."""
    return sum(item["amount"] for item in expenses)
