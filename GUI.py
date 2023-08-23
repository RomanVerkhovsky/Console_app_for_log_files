color_red = '\033[91m'
color_blue = '\033[94m'
color_yellow = '\033[33m'
color_aqua = '\033[36m'
reset = '\033[0m'
fat = '\033[1m'
ital = '\033[3m'
# _________________________________________________________________________________________

# colors          >>>>>>>>>>>>>>>>


def reset_color():
    return reset


def aqua(text):
    text = f'{color_aqua}{text}{reset}'
    return text


def yellow(text):
    text = f'{color_yellow}{text}{reset}'
    return text


def red(text):
    text = f'{color_red}{text}{reset}'
    return text


def blue(text):
    text = f'{color_blue}{text}{reset}'
    return text


def fat_text(text):
    text = f'{fat}{text}{reset}'
    return text


def ital_text(text):
    text = f'{ital}{text}{reset}'
    return text


def color_text(text):
    text = text.replace("ERROR", f'{fat_text(red("ERROR"))}')
    text = text.replace('INFO', f'{fat_text(aqua("INFO"))}')
    text = text.replace('WARNING', f'{fat_text(yellow("WARNING"))}')
    return text


def yellow_word(text, word):
    text = text.replace(word, f'{yellow(word)}')
    return text

# _________________________________________________________________________________________

# info           >>>>>>>>>>>>>>>>>


def you():
    return f'{blue("    YOU:")}'


def info():
    return f'{fat_text(aqua("   INFO:"))}'


def error():
    return f'{red("  ERROR:")}'


def warning():
    return f'{yellow("WARNING:")}'


def starting_message():
    print(f'{info()} The program is starting...')


def ending():
    print(f'{info()} The program was stopped!')
    input(f"{you()} Press enter for exit... >> ")


def find_error():
    print(f'{error()} Log file not found! Choose new file or input {blue(ital_text("stop"))} for exit')


def avoid_log():
    print(f'{error()} {fat_text("Log file is avoid!")}')


def notfound():
    print(f'{error()} {fat_text("File not found!")}')


def not_command():
    print(f'{error()} {fat_text("WRONG COMMAND!")}')


def info_event(collection: list):
    lst = []
    for i in range(len(collection)):
        lst.append(yellow(collection[i]))
    lst = ', '.join(lst)
    return print(f'{info()} The event(s) from: {lst}')


def text_up():
    print(f'{info()} {fat_text("information sort date up.")}')


def text_down():
    print(f'{info()} {fat_text("information sort date down.")}')


def info_add(path):
    print(f'{info()} {fat_text("The information from ")}{yellow(path)}{fat_text(" was successfully added!")}')


def command_list():
    print(f'{info()} Available commands:'
          f'\n\t\t\t'
          f'\n\t\t\t{blue(ital_text("read"))}     - view file'
          f'\n\t\t\t{blue(ital_text("filter"))}   - change importance level to view it'
          f'\n\t\t\t{blue(ital_text("find"))}     - input word or letter to view event with it'
          f'\n\t\t\t{blue(ital_text("stop"))}     - close app'
          f'\n\t\t\t{blue(ital_text("change"))}   - change log file'
          f'\n\t\t\t{blue(ital_text("info"))}     - list of available commands'
          f'\n\t\t\t{blue(ital_text("add"))}      - add info from next log file'
          f'\n\t\t\t{blue(ital_text("up"))}       - sort date up'
          f'\n\t\t\t{blue(ital_text("down"))}     - sort date down'
          f'\n\t\t\t{blue(ital_text("del"))}      - delete information from log file'
          f'\n\t\t\t{blue(ital_text("reset"))}    - reset filters'
          f'\n\t\t\t')


def error_add(path):
    print(f'{error()} {yellow(path)} {fat_text("has already been added! Choose another file.")}\n'
          f'         Enter {blue(ital_text("cancel"))} for cancel, {blue(ital_text("stop"))}'
          f' for exit the program.')


def info_cancel():
    print(f'{info()} {fat_text("Adding information canceled.")}')


def not_del():
    change = 'change'
    print(f'{error()} {fat_text(f"Only one file has been added!")}\n'
          f'         {fat_text(f"To change the file, use command: {blue(change)}")}')


def view_collection(collection: list):
    for i in collection:
        print(f'         {yellow(i)}')


def choose_log():
    print(f'{info()} Choose log file to delete (filters will be reset) or {blue(ital_text("cancel"))} '
          f'to cancel deleting:')


def not_log(log):
    print(f'{error()} {yellow(log)} not found in collection!')


def del_successful():
    print(f'{info()} {fat_text("Deletion was successful.")}')


def del_cancel():
    print(f'{info()} Deletion canceled.')


def info_filter():
    print(f'{info()} {fat_text("Filters was reset.")}')


def info_avoid_word():
    print(f'{error()} You do not entered information!')
# _____________________________________________________________________________________________

# input user >>>>>>>>>>>>>


def input_path():
    path = input(f'{you()} Input path to log file >> ')
    return path


def info_path_add():
    print(f'{info()} Choose log file. Filters will be reset.\n'
          f'         Or enter {blue(ital_text("stop"))} for exit the program.\n'
          f'         Enter {blue(ital_text("cancel"))} for cancel the addition.')
    return


def info_path():
    print(f'         Choose log file. Or enter {blue(ital_text("stop"))} for exit the program.')
    return


def input_command():
    com = input(f'{you()} Input command >> ')
    return com


def input_word():
    word = input(f'{you()} Input word or letter to view event with it >> ')
    return word


def filter_choice():
    print(f'{info()} Choose importance level:')
    print(f'\n\t\t\t{error()} 1'
          f'\n\t\t\t{warning()} 2'
          f'\n\t\t\t{info()} 3'
          f'\n')
    choice = input(f'{you()} Input number >> ')
    return choice


def input_name():
    name = input(f'{you()} >> ')
    return name


def yes_no():
    answer = input(f'{you()} Enter {blue(ital_text("y"))} for exit, {blue(ital_text("n"))} for cancel >> ')
    return answer


def find_question():
    question = input(f'{you()} Do you want to enter a new word to search for? ({blue(ital_text("n"))} for exit'
                     f'/another key continue) >> ')
    return question
