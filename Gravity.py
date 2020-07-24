from numpy import *
import numpy as np
import math

error_itr = []
list_itr = []

np.set_printoptions(precision=3) #print option

row = int(input("Please Enter Rows Number? "))
column = row

#df = pd.read_csv()

raw_matrix = np.array(genfromtxt('/Users/amir/Desktop/gravity.csv', delimiter=',')) #pandas
main_matrix = np.array(raw_matrix)
print(main_matrix)



alpha = 0.05
beta = 0.2
############### Calculate Cij AND Replace Nan Values ###############
for i in range(row):
    for j in range(column):
        main_matrix[i][j] = alpha*math.exp(-beta*(math.log(main_matrix[i][j]+1))**2)   #f(cij)
         # math.exp(x) == e^x , math.log == ln(x)


where_are_nans = isnan(main_matrix)
main_matrix[where_are_nans] = 10**-50  # Notes! np.inf, 0, ...
print(main_matrix)




# target_orgin = list(map(float,input("Enter Targeted Orgin(by order!) - Seprated by Space: ").split()))
target_orgin = [80, 150, 140, 160, 180]
# target_destination = list(map(float,input("Enter Targeted Destination(by order!) - Seprated by Space: ").split()))
target_destination = [40, 90, 320, 80, 200]

target = sum(target_orgin)
k = sum(target_orgin)/sum(target_destination) #sum(list), np.array.sum(axis=1)

target_destination  = [i * k for i in target_destination] #New Target destination



if k != 1.0:
    print("WARNING! SUM target-destination is not equal to SUM target-orgin! Automatically programme will fix this! ")
    print("New Target-Destination is: " )
    print(target_destination)






A = [0] * row  # A = [0,0,0,0,0,0]
B= [1] * column
error = 100
matrix = np.copy(main_matrix)



def calculate_A():
    global A
    A = [0] * row

    for i in range(row):
        for j in range(column):
            A[i] += B[j] * target_destination[j] * main_matrix[i][j]


    A = [1/i for i in A]



def calculate_B():
    global B
    B = [0] * column

    for j in range(column):
        for i in range(row):
            B[j] += A[i] * target_orgin[i] * main_matrix[i][j]

    B = [1 / j for j in B]  #devide by zero


def calculate_error():
    global error
    error = 0.0
    for i in range(row):
        error += abs(target_orgin[i] - matrix.sum(axis=1, dtype='float').item(i))
        # matrix.sum(axis=1, dtype='float')[i]

    for j in range(column):
        error += abs(target_destination[j] - matrix.sum(axis=0, dtype='float').item(j))

    # return error


itr = 0
while error>1:
    itr += 1
    calculate_A()
    calculate_B()

    print("A is: ",format(A))
    print("B is: ", format(B))


    for i in range(row):
        for j in range(column):
            matrix[i][j] = A[i] * target_orgin[i] * B[j] * target_destination[j] * main_matrix[i][j]


    calculate_error()

    error = 100 * error / target

    error_itr.append(error)
    list_itr.append(itr)
    print("The Error ITR: ")
    print(error_itr)
    print(list_itr)
    print("The Transportation Matrix is: ")
    print(matrix)
    #print(main_matrix)
    print("Error is:",error, "%")




import matplotlib.pyplot as plt


plt.plot(list_itr,error_itr)

plt.show()
