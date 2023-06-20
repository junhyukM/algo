num = list(range(1,201))

result = []
for n in num:
    if n % 7 == 0:
        if n % 5:
            result.append(n)
# if를 이중으로 해서 두가지 조건을 만족하는 요소를 리스트에 append 했음
# join을 하려 했는데 int형은 안된다고 해서 구글링을 해보니 각 요소에 str로 매핑을 하면 된다고 해서
# map(str, result)로 각 요소를 문자열로 변경시켜줌            
result = ','.join(map(str, result))
print(result)


### 강사님 풀이
for i in range(1, 201):
    if i % 7 == 0 and i % 5 != 0:
        if i == 196:
            print(i)
            continue
        print(i, end=',')