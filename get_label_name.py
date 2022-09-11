import json

def get_name():
    file = open(r'data\ActivityNet\annotations.json','rb')
    data = json.load(file)
    for v,k in data.items():
        print(v)
        with open('make_anetDatasets\\video_list.txt',"a") as f:
            f.write(str(v)+'.mp4')
            f.write("\n")

if __name__ == '__main__':
    get_name()


