import random
# seperate list in to two seperate values

TOTAL_SAMPLE_LENGTH = 150
RANDOM_VALUES_TO_BE_SELECTED = 120
REMAINING_VALUES = TOTAL_SAMPLE_LENGTH - RANDOM_VALUES_TO_BE_SELECTED

def printMatrix(lst) :
        for row in lst :
                print(row)


import random

totalData = list()

fHandler = open('IRIS_DATASET.txt','r')
next(fHandler)


features = list()

for line in fHandler:

    temp = line.split(",")
    #print(temp)
    for ele in range(len(temp)):
        temp[ele] = float(temp[ele].replace(";\n","").replace("]",""))
    features.append([float(temp[0]),float(temp[1]),float(temp[2]),float(temp[3]),int(temp[4])])
fHandler.close()
# printMatrix(features)

index_list = list(range(TOTAL_SAMPLE_LENGTH))
random_120_values_index = random.sample(index_list,RANDOM_VALUES_TO_BE_SELECTED)
remaining_30_index = list()
for val in range(len(index_list)) :
	if index_list[val] not in random_120_values_index :
		remaining_30_index.append(index_list[val])

feature_random_120 = list()
remaing_30 = list()
featuresDict = dict()

for index in random_120_values_index :
 	feature_random_120.append(features[index])

for index in remaining_30_index :
	remaing_30.append(features[index])

# calculate the no-of classes 
# Workaround - Need to write again
classes = list()
for feature in features :
        classes.append(feature[-1])
classes = set(classes)
print("no of classes are : " + str(len(classes)))

# create a dict with number of classes - class name as key and features list as value
# calculate the mean also
for cla in classes :
        temp = list()
        for feature in feature_random_120 :
                if feature[4] == cla :
                        temp.append(feature)
        # calculate the mean
        f1_sum = 0
        f2_sum = 0
        f3_sum = 0
        f4_sum = 0
        for row in temp :
                f1_sum = f1_sum + row[0]
                f2_sum = f2_sum + row[1]
                f3_sum = f3_sum + row[2]
                f4_sum = f4_sum + row[3]

        featuresDict[cla] = {
         "features" : temp,
         "mean" : [f1_sum/len(temp) , f2_sum / len(temp), f3_sum / len(temp) , f4_sum/len(temp)]
        }

# printMatrix(featuresDict[2])
# print(featuresDict[1])

# Predict the value based on minimum distance to mean algorithm
currentFea = remaing_30[0]
print(currentFea)
# Calculate the equidian distance between current i.e test feature and mean values from training set
meanED = list()
import math

for key,values in featuresDict.items() :
        d1 = values['mean'][0] - currentFea[0]
        d2 = values['mean'][1] - currentFea[1] 
        d3 = values['mean'][2] - currentFea[2]
        d4 = values['mean'][3] - currentFea[3] 
        ED = math.sqrt(d1*d1 + d2*d2 + d3*d3 + d4*d4)
        meanED.append(ED)
print(meanED.index(min(meanED)))