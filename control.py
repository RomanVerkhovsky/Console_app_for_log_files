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
            while True:
                answer = GUI.yes_no()
                if answer == 'y' and answer != '':
                    return command
                elif answer == 'n' and answer != '':
                    break
        elif command == 'change':
            return command
        elif command == 'reset':
            text = original_text
            info_sort = 'def'
            GUI.info_filter()
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
            while True:
                word = GUI.input_word()
                if word != '':
                    BLU.find_word(text, word)
                    answer = GUI.find_question()
                    if answer == 'n':
                        break
                    else:
                        continue
                else:
                    GUI.info_avoid_word()
        elif command == 'add':
            GUI.info_path_add()
            while True:
                path = BLU.open_log()
                if path in collection:
                    GUI.error_add(path)
                elif path == 'stop':
                    command = 'stop'
                    while True:
                        answer = GUI.yes_no()
                        if answer == 'y' and answer != '':
                            return command
                        elif answer == 'n' and answer != '':
                            break
                elif path == 'cancel':
                    GUI.info_cancel()
                    break
                else:
                    original_text = BLU.add(original_text, path)
                    text = original_text
                    collection = BLL.collection_paths(collection, path)
                    GUI.info_add(path)
                    break
        elif command == 'del':
            if len(collection) > 1:
                while True:
                    GUI.choose_log()
                    GUI.view_collection(collection)
                    log = GUI.input_name()
                    if log != 'cancel':
                        if log in collection:
                            original_text = BLU.del_log(collection, log)
                            text = original_text
                            collection = BLL.del_collection(collection, log)
                            info_sort = 'def'
                            GUI.del_successful()
                            break
                        else:
                            GUI.not_log(log)
                    elif log == 'cancel':
                        GUI.del_cancel()
                        break
            else:
                GUI.not_del()

        else:
            GUI.not_command()


def run():
    while True:
        GUI.info_path()
        path = BLU.open_log()
        if path == 'stop':
            while True:
                answer = GUI.yes_no()
                if answer == 'y' and answer != '':
                    return
                elif answer == 'n' and answer != '':
                    break
        else:
            GUI.info_add(path)
            if parsing_file(path) == 'stop':
                return
