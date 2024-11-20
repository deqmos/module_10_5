from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file.readline():
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]
start1 = datetime.now()
for file in filenames:
    read_info(file)
end1 = datetime.now()
time_of_line_function = end1 - start1
print(f'Линейный вызов : {time_of_line_function}')


if __name__ == '__main__':
    start2 = datetime.now()

    with Pool(4) as pool:
        pool.map(read_info, filenames)

    end2 = datetime.now()
    time_of_multiprocessing = end2 - start2
    print(f'Многопроцессный вызов : {time_of_multiprocessing}')
