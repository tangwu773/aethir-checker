import pandas as pd

# Функция для чтения адресов из файла
def read_addresses_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Функция для чтения данных из Excel
def read_data_from_excel(excel_file, sheet_name):
    df = pd.read_excel(excel_file, sheet_name=sheet_name)
    return df

# Функция для проверки токенов
def check_tokens(dataframe, addresses):
    # Создаем словарь для быстрого поиска по адресам
    token_dict = dataframe.set_index('a')['b'].to_dict()

    total_tokens = 0
    results = []

    for address in addresses:
        tokens = token_dict.get(address, 0)
        results.append((address, tokens))
        total_tokens += int(tokens)

    return results, total_tokens

# Основная функция
def main():
    # Путь к файлу с адресами
    file_path = 'addresses.txt'
    # Путь к Excel файлу и название листа
    excel_file = 'data.xlsx'
    sheet_name = 'Sheet1'

    # Чтение адресов из файла
    addresses = read_addresses_from_file(file_path)

    # Чтение данных из Excel
    df = read_data_from_excel(excel_file, sheet_name)

    # Проверка токенов
    results, total_tokens = check_tokens(df, addresses)

    # Вывод результатов
    for address, tokens:
        print(f'{address} : {tokens}')
    print(f'Общее количество токенов: {total_tokens}')

if __name__ == '__main__':
    main()
