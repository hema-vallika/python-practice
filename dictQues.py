# 1. -----------> write python script to merge two python dictionaries
d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}
# d1.update(d2)
for i in d2:
    d1[i] = d2[i] #create /if exist then update
# print(d1)

#2. ----------> write program to sum all the values in a dict

# d={10:100,20:200,30:300}
# sum=0
#  for i in d.values():
#      sum+=i  or
# for i in d:
#     sum+=d[i]
# print(sum)

#3.-----------> count freq of each element in a list
# a=[1,1,1,2,2,2,2,2,3,3,3,4,4,5,5,5]
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

#4.-----------> merge two dict if common key exist then add them
d1 = {10:100,20:200,30:300}
d2 = {30:400,50:500,60:600}
for i in d2:
    if i in d1:
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
print(d1)

#5.-----------> write a python program to print all unique values in a dict
d1 = {10:100,20:200,30:300}
