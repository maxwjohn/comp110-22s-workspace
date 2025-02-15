"""Examples of importing in Python."""



from lessons import helpers

# alIAS A MODULE / IMPORT NAME AS ANOTHER NAME
from lessons import helpers as hp

# Import names defined globaly in module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2,4))
    print(f"The answer: {helpers.THE_ANSWER}")
    print(powerful)

if __name__ == "__main__":
    main()