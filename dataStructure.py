# list
# mutable,ordered,allows duplicates,heterogeneous
fruits = ['apple', 'banana', 'cherry']
# print(type(fruits)) 
fruits[1]= 'orange'  # change value
# print(fruits)
fruits.append('grape')  # add value at the end
fruits.insert(1, 'kiwi')  # add value at index 1
fruits.remove('cherry')  # remove value
popped_item = fruits.pop(2)  # remove last value and return it
# print(popped_item)
fruits.sort()  # sort the list
fruits.reverse()  # reverse the list
# print(fruits)


# tuple
# immutable,ordered,allows duplicates,heterogeneous