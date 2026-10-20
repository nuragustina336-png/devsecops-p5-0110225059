from expense_service import total_expenses
from expense_utils import format_rupiah


def create_summary(expenses):
    """Buat ringkasan jumlah item dan total pengeluaran."""
    count = len(expenses)
    total = total_expenses(expenses)
    return {
        "count": count,
        "total": total,
        "message": f"{count} transaksi, total {format_rupiah(total)}",
    }
