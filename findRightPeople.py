import os
import json
import fnmatch
import datetime
import pickle


def FRP():
    fileList = os.listdir('Data/coros_data/jsonload/extf')
    fldFileList = fnmatch.filter(fileList, '*.xx')
    People = {}
    for fileName in fldFileList:
        try:
            with open("/usr/app/Data/coros_data/jsonload/extf/"+fileName,"r") as reader:
                work_out = json.loads(reader.read())
            people, workID = fileName.split('_')
            if people in People.keys():
                # find Mini
                if People[people][0] > datetime.datetime.strptime(work_out[0]['td'], '%Y-%m-%d %H:%M:%S'):
                    People[people][0] = datetime.datetime.strptime(work_out[0]['td'], '%Y-%m-%d %H:%M:%S')
                if People[people][0] > datetime.datetime.strptime(work_out[-1]['td'], '%Y-%m-%d %H:%M:%S'):
                    People[people][0] = datetime.datetime.strptime(work_out[-1]['td'], '%Y-%m-%d %H:%M:%S')

                # find Max
                if People[people][1] < datetime.datetime.strptime(work_out[0]['td'], '%Y-%m-%d %H:%M:%S'):
                    People[people][1] = datetime.datetime.strptime(work_out[0]['td'], '%Y-%m-%d %H:%M:%S')
                if People[people][1] < datetime.datetime.strptime(work_out[-1]['td'], '%Y-%m-%d %H:%M:%S'):
                    People[people][1] = datetime.datetime.strptime(work_out[-1]['td'], '%Y-%m-%d %H:%M:%S')
            else:
                People[people] = [datetime.datetime.strptime(work_out[0]['td'], '%Y-%m-%d %H:%M:%S'),datetime.datetime.strptime(work_out[-1]['td'], '%Y-%m-%d %H:%M:%S')]
        except:
            print(fileName)
            continue
    keys = []
    for key in People:
        if (People[key][1]-People[key][0]).days > 90:
            keys.append(key)
    print(keys)
    with open('keys.txt', 'wb') as f:
        pickle.dump(keys, f)
          

if __name__ == '__main__':
    FRP()