from os import system, getlogin, name
from platform import node

class term():
    def __init__(self, *arg):
        for title in arg:
            if name == 'win32':
                system(f'title {title}')
            elif name == 'linux' or name == 'linux2':
                system(f'gnome-terminal --title={title}')
            elif name == 'darwin':
                system(f'echo -n -e "\033]0;{title}\007"')
        while True:
            command = input(f"{getlogin}@{node}: ")
            system(command)
            if command == "exit" or command == "quit":
                break