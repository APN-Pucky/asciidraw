try:
    import colorama
    from termcolor import colored
except ImportError:
    warn("colorama and termcolor are required for colored ASCII rendering")

    def colored(text, color):
        return text
