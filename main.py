import pandas as pd
import json
import os
import openpyxl


def load_log(path):
    """
    Принимает на вход путь к файлу с журналом, десериализуем его и возвращает список отфильтрованных событий
    """
    with open('json_oktmo/{}'.format(path)) as Json_file:
        json_file = json.load(Json_file)

        df = pd.DataFrame([])
        for j in range(0, len(json_file['features'])):
            dataframe = (pd.DataFrame.from_dict(json_file['features'][j]['properties'], orient='index').T)
            df = df.append(dataframe)
        return df  # возвращаем полученный df





def main():
    # log_path = sys.argv[1]  # получаем путь к файлу журнала
    total = pd.DataFrame([])
    files = os.listdir(os.getcwd() + "/json_oktmo")  # получаем путь к файлу журнала
    print(files)
    json_file = filter(lambda x: x.endswith('.json'), files)
    for j in json_file:
        total = total.append(load_log(j))
    with pd.ExcelWriter('output.xlsx') as writer:
        total.to_excel(writer, sheet_name='Result')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
