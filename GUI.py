color_red = '\033[91m'
color_blue = '\033[94m'
color_yellow = '\033[33m'
color_aqua = '\033[36m'
reset = '\033[0m'
fat = '\033[1m'
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
    return f'{aqua("   INFO:")}'

def error():
    return f'{red("  ERROR:")}'

def warning():
    return f'{yellow("WARNING:")}'

def starting_message():
    print(f'{info()} The program is starting...')

def ending():
    print(f'{info()} The program was stopped')
    input("\t\t  Press enter for exit")

def find_error():
    print(f'{error()} Log file not found, choose new file or input "stop" for exit')

def avoid_log():
    print(f'{error()} {fat_text("Log file is avoid")}')

def notfound():
    print(f'{error()} File not found')

def notcommand():
    print(f'{error()} {fat_text("WRONG COMMAND")}')

def info_event():
    print(f'{info()} The event(s) from selected log file(s):')

def command_list():
    print(f'{info()} Available commands:'
          f'\n\t\t\t'
          f'\n\t\t\tread     - view file'
          f'\n\t\t\tfilter   - change importance level to view it'
          f'\n\t\t\tfind     - input word or letter to view event with it'
          f'\n\t\t\tsort     - sort date up or down'
          f'\n\t\t\tstop     - close app'
          f'\n\t\t\tchange   - change log file'
          f'\n\t\t\tinfo     - list of available commands'
          f'\n\t\t\tadd      - add info from next log file'
          f'\n\t\t\t')

# _____________________________________________________________________________________________

# input user >>>>>>>>>>>>>
def input_path():
    path = input(f'{you()} Input path to log file or "stop" for exit >> ')
    return path

def input_command():
    com = input(f'{you()} Input command >> ')
    return com

def input_word():
    word = input(f'{you()} Input word >> ')
    return word

def filter_choice():
    print(f'{info()} Choose importance level:')
    print(f'\n\t\t\t{error()} 1'
          f'\n\t\t\t{warning()} 2'
          f'\n\t\t\t{info()} 3'
          f'\n')
    filter = input(f'{you()} Input number >> ')
    return filter
