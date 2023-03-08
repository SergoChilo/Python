import itertools
import numpy as np

""" numpy """
# #numpy array
# 1. Ստեղծել np զանգված, որը կպարունակի 100 պատահական ամբողջ թիվ։ Այնուհետև ստանալ այն տարրերի ինդեքսները,
# որոնք ավարտվում են 6-ով։
#########################################################################################################
# README...
# Generate random numbers between 1 - 500
# Print numbers
# The formula f.e. 16 - 6 = 10 % 10 = 0
# Printed indexes of numbers
#########################################################################################################
###########C__O__D__E####################################################################################
arr_1 = np.random.randint(1, 500, (10, 10))
print(arr_1)
indexes = np.where(arr_1 % 10 == 6)
print('=' * 50)
print(indexes)

# 2. Ստեղծել np զանգված, որի բոլոր տարրերը կլինեն 0-ներ, իսկ անկյունագծայինները՝ 1։

# identity = np.eye(3)
# print(identity)

# 3. Ստեղծել երկու np միաչափ զանգված արդեն պատրաստի պիտոնական լիստերից։ Ապա կցեք երկու զանգվածներն իրար
# հորիզոնական ուղությամբ։

# l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# l_2 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr_1 = np.array(l_1)
# arr_2 = np.array(l_2)
# print(np.hstack((arr_1, arr_2)))

# 4. Ստեղծել երկու np միաչափ զանգված արդեն պատրաստի պիտոնական լիստերից։ Ապա կցեք երկու
# զանգվածներն իրար վերտիկալ ուղությամբ։

# l_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# l_2 = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# arr_1 = np.array(l_1)
# arr_2 = np.array(l_2)
# print(np.vstack((arr_1, arr_2)))

# 5. Ստեղծել երկչափ զանգված, որը կունենա (3, 3) shape: Այնուհետև ստեղծել նոր զանգված, որը կլինի նախորդ զանգվածը, սակայն
# առաջին և երրորդ սյուների տեղերը փոխած։
#########################################################################################################
# README
# l   - is a list
# arr - is a matrix 3x3
# arr_1 is a new matrix [3 2 1]
#########################################################################################################
###########C__O__D__E####################################################################################
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = np.array(l).reshape(3, 3)
# print(arr)
# print('=' * 30)
# arr_1 = arr[:, [2, 1, 0]]
# print(arr_1)

# 6.  Ստեղծել երեք զանգված։ Առաջինը պետք է պարունակի միայն 0-ներ, երկրորդը միայն 1-եր, իսկ երրորդը միայն 9-եր։
#
# print('#' * 20)
# arr_0 = np.zeros((3, 3), dtype=int)
# print(f'{arr_0=}')
# print('#' * 20)
# arr_1 = np.ones((3, 3), dtype=int)
# print(f'{arr_1=}')
# print('#' * 20)
# arr_9 = np.ones((3, 3), dtype=int) * 9
# print(f'{arr_9=}')
# print('#' * 20)

# 7. Ստեղծել (10, 10) shape-ով զանգված։ Ապա փոխել դրա shape-ը հնարավոր բոլոր տարբերակներով։

# print('=' * 30)
# arr = np.arange(1, 101)
# print(arr)
# print('=' * 30)
# print(arr.reshape(1, 100))
# print('=' * 30)
# print(arr.reshape(2, 50))
# print('=' * 30)
# print(arr.reshape(4, 25))
# print('=' * 30)
# print(arr.reshape(5, 20))
# print('=' * 30)
# print(arr.reshape(10, 10))
# print('=' * 30)
# print(arr.reshape(20, 5))
# print('=' * 30)
# print(arr.reshape(25, 4))
# print('=' * 30)
# print(arr.reshape(50, 2))
# print('=' * 30)
# print(arr.reshape(100, 1))
# print('=' * 30)

# 8. Ստեղծել երկու երկչափ զանգված և հաշվել դրանց ա) տարր առ տարր արտադրյալը, բ) մատրիցային արտադրյալը։

# arr_1 = np.arange(10, 19).reshape(3, 3)
# arr_2 = np.arange(1, 10).reshape(3, 3)
# print(arr_1 * arr_2)
# print('=' * 30)
# print(np.matmul(arr_1, arr_2))

# 9. Ստեղծել երկու զանգված (10, 10) shape-ի, որոնք կպարունակեն 0-ից 20-ը պատահական թվեր։ Բաժանել մատրիցներն իրար։
# Այնուհետև առանձնացնել նոր մատրիցի մեջ մատրիցների այն տարրերը, որոնք թիվ են (inf կամ nan չեն): Ստանալ inf-երի և
# nan-երի նաև դրանց ինդեքսները։

# np.seterr(divide='ignore', invalid='ignore')
# arr_1 = np.random.randint(0, 20, (10, 10))
# arr_2 = np.random.randint(0, 20, (10, 10))
# print('=' * 7, '   First matrix   ', '=' * 10)
# print(arr_1)
# print('=' * 7, '   Second matrix   ', '=' * 10)
# print(arr_2)
# print('=' * 7, '   Result First matrix : Second matrix ', '=' * 10)
# arr_3 = np.divide(arr_1, arr_2)
# print(arr_3)
# print('=' * 30)
# print('Indexes of nan is : ', np.argwhere(np.isnan(arr_3)))
# print('Indexes of inf is : ', np.argwhere(np.isinf(arr_3)))

# 10. Ստեղծել (3, 3) մատրից, որի տարրերը կլինեն 11-19, սակայն բացահայտ կերպով սահմանել տարրերի տիպը որպես float։

