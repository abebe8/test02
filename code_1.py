list_1 = [61,3,0,25,10,60,2,43,55,15]
list_2 = [15,8,4,0,0,59,3.08,87,30,0.667]
list_3 = [372,102,101,17,25,1186,3.77,1673,701,0.502]

# 新配列を作成
array = []
array.append(list_1)
array.append(list_2)
array.append(list_3)
# print(array)
print(array[2][8])

# 各配列のi番目の要素を抽出して、別の配列に格納する

array_1,array_2,array_3,array_4,array_5,array_6,array_7,array_8,array_9,array_10 = [],[],[],[],[],[],[],[],[],[]

array_1.append(array[0][0])
array_1.append(array[1][0])
array_1.append(array[2][0])
print(array_1)

array_2.append(array[0][1])
array_2.append(array[1][1])
array_2.append(array[2][1])
print(array_2)

for i in range(3):
    array_1.append(array[i][0])
    array_2.append(array[i][1])
    array_3.append(array[i][2])
    array_4.append(array[i][3])
    array_5.append(array[i][4])
    array_6.append(array[i][5])
    array_7.append(array[i][6])
    array_8.append(array[i][7])
    array_9.append(array[i][8])
    array_10.append(array[i][9])

# print(array_1)
# print(array_2)
# print(array_3)
# print(array_4)
# print(array_5)
# print(array_6)
# print(array_7)
# print(array_8)
# print(array_9)
# print(array_10)

import pandas as pd
df = pd.DataFrame({"x":list_1,"y":list_2,"z":list_3})
print(df)



