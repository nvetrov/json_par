import pandas as pd
import json
import os


def load_log(path):
    """
    Принимает на вход путь к файлу с журналом, десериализуем его и возвращает список отфильтрованных событий
    """
    json_file = json.load(path)
    df = pd.DataFrame([])
    for j in range(0, len(json_file['features'])):
        dataframe = (pd.DataFrame.from_dict(json_file['features'][j]['properties'], orient='index').T)
        df = df.append(dataframe)
    return df  # возвращаем полученный df


lst = []


# for top, dirs, files in os.walk('C:/Users/User/PycharmProjects/pythonProject/json_oktmo'):
#     for nm in files:
# print(os.path.join(top, nm))
#         lst.append(os.path.join(nm))
#
# with open('json_file_oktmo/77oktmo.json_file') as json_file_file:
#     json_file = json_file.load(json_file_file)
#     # except AttributeError:
#     # json_file = json_file_file
#
#     df = pd.DataFrame([])
#
#     for j in range(0, len(json_file['features'])):
#         dataframe = (pd.DataFrame.from_dict(json_file['features'][j]['properties'], orient='index').T)
#         df = df.append(dataframe)
# #
# print(df)


def main():
    # log_path = sys.argv[1]  # получаем путь к файлу журнала
    files = os.listdir("3oktmo.json")  # получаем путь к файлу журнала
    print(f'files')
    # json_file = filter(lambda x: x.endswith('.json'), files)
    # print(json_file)
    # events = load_log('C:\\Users\\User\\PycharmProjects\\pythonProject\\json_oktmo')  # вызываем функцию load_log
    # print(events)


if __name__ == "_main_":
    main()
