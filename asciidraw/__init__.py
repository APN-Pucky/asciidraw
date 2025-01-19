from warnings import warn

try:
    import colorama  # noqa: F401
    from termcolor import colored
except ImportError:
    warn(
        "colorama and termcolor are required for colored ASCII rendering", stacklevel=2
    )

    def colored(text, color):  # noqa: ARG001
        return text
