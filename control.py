import GUI
import BLU
import BLL

def parsing_file(path):
    origin_text = BLL.read(path)
    text = BLL.sort_time(origin_text)
    GUI.command_list()
    while True:
        command = GUI.input_command()
        if command == 'stop':
            return command
        elif command == 'change':
            break
        elif command == 'info':
            GUI.command_list()
        elif command == 'add':
            origin_text = BLU.add(origin_text)
            if text == 'stop':
                command = 'stop'
                return command
        else:
            BLU.check_command(command, text)

def open_log():
    while True:
        log_name = GUI.input_path()
        if BLU.check_exist(log_name):
            if BLU.check_log(log_name):
                return log_name
            else:
                GUI.avoid_log()
        elif log_name == 'stop':
            return log_name
        else:
            GUI.notfound()

def run():
    while True:
        path = open_log()
        if path == 'stop':
            return
        elif path != 'change':
            if parsing_file(path) == 'stop':
                return
