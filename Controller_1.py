# Nhập các thư viện cần thiết
import json
from array import array
from builtins import print, map, format
from operator import index

from numpy import nan
from numpy.core._multiarray_tests import npy_sinhf
from scipy.constants import value

from Impact import Impact

# đối tượng cảm xúc
class Emotion:
    pleasure = 0.75
    surprise = 0.5
    anger = -0.2
    fear = -0.2
    hate = -0.4
    sad = -0.4
    def getLstEmotion(self):
        return [self.pleasure, self.surprise, self.anger, self.fear, self.hate, self.sad]

#tính các N ( số người them nhóm )
nChildren = nALKW = nBFGMEN = nElder = nBlinder = nOther = 0

with open("Pedestrians.json", 'r') as file:
    data = json.load(file)

# for obj_Pedestrian in data:
#     age = obj_Pedestrian["age"]
#     if age < 12:
#         nChildren += 1
#     if age > 60:
#         nElder += 1
#     if 12 < age < 60:
#         nOther += 1
#     velocity = obj_Pedestrian["velocity"]
#     if velocity == 0.52:
#         nBlinder += 1
#     start = obj_Pedestrian["wardDistribution"]
#     if start == "A" or start == "L" or start == "K" or start == "W":
#         nALKW += 1
#     if start == "B" or start == "F" or start == "M" or start == "G" or start == "E" or start == "N":
#         nBFGMEN += 1
# đọc lấy impactOfAGV
def read_json_file():
    # Đường dẫn tới tệp JSON cần đọc
    file_path = 'input.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data["impactOfAGV"]["distribution"]

def impactToChildren(n):
    data = read_json_file()["children"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactChildren = Impact(n, k, min, max)
    return impactChildren.getImpact()

def impactToALKW(n):
    data = read_json_file()["ALKW"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactALKW = Impact(n, k, min, max)
    return impactALKW.getImpact()

def impactToBFGMEN(n):
    data = read_json_file()["BFGMEN"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBFGMEN = Impact(n, k, min, max)
    return impactBFGMEN.getImpact()

def impactToElder(n):
    data = read_json_file()["Elder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBFGMEN = Impact(n, k, min, max)
    return impactBFGMEN.getImpact()

def impactToBlinder(n):
    data = read_json_file()["Blinder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBlinder = Impact(n, k, min, max)
    return impactBlinder.getImpact()

def impactToOthers(n):
    data = read_json_file()["Other"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactOthers = Impact(n, k, min, max)
    return impactOthers.getImpact()

# # tạo obj emotion lấy giá trị cảm xúc gần nhất
# ex1 = Emotion()
# closest_value = find_closest_value(0.1, ex1.getLstEmotion())
# print("Giá trị gần nhất là:", closest_value)

# # tạo các giá trị ngẩu nhiên
# impactToChildren(nChildren)
# impactToALKW(nALKW)
# impactToBFGMEN(nBFGMEN)
# impactToOthers(nOther)
# impactToElder(nElder)
# impactToBlinder(nBlinder)

# tạo mảng 2 chiều 6*N với N là số lượng Pedestrian theo đối tượng
array_2d = [[0 for _ in range(allpedestrian)] for _ in range(6)]

with open("Pedestrians.json", 'r') as file:
    data = json.load(file)

for person in data:

	#Khởi tạo mảng impactOfAGV cho person là mảng 2 chiều có 6x1 phần tử
	#Gán các giá trị 0 cho mảng impactOfAGV
    impactOfAGV = [[0] for _ in range(6)]

    age = person["age"]
    if age < 12:
        person.impactOfAGV[:0] += impactToChildren [:0] 
        #cộng cột của impactOfAGV với cột đầu tiên của impactToChildren 
        impactToChildren = np.delete(impactToChildren, 0, axis=1)
    elif start == "A" or start == "L" or start == "K" or start == "W":
	        person.impactOfAGV[:0] += impactToALKW [:0] 
            #cộng cột của impactOfAGV với cột đầu tiên của impactToALKW 
            impactToALKW = np.delete(impactToALKW, 0, axis=1)
    elif start == "B" or start == "F" or start == "M" or start == "G" or start == "E" or start == "N":
            person.impactOfAGV[:0] += impactToBFGMEN [:0] 
            #cộng cột của impactOfAGV với cột đầu tiên của impactToBFGMEN 
            impactToBFGMEN = np.delete(impactToBFGMEN, 0, axis=1)
    elif age > 60:
	        person.impactOfAGV[:0] += impactToElder [:0] 
            #cộng cột của impactOfAGV với cột đầu tiên của impactToElder 
            impactToElder = np.delete(impactToElder, 0, axis=1)
    elif velocity == 0.52:
            person.impactOfAGV[:0] += impactToBlinder [:0] 
            #cộng cột của impactOfAGV với cột đầu tiên của impactToBlinder 
            impactToBlinder = np.delete(impactToBlinder, 0, axis=1)
    else:
        person.impactOfAGV[:0] = impactToOthers [:0] 
        #cộng cột của impactOfAGV với cột đầu tiên của impactToOthers 
        impactToOthers = np.delete(impactToOthers, 0, axis=1)
    
    # Cộng mảng impactofAGV vào mảng 6*n
    for j in range(len(impactofAGV)):
        array_2d[j][i - 1] += impactofAGV[j][0]

# Output
for row in array_2d:
    print(row)

# arr = impactToChildren(100)
# nPleasure = nSurprise = nAnger = nFear = nHate = nSad = 0
# for i in range(len(arr)):
#    if arr[i] > 0.75:
#        nPleasure += 1
#    if arr[i] > 0.5 and arr[i] < 0.75:
#        nSurprise += 1
#    if arr[i] > 0 and arr[i] < 0.5:
#        nAnger += 1
#    if arr[i] > -0.2 and arr[i] < 0:
#        nFear += 1
#    if arr[i] > -0.4 and arr[i] < -0.2:
#        nHate += 1
#    if arr[i] < -0.4:
#        nSad += 1
#print(nPleasure, nSurprise, nAnger, nFear, nHate, nSad)


