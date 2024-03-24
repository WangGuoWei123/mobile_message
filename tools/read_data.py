import yaml

from config import BASE_DIR


def read_msg():
    # 解析txt格式文件
    # data_list = list()
    # with open(BASE_DIR+"/data/msg_data", encoding="utf-8") as f:
    #     contents = f.readlines()
    #     for data in contents:
    #         data_list.append(eval(data.strip()))
    #     return data_list
    # 解析yaml格式文件
    with open(BASE_DIR + "/data/msg_data.yml", encoding="utf-8") as f:
        data = yaml.safe_load(f)
        print(data)
        return data
