import numpy as np
from numpy import genfromtxt




row = int(input("Please Enter Rows Number? "))
column = row


raw_matrix = np.array(genfromtxt('/Users/amir/Desktop/gravity.csv', delimiter=','))
matrix = np.array(raw_matrix)

print(matrix)



# target_orgin = list(map(float,input("Enter Targeted Orgin(by order!) - Seprated by Space: ").split()))
target_orgin = [80, 150, 140, 160, 180]
# target_destination = list(map(float,input("Enter Targeted Destination(by order!) - Seprated by Space: ").split()))
target_destination = [40, 90, 320, 80, 200]

target = sum(target_orgin)
k = sum(target_orgin)/sum(target_destination)
target_destination  = [i * k for i in target_destination] #New Target destination

# print(target_destination)
# print(target_orgin)
# print(k)


if k != 1.0:
    print("WARNING! SUM target-destination is not equal to SUM target-orgin! Automatically programme will fix this! ")
    print("New Target-Destination is: " )
    print(target_destination)




f_orgins = [0] * row
f_destinations = [0] * column
error = 100


def calculate_f_orgins():
    for i in range(row):
        f_orgins[i] = target_orgin[i] / matrix.sum(axis=1, dtype='float').item(i)


def calculate_f_destination():
    for j in range(column):
        f_destinations[j] = target_destination[j] / matrix.sum(axis=0, dtype='float').item(j)


def calculate_sum_Denominator(i):
    denominator = 0
    for j in range(column):
        denominator += matrix[i][j]*f_destinations[j]

    return denominator



def calculate_errror():
    global error
    error = 0.0
    for i in range(row):
        error += abs(target_orgin[i] - matrix.sum(axis=1, dtype='float').item(i))

    for j in range(column):
        error += abs(target_destination[j] - matrix.sum(axis=0, dtype='float').item(j))




while error>1:

    calculate_f_orgins()
    calculate_f_destination()

    print("f_orgin is: ",format(f_orgins))
    print("f_destination is: ", format(f_destinations))

    for i in range(row):
        denominator = calculate_sum_Denominator(i)
        for j in range(column):
            matrix[i][j] = target_orgin[i]*(matrix[i][j]*f_destinations[j])/denominator


    #print(f_destinations)

    calculate_errror()
    error = 100 * error / target

    print("The Transportation Matrix is: ")
    print(matrix)
    print("Error is:",error, "%")

