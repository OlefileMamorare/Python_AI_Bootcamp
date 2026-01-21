l1 = list()


#Adding Elements to a list: append(), extend(), insert()
list1 = [1 , 2.2 , "abc"]

#extend(): you can add multiple elements at once using the extend() method:
list1.extend(['x' , 'y'])
print(list1)

#insert(): lets you add elements at specified index:
years = [2001 , 2002, 2003 , 2005]
years.insert(3 , 2004)
print(years)


#Removing elements from the list:

#pop(): removes and returns elements at a specified index
#if no index is provided, it removes and returns the last element
l2 = ['a' , 'b' , 'c' , 'd']
x = l2.pop(3)
print(l2 , "removed: " , x)

#remove() deletes the first occurrence of a specified element
#it removes by value not by index
l3 = [10 , 20 ,30 ,40]
l3.remove(20)
print(l3)

#to remove all occurrences, use a while loop:
l4 = [10 , 20 , 30 , 10, 40 , 10]

while 10 in l4:
    l4.remove(10)
print(l4)

#sort() , sorted(list)
#the sort() methods sorts the list in ascending order:
numbers = [3 , 4 , 1 , 1 , 1 , 7 , 8 , 5]
numbers.sort()
print(numbers)

#sort(reverse; True): sorts the list in descending order:
numbers_rev = [ 1 , 2 , 3 , 4 , 5 , 6 , 9]
numbers_rev.sort(reverse=True)
print(numbers_rev)

#sorted(list): sorts and returns the list, but leaves the original list unchanged:
numbers2 =[3 , 4 , 1 , 1 , 1 , 7 , 8 , 5]
sorted_numbers = sorted(numbers2)
print(numbers2)
print(sorted_numbers)


