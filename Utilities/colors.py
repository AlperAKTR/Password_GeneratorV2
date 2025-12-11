try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError as e:
    raise ImportError(
        "This module requires the 'colorama' package.\n"
        "Install it using: pip install colorama"
    ) from e


class Color:
    """
    Utility class for printing colored terminal messages using Colorama.

    USAGE EXAMPLES:
        Color.green("Operation completed successfully.")
        Color.red("An error occurred.")
        Color.yellow("Be careful!")
        Color.cyan("This is an informational message.")

    NOTE:
        Colorama must be installed for these methods to work.
    """

    @staticmethod
    def green(msg: str):
        """Prints a green message."""
        print(Fore.GREEN + msg + Style.RESET_ALL)

    @staticmethod
    def red(msg: str):
        """Prints a red message."""
        print(Fore.RED + msg + Style.RESET_ALL)

    @staticmethod
    def yellow(msg: str):
        """Prints a yellow message."""
        print(Fore.YELLOW + msg + Style.RESET_ALL)

    @staticmethod
    def cyan(msg: str):
        """Prints a cyan message."""
        print(Fore.CYAN + msg + Style.RESET_ALL)
