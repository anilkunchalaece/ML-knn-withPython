import random
# seperate list in to two seperate values

TOTAL_SAMPLE_LENGTH = 150
RANDOM_VALUES_TO_BE_SELECTED = 120
REMAINING_VALUES = TOTAL_SAMPLE_LENGTH - RANDOM_VALUES_TO_BE_SELECTED
"""
f_1 = list(range(0,150))
f_2 = list(range(150,300))
f_3 = list(range(300,450))
f_4 = list(range(450,600))
"""

import random

totalData = list()

fHandler = open('IRIS_DATASET.txt','r')
next(fHandler)

#variables to save the data
f_1 = list()
f_2 = list()
f_3 = list()
f_4 = list()
c = list()

for line in fHandler:

    temp = line.split(",")
    #print(temp)
    for ele in range(len(temp)):
        temp[ele] = float(temp[ele].replace(";\n","").replace("]",""))
    f_1.extend(temp[0:1])
    f_2.extend(temp[1:2])
    f_3.extend(temp[2:3])
    f_4.extend(temp[3:4])
    c.extend(temp[4:5])
fHandler.close()

index_list = list(range(TOTAL_SAMPLE_LENGTH))
# print(index_list)
# print("####### Radom 12o ########")

random_120_values_index = random.sample(index_list,RANDOM_VALUES_TO_BE_SELECTED)
#print(random_120_values_index)

#pick another 30 values index

remaining_30_index = list()
for val in range(len(index_list)) :
	if index_list[val] not in random_120_values_index :
		remaining_30_index.append(index_list[val])
#print("######## Remaining 30#########")
#print(remaining_30_index)


#using the generated index assign the values to the new lists
f_1_random_120 = list()
f_2_random_120 = list()
f_3_random_120 = list()
f_4_random_120 = list()
c_random_120 = list()

f_1_remaining_30 = list()
f_2_remaining_30 = list()
f_3_remaining_30 = list()
f_4_remaining_30 = list()
c_remaining_30 = list()

for index in random_120_values_index :
	f_1_random_120.append(f_1[index])
	f_2_random_120.append(f_2[index])
	f_3_random_120.append(f_3[index])
	f_4_random_120.append(f_4[index])
	c_random_120.append(c[index])

for index in remaining_30_index :
	f_1_remaining_30.append(f_1[index])
	f_2_remaining_30.append(f_2[index])
	f_3_remaining_30.append(f_3[index])	
	f_4_remaining_30.append(f_4[index])
	c_remaining_30.append(c[index])
"""
print(f_1)
print(f_1_random_120)
print(f_1_remaining_30)
print(f_2)
print(f_2_random_120)
print(f_2_remaining_30)
print(f_3)
print(f_3_random_120)
print(f_3_remaining_30)
print(f_4)
print(f_4_random_120)
print(f_4_remaining_30)
"""
def most_common(lst):
    return max(set(lst), key=lst.count)
import math

# print ("f1 " + str(f_1_remaining_30[0])  + " f2 " + str(f_2_remaining_30[0]) + " f3 " + str(f_3_remaining_30[0]) + " f4 " + str(f_4_remaining_30[0]) +
#        " c " + str(c_remaining_30[0]))
EDArray = list()
resultArray = list()

for index in range(len(c_remaining_30)) :
        EDArray = []
        for val in range(len(random_120_values_index)) :
                d1 = f_1_random_120[val] - f_1_remaining_30[index]
                d2 = f_2_random_120[val] - f_2_remaining_30[index]
                d3 = f_3_random_120[val] - f_3_remaining_30[index]
                d4 = f_4_random_120[val] - f_4_remaining_30[index]
                totalD = (d1*d1)+(d2*d2)+(d3*d3)+(d4*d4)
                ED = math.sqrt(totalD)
                EDArray.append(ED)
                #print(EDArray)
                #print("val index " + str(val) + " totalD " + str(totalD) + " ED " + str(ED) +" C " + str(c[val]))
        top3 = sorted(EDArray)[0:3] # Geting top3 equalidian distance
        # print("k3 ",top3)
        # get the class elements
        clsArray = list()
        for k in top3 :
                # print(EDArray.index(k))
                # get the index of those minimum k's and get their original class values
                clsArray.append(c_random_120[EDArray.index(k)])
        # find most commom value in the class array
        mCommon = most_common(clsArray)
        # append them to the result dict
        resultArray.append((mCommon, c_remaining_30[index]))

# print the expected value and calculated value
print(resultArray)
cnt = 0

# calculate the accuracy
for result in resultArray :
        if result[0] == result[1] :
                cnt = cnt + 1

accuracy = cnt / len(resultArray)

print("accuracy is " + str(accuracy))
