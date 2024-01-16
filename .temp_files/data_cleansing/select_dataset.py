import json

'''
数据集要求：
1. 时间：夜晚（night）
2. 标签：只取汽车（car）公交车（bus）卡车（truck）
'''


with open("bdd100k_labels_images_train.json", 'r', encoding='utf-8') as ft:
    train_data = json.load(ft)

with open("bdd100k_labels_images_val.json", 'r', encoding='utf-8') as fv:
    val_data = json.load(fv)


all_data = train_data + val_data
new_data = []
# del_data = []


for pic in all_data:
    if pic["attributes"]["timeofday"] == "daytime":
        new_labels = []
        for label in pic["labels"]:
            if label["category"] in ["car", "bus", "truck"]:
                new_labels.append(label)
        pic["labels"] = new_labels
        new_data.append(pic)
    # else:
    #     del_data.append(pic)


print(len(new_data))
# print(len(del_data))


# with open("del_img.txt", 'w', encoding='utf-8') as fd:
#     fd.writelines(del_data)
