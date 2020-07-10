list1 = [1,2,3,4,5]
list2 = ['m','h','a','n']

tuple = (1,'mohan',3,4)

dict = {'J':'java','p':'python'}


#assigning elements to lists

list1.append('numbers')  #addeds the element 'numbers' at the last of the list1
print(list1)

list2.insert(1,'o')
print(list2)


#accessing elements from tuple

print(tuple[1]) #prints mohan as mohan is at index 1


#deleting elements from dictionary


dict['p1'] = 'pearl' # adds this element to the dictionary
print(dict)

del dict['p1'] # deletes the element 'p1':'pearl'
print(dict)

dict.pop('J') # this will diplay the element and deletes the element from the dictionary

dict.clear() # this will clear all the elements but dictionary will be avilable. we can add elements to the dictionary
print(dict)
