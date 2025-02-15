"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 0) -> int:
    """Default parameters give more flexibility to a function."""
    # Default paramters must follow required paramaters
    return x + y


print(1)
print(add(1, 2))
print(add(1, 2, 3))