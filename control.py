import GUI
import BLU
import BLL


def parsing_file(path):
    original_text = BLL.read(path)
    text = original_text
    collection = []
    collection = BLL.collection_paths(collection, path)
    info_sort = 'def'
    GUI.command_list()
    while True:
        command = GUI.input_command()
        if command == 'stop':
            return command
        elif command == 'change':
            return command
        elif command == 'reset':
            text = original_text
            info_sort = 'def'
        elif command == 'info':
            GUI.command_list()
        elif command == 'up':
            text = BLU.sort_time_up(text)
            info_sort = 'up'
            GUI.text_up()
        elif command == 'down':
            text = BLU.sort_time_down(text)
            info_sort = 'down'
            GUI.text_down()
        elif command == 'filter':
            if info_sort == 'def':
                sorted_text = original_text
                text = BLU.filter_file(sorted_text)
            elif info_sort == 'up':
                sorted_text = BLU.sort_time_up(original_text)
                text = BLU.filter_file(sorted_text)
            elif info_sort == 'down':
                sorted_text = BLU.sort_time_down(original_text)
                text = BLU.filter_file(sorted_text)
        elif command == 'read':
            BLU.read_log(text, collection)
        elif command == 'find':
            BLU.find_word(text)
        elif command == 'add':
            GUI.info_path_add()
            while True:
                path = BLU.open_log()
                if path in collection:
                    GUI.error_add(path)
                elif path == 'stop':
                    command = 'stop'
                    return command
                elif path == 'cancel':
                    GUI.info_cancel()
                    break
                else:
                    original_text = BLU.add(original_text, path)
                    text = original_text
                    collection = BLL.collection_paths(collection, path)
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
