import GUI
import control

def sort_down(date: list):
    lst_max = []
    sort_index = []
    max_num = date[0]
    max_index = 0
    for k in range(len(date)):
        for i in range(len(date)):
            if date[i] not in lst_max:
                max_num = date[i]
                max_index = i

        for i in range(len(date)):
            if date[i] > max_num and i not in sort_index:
                max_num = date[i]
                max_index = i
        lst_max.append(max_num)
        sort_index.append(max_index)
    return lst_max

def read(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text

def read_color(text):
    text = GUI.color_text(text)
    return text

def read_log(text):
    text = read_color(text)
    text = text.replace('\n', '\n\t\t\t')
    GUI.info_event()
    print('')
    print(f'\t\t\t{text}')
    print('')

def find_word(text):
    text = read_color(text)
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

def filter_file(text):
    text = read_color(text)
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


def sort_time(text):
    text = read_color(text)
    text = text.replace('\n', '\n\t\t\t')
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')
    time = []
    for i in range(len(text)):
        time.append([])
        for j in range(2):
            time[i].append(text[i][j])
    print('')
    print('\t\t\t', end='')
    for i in range(len(time)):
        for j in range(len(time[i])):
            print(time[i][j], end=' ')
        print('')
    print('')

    date = []
    for i in range(len(time)):
        date.append(time[i][0])

    for i in range(len(date)):
        date[i] = date[i].replace('.', ' ')
        date[i] = date[i].replace('\t\t\t', '')
        date[i] = date[i].split(' ')
        date[i] = date[i][::-1]
        date[i] = ''.join(date[i])
        date[i] = int(date[i])

    print(date)
    print(sort_down(date))
