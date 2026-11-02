import math
import secrets
import string


def get_length():
    raw = input("Enter password length (min 8, 15+ recommended): ").strip()
    try:
        length = int(raw)
    except ValueError:
        print("Invalid Data")
        return None
    if length < 8:
        print("Length must be at least 8")
        return None
    if length > 128:
        print("Length must be 128 or less")
        return None
    return length


def generate_password(length, use_symbols=False):
    pool = string.ascii_letters + string.digits
    if use_symbols:
        pool += string.punctuation

    chars = [secrets.choice(string.ascii_letters), secrets.choice(string.digits)]
    chars += [secrets.choice(pool) for _ in range(length - 2)]

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars), len(pool)


def calculate_entropy(length, pool_size):
    return length * math.log2(pool_size)


def show_password(password, entropy):
    print(f"\nPassword: {password}")
    print(f"Entropy: {entropy:.1f} bits")


def main():
    length = None
    while length is None:
        length = get_length()

    choice = input("Include special characters (@, #, $)? (y/n): ").strip().lower()
    use_symbols = choice == "y"

    password, pool_size = generate_password(length, use_symbols)
    entropy = calculate_entropy(length, pool_size)
    show_password(password, entropy)


main()