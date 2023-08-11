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
        elif command == 'change':
            return command
        elif command == 'reset':
            text = original_text
        elif command == 'info':
            GUI.command_list()
        elif command == 'up':
            text = BLU.sort_time_up(text)
            GUI.text_up()
        elif command == 'down':
            text = BLU.sort_time_down(text)
            GUI.text_down()
        elif command == 'filter':
            text = BLU.filter_file(text)
        elif command == 'read':
            BLU.read_log(text, collection)
        elif command == 'find':
            BLU.find_word(text)
        elif command == 'add':
            while True:
                GUI.info_path_add()
                path = BLU.open_log()
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
        else:
            GUI.not_command()


def run():
    while True:
        GUI.info_path()
        path = BLU.open_log()
        if path == 'stop':
            return
        elif path != 'change':
            GUI.info_add(path)
            if parsing_file(path) == 'stop':
                return
