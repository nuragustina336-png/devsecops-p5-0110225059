from expense_service import add_expense, total_expenses, list_expenses
from expense_utils import format_rupiah


def main():
    expenses = []
    print("=== Aplikasi Pencatat Pengeluaran ===")
    print("Masukkan nama dan nominal pengeluaran.")
    print("Kosongkan nama untuk selesai.\n")

    while True:
        name = input("Nama pengeluaran: ").strip()
        if not name:
            break

        amount_text = input("Nominal (angka rupiah): ").strip()
        try:
            amount = int(amount_text)
        except ValueError:
            print("Nominal harus berupa angka bulat.\n")
            continue

        if add_expense(expenses, name, amount):
            print("Pengeluaran berhasil dicatat.\n")
        else:
            print("Nama harus diisi dan nominal harus lebih dari 0.\n")

    print("\n=== Ringkasan Pengeluaran ===")
    if not expenses:
        print("Belum ada pengeluaran.")
    else:
        for number, expense in enumerate(list_expenses(expenses), start=1):
            print(f"{number}. {expense['name']}: {format_rupiah(expense['amount'])}")
        print(f"Total: {format_rupiah(total_expenses(expenses))}")


if __name__ == "__main__":
    main()
