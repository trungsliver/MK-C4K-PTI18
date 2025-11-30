import json


def load_json_data():
    """
    Đọc dữ liệu (READ)
    """
    anime_dict_data = list()
    with open("data/data.json", "r") as json_in:
        json_data = json.load(json_in)
    anime_dict_data.extend(json_data)
    return anime_dict_data

def write_json_data(json_data):
    """
    Viết dữ liệu (WRITE)
    """
    with open("data/data.json", "w") as json_out:
        json.dump(json_data, json_out)
     