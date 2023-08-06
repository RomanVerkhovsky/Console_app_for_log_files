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


def sort_time(text):
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
