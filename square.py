
def square(n: float) -> float:
    """Return the square of a number."""
    return n * n

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            value = float(sys.argv[1])
            print(square(value))
        except ValueError:
            print("Please provide a numeric value.")
    else:
        print("Usage: python square.py <number>")
