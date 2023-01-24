
def write_data(data):
    with open('log.txt', 'a', encoding='utf=8') as file:
        file.write(data + '\n')
