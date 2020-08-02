from os import path
from openpyxl import load_workbook


def main():
    while True:
        title = input('Введіть назву файлу: ')
        if not path.exists(title):
            print('Введеного файлу не існує.')
            continue
        while True:
            code = input(f'Вы у файлі: "{title}"; Введіть код (щоб повернутися назад введіть 0): ')
            if code == '0':
                break
            wb = load_workbook(title, read_only=True)
            for string in wb.active:
                if string[0].value == code:
                    print(string[1].value)
                    break
            else:
                print('Знайденого коду не існує.')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
