import json

def get_name():
    file = open(r'data\ActivityNet\annotations.json','rb')
    data = json.load(file)
    Label_list = []
    for k,v in data.items():
        annotations = v['annotations']
        for label in annotations:
            label = label['label']
            Label_list.append(label)

    Label_list = set(Label_list)
    for i in Label_list:
        with open('make_anetDatasets\\action_name.csv', "a") as f:
            f.write(i + '\n')

if __name__ == '__main__':
    get_name()


