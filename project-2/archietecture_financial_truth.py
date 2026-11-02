def get_expense():
    """Input: returns a number, 'quit', or None if invalid."""
    raw = input("Enter expense (or 'quit'): ").strip()
    if raw.lower() == "quit":
        return "quit"
    try:
        amount = float(raw)
    except ValueError:
        print("Invalid Data")
        return None
    if amount < 0:
        print("Expense can't be negative")
        return None
    return amount


def show_total(total):
    """Output: display only, no logic."""
    print(f"FINAL TOTAL: ${total:.2f}")


def main():
    total = 0  # initialized OUTSIDE the loop so it keeps its state

    while True:
        expense = get_expense()
        if expense == "quit":
            break
        if expense is None:
            continue
        total += expense
        print(f"Running total: ${total:.2f}")

    show_total(total)


main()