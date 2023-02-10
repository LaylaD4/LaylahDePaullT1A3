'''Python library that allows you to calculate the size the terminal.'''
import shutil

'''Centres output in terminal'''
def print_centre(object):
    print(object.center(shutil.get_terminal_size().columns))