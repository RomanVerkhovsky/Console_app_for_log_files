def choice():
    print("The program is starting")
    while True:
        path = input("Input path for log file >> ")
        if path == "stop":
            print("The program is stopped")
            break
        elif os.path.exists(path):
            file = open(path, "r")
        else:
            print("Error: file not found")

def red_text(text):
    print('\033[34m'.format(text))


def color_text(text):
    text = text.replace("ERROR", '\033[31;1mERROR\033[0m')
    text = text.replace('INFO', '\033[36;1mINFO\033[0m')
    text = text.replace('WARNING', '\033[33;1mWARNING\033[0m')
    return text


def sort_time_2(text):
    text = read_color(text)
    text = text.replace('\n', '\n\t\t\t')
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')
    print(text)
    print('')
    time = []
    for i in range(len(text)):
        time.append([])
        for j in range(2):
            time[i].append(text[i][j])
    print('\t\t\t', end='')
    for i in range(len(text)):
        for j in range(len(text[i])):
            print(text[i][j], end=' ')
        print('')
    print('')
    print('\t\t\t', end='')
    for i in range(len(time)):
        for j in range(len(time[i])):
            print(time[i][j], end=' ')
        print('')
    print('')


def sort_time(text):
    text = read_color(text)
    text = '\t\t\t' + text
    text = text.replace('\n', '\n\t\t\t')
    text = text.split('\n')
    for i in range(len(text)):
        text[i] = text[i].split(' ')
    time_date = []
    for i in range(len(text)):
        time_date.append([])
        for j in range(2):
            time_date[i].append(text[i][j])
    print('')
    for i in range(len(time_date)):
        for j in range(len(time_date[i])):
            print(time_date[i][j], end=' ')
        print('')
    print('')

    date = []
    for i in range(len(time_date)):
        date.append(time_date[i][0])

    for i in range(len(time_date)):
        date[i] = date[i].replace('.', ' ')
        date[i] = date[i].replace('\t\t\t', '')
        date[i] = date[i].split(' ')
        date[i] = date[i][::-1]
        date[i] = ''.join(date[i])

    time = []
    for i in range(len(time_date)):
        time.append(time_date[i][1])

    for i in range(len(time_date)):
        time[i] = time[i].replace(':', '')

    for i in range(len(date)):
        date[i] = date[i] + time[i]
        date[i] = int(date[i])

    for i in range(len(text)):
        text[i] = ' '.join(text[i])

    for i in range(len(sort_down(date))):
        for j in range(len(text)):
            if j == sort_down(date)[i]:
                print(text[j])
    print('')

print('')
    for i in range(len(sort_down(date_time))):
        for j in range(len(text)):
            if j == sort_down(date_time)[i]:
                print(f'\t\t\t{text[j]}')


def blue(text):
    text = f'{color_blue}{text}{reset}'
    return text

def you():
    return f'{blue("    YOU:")}'