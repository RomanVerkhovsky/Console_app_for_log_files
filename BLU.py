import os
import BLL
import GUI
import control


def check_exist(name):
    if os.path.exists(name):
        return True
    else:
        return False


def check_command(command, text, collection):
    if command == 'read':
        BLL.read_log(text, collection)
        return True
    elif command == 'find':
        BLL.find_word(text)
        return True
    else:
        return False


def check_log(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    if (text.find('INFO') or text.find('WARNING') or text.find('ERROR')) != -1:
        return True
    else:
        return False


def add(original_text, path):
    text_2 = BLL.read(path)
    original_text = original_text + '\n' + text_2
    return original_text
