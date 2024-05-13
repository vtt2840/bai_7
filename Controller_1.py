import json
import numpy as np
from builtins import print
from Impact import Impact

# đối tượng cảm xúc
#class Emotion:
#    pleasure = 0.75
#    surprise = 0.5
#    anger = -0.2
#    fear = -0.2
#    hate = -0.4
#    sad = -0.4
#    def getLstEmotion(self):
#        return [self.pleasure, self.surprise, self.anger, self.fear, self.hate, self.sad]

#tính số người theo nhóm
nChildren = nALKW = nBFGMEN = nElder = nBlinder = nOther = 0

with open("pedestrians.json", 'r') as file:
    data = json.load(file)

for obj_Pedestrian in data:
    age = obj_Pedestrian["age"]
    if age < 12:
        nChildren += 1
    if age > 60:
        nElder += 1
    if 12 <= age <= 60:
        nOther += 1
    velocity = obj_Pedestrian["velocity"]
    if velocity == 0.52:
        nBlinder += 1
        nOther -= 1
    start = obj_Pedestrian["wardDistribution"]
    if start == "A" or start == "L" or start == "K" or start == "W":
        nALKW += 1
        nOther -= 1
    if start == "B" or start == "F" or start == "M" or start == "G" or start == "E" or start == "N":
        nBFGMEN += 1
        nOther -= 1

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
    return (-1)*impactBFGMEN.getImpact()

def impactToElder(n):
    data = read_json_file()["Elder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBFGMEN = Impact(n, k, min, max)
    return (-1)*impactBFGMEN.getImpact()

def impactToBlinder(n):
    data = read_json_file()["Blinder"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactBlinder = Impact(n, k, min, max)
    return (-1)*impactBlinder.getImpact()

def impactToOthers(n):
    data = read_json_file()["Other"]
    k = data["numberOfValues"]
    min = data["minValue"]
    max = data["maxValue"]
    impactOthers = Impact(n, k, min, max)
    return impactOthers.getImpact()

# tạo obj emotion lấy giá trị cảm xúc gần nhất
#def find_closest_value(target, lst):
#    return min(lst, key=lambda x: abs(x - target))
#ex1 = Emotion()
#closest_value = find_closest_value(0.1, ex1.getLstEmotion())

impactToChildren(nChildren)
impactToALKW(nALKW)
impactToBFGMEN(nBFGMEN)
impactToOthers(nOther)
impactToElder(nElder)
impactToBlinder(nBlinder)


# Đọc dữ liệu từ file input.json
with open('input.json') as f:
    data = json.load(f)

# Lấy giá trị của trường numOfAgents từ file input.json
allpedestrian = data['numOfAgents']['value']

# tạo mảng 2 chiều 6*N với N là số lượng Pedestrian theo đối tượng
array_2d = [[0 for _ in range(allpedestrian)] for _ in range(6)]

with open("pedestrians.json", 'r') as file:
    data = json.load(file)

for person in data:
	#Khởi tạo mảng impactOfAGV cho person là mảng 2 chiều có 6x1 phần tử
	#Gán các giá trị 0 cho mảng impactOfAGV
    impactOfAGV = [[0] for _ in range(6)]

    age = person["age"]
    start = person["wardDistribution"]
    velocity = person["velocity"]
    if age < 12:
        person.impactOfAGV[:0] += impactToChildren [:0] 
        #cộng cột của impactOfAGV với cột đầu tiên của impactToChildren 
        impactToChildren = np.delete(impactToChildren, 0, axis=1)
    else:
        if start == "A" or start == "L" or start == "K" or start == "W":
            person.impactOfAGV[:0] += impactToALKW[:0]
            impactToALKW = np.delete(impactToALKW, 0, axis = 1)
        else: 
            if start == "B" or start == "F" or start == "M" or start == "G" or start == "E" or start == "N":
                person.impactOfAGV[:0] += impactToBFGMEN[:0]
                impactToBFGMEN = np.delete(impactToBFGMEN, 0, axis = 1)
            else:
                if age > 60:
                    person.impactOfAGV[:0] +=impactToElder[:0]
                    impactToElder = np.delete(impactToElder, 0, axis = 1)
                else:
                    person.impactOfAGV[:0] = impactToOthers[:0]
                    impactToOthers = np.delete(impactToOthers, 0, axis = 1)

    # Cộng mảng impactofAGV vào từng cột của mảng 6*n
    for i in range(array_2d.shape[1]):
        array_2d[:, i] += impactOfAGV[:, 0]

# Output
for row in array_2d:
    print(row)

#Đánh giá
def positive_impact(impact_array, t):
    count = 0  # Biến đếm số lượng có giá trị cảm xúc tích cực từ AGV
    for impact_values in impact_array:
        for impact_value in impact_values:
            if impact_value > t:
                count += 1

    percent = (count / (6 * len(impact_array))) * 100
    return percent

# Kiểm tra xem đa số các trẻ em có chịu tác động tích cực từ AGV hay không với ngưỡng 0.75
perC = positive_impact(impactToChildren(nChildren), 0.75)
if perC > 50:
    print("Đa số các trẻ em chịu tác động tích cực từ AGV.")
else:
    print("Đa số các trẻ em không chịu tác động tích cực từ AGV.")

# Kiểm tra xem đa số người đến khoa viện ALKW  có chịu tác động tích cực từ AGV hay không với ngưỡng 0.75
perA = positive_impact(impactToALKW, 0.75)
if perA > 50:
    print("Đa số người đến khoa viện ALKW chịu tác động tích cực từ AGV.")
else:
    print("Đa số người đến khoa viện ALKW không chịu tác động tích cực từ AGV.")

# Kiểm tra xem đa số người cao tuổi có chịu tác động tích cực từ AGV hay không với ngưỡng 0.4
perE = positive_impact(impactToElder, 0.4)
if perE > 50:
    print("Đa số người cao tuổi chịu tác động tiêu cực từ AGV.")
else:
    print("Đa số người cao tuổi không chịu tác động tiêu cực từ AGV.")

# Kiểm tra xem đa số người mù có chịu tác động tích cực từ AGV hay không với ngưỡng 0.4
perBl = positive_impact(impactToBlinder, 0.4)
if perBl > 50:
    print("Đa số người mù chịu tác động tiêu cực từ AGV.")
else:
    print("Đa số người mù không chịu tác động tiêu cực từ AGV.")

# Kiểm tra xem đa số người đến khoa viện BFGMEN có chịu tác động tích cực từ AGV hay không với ngưỡng 0.4
perB = positive_impact(impactToBFGMEN, 0.4)
if perB > 50:
    print("Đa số người đến khoa viện BFGMEN chịu tác động tiêu cực từ AGV.")
else:
    print("Đa số người đến khoa viện BFGMEN không chịu tác động tiêu cực từ AGV.")
