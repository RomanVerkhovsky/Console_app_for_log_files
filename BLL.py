import GUI
import control

def read(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text

def read_color(path):
    text = read(path)
    text = GUI.color_text(text)
    return text

def read_log(path):
    text = read_color(path)
    text = text.replace('\n', '\n\t\t\t')
    GUI.info_event(path)
    print(f'\n'
          f'\t\t\t{text}'
          f'\n')

def find_word(path):
    text = read_color(path)
    word = GUI.input_word()
    if text.find(word) != -1:
        print('')
        text = text.split('\n')
        text_new = []
        for i in range(len(text)):
            if text[i].find(word) != -1:
                print(f'\t\t\t {GUI.yellow_word(text[i], word)}')
                text_new.append(text[i])
        print('')

    else:
        print(f'{GUI.info()} log file do not contain this word')

def filter_file(path):
    text = read_color(path)
    text = text.split('\n')
    while True:
        filter = GUI.filter_choice()
        if filter == '1':
            print('')
            for i in range(len(text)):
                if text[i].find('ERROR') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            return

        elif filter == '2':
            print('')
            for i in range(len(text)):
                if text[i].find('WARNING') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            return

        elif filter == '3':
            print('')
            for i in range(len(text)):
                if text[i].find('INFO') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            return

        else:
            print(f'{GUI.error()} You entered a number not from the list ')

# def time(path):
#    text = read_color(path)
#    text =
