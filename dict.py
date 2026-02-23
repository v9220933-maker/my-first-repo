dict1={'name':'vianny', 'age':22,'gender':'male'}
print(dict1)
del dict1['name']
print(dict1)
print("successfully deleted")
dict1['name']='john'
print(dict1)
dict1['nationality']='ugandan'
print(dict1)
for keys in dict1:
    print(keys)

print(dict1['name'])
dict1.clear()
print(dict1)
list1=[1,2,3,4]
list2=[2,4,6,8]
list3=[dict(zip (list1,list2))]
print(list3)
for items in list3:
    print(items)