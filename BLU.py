import os
import BLL
import GUI


def check_exist(name):
    if os.path.exists(name):
        return True
    else:
        return False

def check_command(command, path):
    if command == 'read':
        BLL.read_log(path)
    elif command == 'filter':
        BLL.filter_file(path)
    elif command == 'find':
        BLL.find_word(path)
    else:
        GUI.notcommand()

def check_log(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    if (text.find('INFO') or text.find('WARNING') or text.find('ERROR')) != -1:
        return True
    else:
        return False
