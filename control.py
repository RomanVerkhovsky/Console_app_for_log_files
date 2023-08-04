import GUI
import BLU
import BLL

def parsing_file(path):
    GUI.command_list()
    text = BLL.read(path)
    while True:
        command = GUI.input_command()
        if command == 'stop':
            return command
        elif command == 'change':
            break
        elif command == 'info':
            GUI.command_list()
        elif command == 'add':
            text = BLU.add(text)
        else:
            BLU.check_command(command, text)

def open_log():
    while True:
        log_name = GUI.input_path()
        if BLU.check_exist(log_name):
            if BLU.check_log(log_name):
                return log_name
            else:
                log_name = 'change'
                GUI.avoid_log()
                return log_name
        elif log_name == 'stop':
            return log_name
        else:
            GUI.notfound()
#        elif non_exist(log_name) == 'stop':
#            return log_name

#def non_exist(name):
#    GUI.find_error()
#    while True:
#        command = GUI.input_path()




def run():
    while True:
        path = open_log()
        if path == 'stop':
            return
        elif path != 'change':
            if parsing_file(path) == 'stop':
                return
