def format_rupiah(amount):
    """Format angka sebagai nominal rupiah sederhana."""
    return f"Rp{amount:,}".replace(",", ".")
