#1.---> print positive and negative numbers in a list

# l = [12,14,-32,-33,44,-87,79]

# for i in l:
#     if i >= 0:
#         print(i, end = " ")
# for i in l:
#     if i < 0:
#         print(i, end = " ")        


# 2. ----> mean of list elements
# l=[23,66,87,98,67,22]
# sum =0
# for i in l:
#     sum = sum+i
# print("mean of list elements is: ", sum/len(l))


# 3. ------> find the greatest element and print it's index too

# l = [23,66,87,98,67,22,98,98,98]

# max = l[0]
# index =0
# for i in range(len(l)):
#     if l[i] > max:
#         max = l[i]
#         index = i
# print("greatest element is: ", max, "and it's index is: ", index)     


# 4. ------> find the second greatest element in the list
# l = [23,66,87,98,67,22,98,98,98]

# max = l[0]
# second_max = l[0]
# for i in range(len(l)):
#     if l[i] > max:
#         second_max = max
#         max = l[i]
#     elif l[i] > second_max and l[i] != max:
#         second_max = l[i]
# print("second greatest element is: ", second_max)


# 5. -------> check if list is sprted or not
# l=[13,45,17,29,79]

# for i in range(len(l)-1):
#     if l[i] > l[i+1]:
#         print("list is not sorted")
#         break
# else:
#     print("list is sorted")
    