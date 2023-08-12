import BLL
import GUI


# check file and open log file
def open_log():
    while True:
        log_name = GUI.input_path()
        if BLL.check_exist(log_name):
            if BLL.check_log(log_name):
                return log_name
            else:
                GUI.avoid_log()
        elif log_name == 'stop':
            return log_name
        elif log_name == 'cancel':
            return log_name
        else:
            GUI.notfound()


# reading log file
def read_log(text, collection: list):
    text = BLL.read_color(text)
    text = text.replace('\n', '\n\t\t\t')
    GUI.info_event(collection)
    print('')
    print(f'\t\t\t{text}')
    print('')


# add information from next log file
def add(original_text, path):
    text_2 = BLL.read(path)
    original_text = original_text + '\n' + text_2
    return original_text


# sort date up
def sort_time_up(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')

    date = []
    for i in range(len(text)):
        date.append(text[i][0])

    for i in range(len(text)):
        date[i] = date[i].replace('.', ' ')
        date[i] = date[i].split(' ')
        date[i] = date[i][::-1]
        date[i] = ''.join(date[i])

    time = []
    for i in range(len(text)):
        time.append(text[i][1])

    for i in range(len(text)):
        time[i] = time[i].replace(':', '')

    date_time = []
    for i in range(len(date)):
        number = date[i] + time[i]
        number = int(number)
        date_time.append(number)

    for i in range(len(text)):
        text[i] = ' '.join(text[i])

    text_sorted = []
    for i in range(len(BLL.sort_index_up(date_time))):
        for j in range(len(text)):
            if j == BLL.sort_index_up(date_time)[i]:
                text_sorted.append(text[j])

    text = '\n'.join(text_sorted)
    return text


# sort date down
def sort_time_down(text):
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')

    date = []
    for i in range(len(text)):
        date.append(text[i][0])

    for i in range(len(text)):
        date[i] = date[i].replace('.', ' ')
        date[i] = date[i].split(' ')
        date[i] = date[i][::-1]
        date[i] = ''.join(date[i])

    time = []
    for i in range(len(text)):
        time.append(text[i][1])

    for i in range(len(text)):
        time[i] = time[i].replace(':', '')

    date_time = []
    for i in range(len(date)):
        number = date[i] + time[i]
        number = int(number)
        date_time.append(number)

    for i in range(len(text)):
        text[i] = ' '.join(text[i])

    text_sorted = []
    for i in range(len(BLL.sort_index_down(date_time))):
        for j in range(len(text)):
            if j == BLL.sort_index_down(date_time)[i]:
                text_sorted.append(text[j])

    text = '\n'.join(text_sorted)
    return text


# change importance level to view it
def filter_file(text):
    text = BLL.read_color(text)
    text = text.split('\n')

    while True:
        choice = GUI.filter_choice()
        if choice == '1':
            new_text = ''
            for i in range(len(text)):
                if text[i].find('ERROR') != -1:
                    new_text += text[i] + '\n'
            print('')
            for i in range(len(text)):
                if text[i].find('ERROR') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            text = new_text[:-1]
            return text

        elif choice == '2':
            new_text = ''
            for i in range(len(text)):
                if text[i].find('WARNING') != -1:
                    new_text += text[i] + '\n'
            print('')
            for i in range(len(text)):
                if text[i].find('WARNING') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            text = new_text[:-1]
            return text

        elif choice == '3':
            new_text = ''
            for i in range(len(text)):
                if text[i].find('INFO') != -1:
                    new_text += text[i] + '\n'
            print('')
            for i in range(len(text)):
                if text[i].find('INFO') != -1:
                    print(f'\t\t\t {text[i]}')
            print('')
            text = new_text[:-1]
            return text

        else:
            print(f'{GUI.error()} You entered a number not from the list ')


# search entered information in log file
def find_word(text):
    text = BLL.read_color(text)
    word = GUI.input_word()
    if text.find(word) != -1 and word != '':
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
