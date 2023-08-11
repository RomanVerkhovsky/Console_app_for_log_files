import GUI
import BLU
import BLL


def parsing_file(path):
    original_text = BLL.read(path)
    text = original_text
    collection = []
    collection = GUI.collection_paths(collection, path)
    GUI.command_list()
    while True:
        command = GUI.input_command()
        if command == 'stop':
            return command
        elif command == 'reset':
            text = original_text
        elif command == 'change':
            return command
        elif command == 'info':
            GUI.command_list()
        elif command == 'filter':
            text = BLL.filter_file(text)
        elif command == 'add':
            while True:
                GUI.info_path_add()
                path = open_log()
                if path in collection:
                    GUI.error_add(path)
                elif path == 'stop':
                    command = 'stop'
                    return command
                elif path == 'cancel':
                    break
                else:
                    original_text = BLU.add(original_text, path)
                    text = original_text
                    collection = GUI.collection_paths(collection, path)
                    GUI.info_add(path)
                    break
        elif command == 'up':
            text = BLL.sort_time_up(text)
            GUI.text_up()
        elif command == 'down':
            text = BLL.sort_time_down(text)
            GUI.text_down()
        else:
            if not BLU.check_command(command, text, collection):
                GUI.not_command()


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
        elif log_name == 'cancel':
            return log_name
        else:
            GUI.notfound()


def run():
    while True:
        GUI.info_path()
        path = open_log()
        if path == 'stop':
            return
        elif path != 'change':
            GUI.info_add(path)
            if parsing_file(path) == 'stop':
                return