# arr = np.arange(11, 20).reshape(3, 3)
# print('Before converting numpy int array to float array : \n')
# print(arr)
# print('=' * 50)
# arr = arr.astype(float)
# print('After converting numpy int array to float array : \n')
# print(arr)

""" numpy Part 2 """

# 1. Create a numpy array from a python list consisting even numbers from 0-20.

# l = range(0, 20)
# arr = np.array(l)
# indexes = np.where(arr % 2 == 0)
# print(indexes)

# 2. Create a 3x3 numpy array, which will contain 3s only.

# arr = np.ones((3, 3), dtype=int) * 3
# print(arr)

# 3. Create a 1D numpy array with length 18. Reshape it to 3 columns and 6 rows.

# l = range(0, 18)
# arr = np.array(l).reshape(3, 6)
# print(arr)

# 4. Create two numpy arrays of shape 10x10. One of them must contain the numbers from 1-100, the other from 100-1.
# Add them and output the result.

# l1 = range(1, 101)
# l2 = range(100, 0, -1)
# arr_1 = np.array(l1).reshape(10, 10)
# arr_2 = np.array(l2).reshape(10, 10)
# print(arr_1)
# print('=' * 50)
# print(arr_2)
# print('=' * 10 , 'The sum', '=' * 10)
# print(arr_1 + arr_2)
###########################################################################################################
# myarr1 = np.arange(1,101).reshape((10,10))
# myarr2 = np.arange(100,0,-1).reshape((10,10))
# mysum = myarr1+myarr2
# print(mysum)

# 5. In how many ways can we reshape an array of length 12? Write down all the possibilities (2D).

# l = range(1, 13)
# arr = np.array(l).reshape(1, 12)
# print('=' * 10 , '1 x 12', '=' * 10)
# print(arr)
# print('=' * 10 , '2 x 6', '=' * 10)
# arr = np.array(l).reshape(2, 6)
# print(arr)
# print('=' * 10 , '3 x 4', '=' * 10)
# arr = np.array(l).reshape(3, 4)
# print(arr)
# print('=' * 10 , '4 x 3', '=' * 10)
# arr = np.array(l).reshape(4, 3)
# print(arr)
# print('=' * 10 , '6 x 2', '=' * 10)
# arr = np.array(l).reshape(6, 2)
# print(arr)
# print('=' * 10 , '12 x 1', '=' * 10)
# arr = np.array(l).reshape(12, 1)
# print(arr)
# print('=' * 50)

# myarr1=np.arange(0,12)
# myl=[i for i in range(1,13) if 12%i==0]
# a=[j for j in itertools.permutations(myl,2) if j[0]*j[1]==12]
# print(a)
# for k in a:
#     myarrshape=myarr1.reshape(k)
#     print(myarrshape)

# 6. Create an array of shape (5, 5) that will contain zeros except for the diagonal. The diagonal should be all 4s.

# print(np.eye(5) * 4)

# 7․ Create a numpy array that will contain random numbers from 0, 100 and will have 20 columns with 5 rows.
# arr = np.full((3, 3), 5)

# arr = np.random.randint(0, 100, (20, 5))
# print(arr)

# 8․ Create a 3 dimensional array from a 1 dimensional array of length 100.

# l = range(1, 101, 1)
# arr = np.array(l).reshape((2, 5, 10))
# print(arr)

# 9. Create a 3x3 array containing random numbers from (0, 1). Then, change the datatype of the array to integers
# (you need to do some googling for this).

# arr_2 = np.random.random(9).reshape(3, 3)
# print(arr_2.astype(int))


# 10. Create two arrays of shape 3x3 that will contain random numbers from 1-100. Calculate their scalar product,
# dot product, division and difference. Use np methods AND corresponding operators.

# arr_1 = np.random.randint(1, 500, (3, 3))
# arr_2 = np.random.randint(1, 500, (3, 3))
# print(arr_1)
# print('=' * 50)
# print(arr_2)
# print('=' * 50, 'սկալար արտադրյալը')
# print(arr_1 @ arr_2)
# print('=' * 50, 'վեկտորական արտադրյալը')
# print(arr_1 * arr_2)
# print('=' * 50, 'քանորդը')
# print(arr_1 / arr_2)
# print('=' * 50, 'տարբերությունը')
# print(arr_1 - arr_2)

# 11. Create an array of shape 5x5. Calculate its determinant. If the determinant is non-zero, calculate the inverse as
# well. Otherwise, tell the user that the matrix in non-invertible.

# arr = np.random.randint(1, 5, (5, 5))
# print('The matrix is : ')
# print(arr)
# if np.linalg.det(arr) == 0:
#     print('The determinant is a 0. The matrix in non-invertible')
# else:
#     print(f'{np.linalg.det(arr)=}')
#     print('The inverse of matrix is :\n' ,np.linalg.inv(arr))

# 12. Create an array of shape 3x3 that will contain numbers from 1-10. Calculate the scalar and dot products
# of it with its transposed version.

# arr = np.random.randint(1, 10, (3, 3))
# print(arr)
# print('+' * 20)
# print(arr.T)
# print('+' * 20)
# print(arr * arr.T)
# print('+' * 20)
# print(np.dot(arr, arr.T))

# 13. Create a 3x3 array of random integers. Calculate its inverse (check if possible). Then find the vector product of
# these. What do you get?

# arr = np.random.randint(-500, 500, (3, 3))
# print(arr)
# print('+' * 20)
# if np.linalg.det(arr) == 0:
#     print('The determinant is a 0. The matrix in non-invertible')
# else:
#     print(f'{np.linalg.det(arr)=}')
#     print('+' * 20)
#     print('The inverse of matrix is :\n' ,np.linalg.inv(arr))
#     print('+' * 20)
#     print(arr @ np.linalg.inv(arr))