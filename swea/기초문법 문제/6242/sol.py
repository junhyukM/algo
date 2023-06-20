blood = ['A','A','A','O','B','B','O','AB','AB','O']

A_blood = []
B_blood = []
O_blood = []
AB_blood = []

for i in blood:
    if i == 'A':
        A_blood.append(i)
    elif i == 'B':
        B_blood.append(i)
    elif i == 'O':
        O_blood.append(i)
    else:
        AB_blood.append(i)
blood_dict = {
    'A': len(A_blood),
    'O': len(O_blood),
    'B': len(B_blood),
    'AB': len(AB_blood),
}                    
print(blood_dict)        


### 풀이2
blood_dict = {
    'A': 0,
    'B': 0,
    'O': 0,
    'AB': 0,
}

blood_list = ['A','A','A','O','B','B','O','AB','AB','O']

for blood in blood_list:
    blood_dict[blood] += 1

print(blood_dict)

## 풀이3

location = ['서울', '대전', '대전', '부산', '제주']
location_dict = {}

for l in location:
    # 이미 기록을 한 경우
    if l in location_dict.keys():
        location_dict[l] += 1
    # 처음으로 등장한 경우
    else:
        location_dict[l] = 1

print(location_dict)
