import time
import random
import connector


def fuzzifier(value):
    v = int(value)
    classes = ['thin', 'normal', 'thick', 'very thick']
    class1 = random.uniform(0, min(1, max(0, 1.5 - v)))
    class2 = random.uniform(0, min(min(max(-1.5 + v, 0), 1), max(min(5.5 - v, 1), 0)))
    class3 = random.uniform(0, min(min(max(-4.5 + v, 0), 1), max(min(8.5 - v, 1), 0)))
    class4 = random.uniform(0, min(max(-7.5 + v, 0), 1))
    winner = max(class1, class2, class3, class4)
    if winner == class1:
        return classes[0]
    elif winner == class2:
        return classes[1]
    elif winner == class3:
        return classes[2]
    else:
        return classes[3]


def main():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentials = 'breast-cancer-dataset-credentials.json'

    worksheet = connector.connect(scope=scope, credentials=credentials).open('breast-cancer-dataset').sheet1

    all_records = worksheet.get_all_values()
    headers = all_records[0]

    worksheet.update_cell(1, len(all_records[0]), 'clump_thickness_cat2')
    for row, data in enumerate(all_records[1:]):
        worksheet.update_cell(row + 2, len(data), fuzzifier(value=data[headers.index('clump_thickness')]))
        time.sleep(1)


if __name__ == '__main__':
    main()
