# list  ~~~~~~~~~~~~~~~~
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




# tuple ~~~~~~~~~~~~~~
# immutable,ordered,allows duplicates,heterogeneous  
# only 2 methods - count and index
fruits = ('apple', 'banana', 'cherry','apple')
# fruits[0] = 'orange'  #can't change value (immutable)
index = fruits.index('banana')  # find index of value (ordered)
# print(fruits[1])
# print(index)
count = fruits.count('apple')  # count number of times value appears
# print(count)

# a = ('1',2,3,'banana')
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])
    
# print(a)

# print(fruits)
# print(type(fruits))   
# tuple unpacking
# ~~~~~~~~~~~~~~~~~~~
a,b,c,d = (1,2,3,4)
# print(a)
# print(c)








# set ~~~~~~~~~~~~~~
# mutuable,unordered, doesn't allows duplicates,semi heterogeneous(string,number,tuples allowed)

# s = {1,2,3,4,5,5,5,5,6,7,8,9,10}
# print(s)
# print(type(s))

# set methods
# ~~~~~~~~~~~~~
# s.add(11)  # add value at the end
# print(s)
# s.remove(11)  # remove value
# print(s)
# s.pop()  # remove last value and return it
# print(s)
# s.clear()  # remove all values
# print(s)
# print(type(s))
# print(hash(1))
# print(hash("hello")) everytime you hash you get a different no. so it's unordered
# only immutable things can store like no,string,tuple
# list and dict can't store in set as they are mutable and ordered
# set can't traverse through index as they are unordered

# a={1,2,3,4,5}
# b={4,5,6,7,8}
# s= a.union(b)  # union of two sets
# print(s)
# s= a.intersection(b)  # intersection of two sets
# print(s)
# s= a.difference(b)  # difference of two sets
# print(s)
# s= a.symmetric_difference(b)  # symmetric difference of two sets
# print(s)
# print(a)
# print(b)

# dict ~~~~~~~~~~~~~~
# mutable,follows insertion order,allows duplicates but key must be unique,heterogeneous

d= {10:100,20:200,30:300,40:400,50:500}
# d[10]=110 #update
# d[60] = 600   #add
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d[10])

# for i in d:   #i is index/key
    # print(i,d[i])

# for i in d.values():
#     print(i)    


# help(dict)
# dict methods~~~~~~~~~~

d2 = d.copy() #shallow copy --> doesn't affect the original
# print (d2)

num = d2.get(30)
# print(num)



