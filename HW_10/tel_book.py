import json
import os

field = {"id": "id: ",
         "first_name": "Имя: ",
         "last_name": "Фамилия: ",
         "phone_number": "Телефон: ",
         "birthday": "Дата рождения: ",
         "workplace": "Место работы: "}

file_db = "db.json"

#todo доделать проверку на надичие файла с БД
def get_data() -> list:
    """
    Выгружает данные из файла и возвращает словарь
    Если id существует, то возвращает только одну запись по id
    """
    with open(file_db, 'r', encoding="utf-8") as file:
        data_file = json.load(file)
    return data_file["items"]


def get_data_id(id: int) -> dict:
    """
    Возвращает только одну запись по id
    """
    with open(file_db, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['id'] == id:
                return item


def get_data_last_name(last_name: str) -> list:
    """
    Возвращает только одну запись по фамилии
    """
    res = []
    with open(file_db, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        for item in data_file['items']:
            if item['last_name'].lower() == last_name.lower():
                res.append(item)
    return res


def add_data(data: dict):
    """
    Принимает словарь с записью и добавляет в файл.
    Если в принимаемом словаре имеется поле id, тогда сначала удаляет эту запись из словаря.
    :param data:
    """
    id = data.get("id")

    with open(file_db, 'r', encoding="utf-8") as file:
        data_file = json.load(file)

    if id:
        for i, items in enumerate(data_file["items"]):
            if id == items["id"]:
                data_file["items"][i] = data
                break

    else:
        id = data_file["last_id"]["id"] + 1
        data_file["last_id"]["id"] = id
        data["id"] = id
        data_file["items"].append(data)

    with open(file_db, "w", encoding="utf-8") as file:
        json.dump(data_file, file, indent=2, ensure_ascii=False)


def create_card(data):
    res = ""
    for key in field:
        if key =="phone_number":
            res += field[key]
            for tel in data[key]:
                res += tel+" "
            res += "\n"

        else:
            res += field[key] + str(data[key]) + '\n'
    if not data:
        res = "<-Нет данных для отображения->"
    return res
