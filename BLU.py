import os
import BLL
import GUI
import control


def check_exist(name):
    if os.path.exists(name):
        return True
    else:
        return False

def check_command(command, text):
    if command == 'read':
        BLL.read_log(text)
    elif command == 'filter':
        BLL.filter_file(text)
    elif command == 'find':
        BLL.find_word(text)
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

def add(text):
    path = control.open_log()
    text_2 = BLL.read(path)
    text = text + '\n' + text_2
    return text
