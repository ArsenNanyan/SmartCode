# 110

# array1 = []
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     array1.append(number)
# array1.sort()
# for i in range(len(array1)):
#     print(array1[i])



# 111

# array1 = []
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     array1.append(number)
# array1.sort(reverse = True)
# for i in range(len(array1)):
#     print(array1[i])



# 112

# array2 = []
# n = int(input("Enter a number of deleteable numbers: "))
# while True:
#     number = int(input("Enter a number: "))
#     if number == 0:
#         break
#     array2.append(number)
# array2.sort()

# for i in range(0,n):
#     array2.remove(max(array2))
#     array2.remove(min(array2))
# print(array2)



# 113

# array3 = []
# array4 = []
# while True:
#     word = input("Enter a word: ")
#     if word == '0':
#         break
#     array3.append(word)
# for i in range(0,len(array3)):
#         if array3[i]  not in array4:
#              array4.append(array3[i])
# print(array4)



# 114

# array4 = []
# while True:
#     number = input("Enter a number: ")
#     if number == '':
#         break
#     array4.append(int(number))
# array4.sort()
# print(array4)



# 115

# array5 = []
# number = int(input("Enter a number: "))
# for i in range(1, number//2+1):
#     if number % i == 0:
#         array5.append(i) 
# print(array5)



# 116

# array5 = []
# summ = 0
# number = int(input("Enter a number: "))
# for i in range(1, number//2+1):
#     if number % i == 0:
#         array5.append(i) 
# for k in range(0,len(array5)):
#     summ = summ + array5[k]
# if summ == number:
#     print("Perfect number")
# else:
#     print("Not a perfect number")



# 117

# list = []
# sentance = input("Enter a sentance: ")

# for word in sentance.split(' '):
#     if word == '':
#         continue
#     else:
#         list.append(word)
# print(list)



# 118

# list1 = []
# list2 = []
# sentance = input("Enter a sentance: ")
# for word in sentance.split():
#     list1.append(word.lower())
# list2 = list1[::-1]
# if list1 == list2:
#     print("Palindrom")
# else:
#     print("Not palindrom")



# 119

# array6 = []
# array7 = []
# array8 = []
# array9 = []

# count = 0
# summ = 0
# while True:
#     number = input("Enter a number: ")
#     if number == '':
#         break
#     array6.append(int(number))
#     summ = summ + int(number)
#     count += 1
# average = summ / count
# array6.sort()
# for i in array6:
#     if i < average:
#         array7.append(i)
#     if i == average:
#         array8.append(i)
#     if i > average:
#         array9.append(i)
# print(array7)
# print(array8)
# print(array9)



# 121

# import random

# arr = []
# while True:
#     number = random.randint(1,47)
#     if len(arr) == 6:
#         break
#     if number in arr:
#         continue
#     else: 
#         arr.append(number)

# print(arr)



# 133

# arr1 = [1,2,3,4,5,6]
# arr2 = [1,2,3,4]
# string1 = ''
# string2 = ''
# for i in range(len(arr1)):
#     string1 = string1 + str(arr1[i])
# for j in range(len(arr2)):
#     string2 = string2 + str(arr2[j])

# if string2 in string1:
#     print("Yes")
# else:
#     print("No")


