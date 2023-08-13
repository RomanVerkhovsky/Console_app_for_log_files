import GUI
import os


# check path
def check_exist(name):
    if os.path.exists(name):
        return True
    else:
        return False


# check log file
def check_log(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    if (text.find('INFO') or text.find('WARNING') or text.find('ERROR')) != -1:
        return True
    else:
        return False


# read text from file
def read(path):
    file = open(path, 'r')
    text = file.read()
    file.close()
    return text


# text in color
def read_color(text):
    text = GUI.color_text(text)
    return text


# adding path in collection of paths
def collection_paths(collection: list, path):
    collection.append(path)
    return collection


# analysis of numerical data and output of a list of indexes in ascending order
def sort_index_up(date: list):
    lst_max = []
    sort_index = []
    max_num = date[0]
    max_index = 0
    for k in range(len(date) - 1):
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
    for i in range(len(date)):
        if i not in sort_index:
            sort_index.append(i)
    return sort_index


# analysis of numerical data and output of a list of indexes in descending order
def sort_index_down(date: list):
    lst_min = []
    sort_index = []
    min_num = date[0]
    min_index = 0
    for k in range(len(date) - 1):
        for i in range(len(date)):
            if date[i] not in lst_min:
                min_num = date[i]
                min_index = i

        for i in range(len(date)):
            if date[i] < min_num and i not in sort_index:
                min_num = date[i]
                min_index = i
        lst_min.append(min_num)
        sort_index.append(min_index)
    for i in range(len(date)):
        if i not in sort_index:
            sort_index.append(i)
    return sort_index


def avoid_str(text):
    text = text.split('\n')
    text_new = []
    for i in text:
        if i != '':
            text_new.append(i)
    text_new = '\n'.join(text_new)
    return text_new


def del_collection(collection: list, log):
    new_collection = []
    for i in collection:
        if i != log:
            new_collection.append(i)
    return new_collection

