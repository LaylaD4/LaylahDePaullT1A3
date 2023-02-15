# Python library that allows you to calculate the size the terminal.
import shutil


def print_centre(object):
    """Centres output in terminal
    
    :param object: object that is to be printed in centre of terminal.
    """
    print(object.center(shutil.get_terminal_size().columns))