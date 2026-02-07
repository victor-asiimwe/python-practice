#Organizing a List
#Python provides a number of different ways to organize your lists, depending on the situation.

#Sorting a List Permanently with the sort() Method
#.sort() organizes elements in an alphabetic order and once changed, this order change is permanent
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars.sort()
print(Cars)
#list sorted from A to Z

#You can also sort this list in reverse-alphabetical order by passing the argument reverse=True to the sort() method.
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars.sort(reverse=True)
print(Cars)
#Again list is changed permanently

#Sorting a List Temporarily with the sorted() Function
#To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Final_1 = f"Here is the original list: {Cars}"
print(Final_1)
#This is original list
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Final_2 = f"Here is the original list: {sorted(Cars)}"
print(Final_2)
#Now we have the list in A to Z order after applying the sorted() Function
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Final_3 = f"Here is the original list again: {Cars}"
print(Final_3)
#As you can we restored list to original order

#Alternative code while using sorted() Function
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
print("Here is the original list:".title(), Cars)
print("\nHere is the sorted list:", sorted(Cars))
print("\nHere is the original list again:", Cars)
#Here we are not using the f-string

#The sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.

#Note: For the accurate results it is good to sort elements when they are all in lowercase because there are many ways python can interpret capital letters

#Printing a List in Reverse Order
#To reverse the original order of a list, you can use the reverse() method. 
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
print(Cars)
Cars.reverse()
print(Cars)
#The order has been reverse. reverse method does not reverse in aplhabetic order but rather from last to first.
#Notice that to use reverse we must have first output of list, you can not reverse somethng you haven't arranged
#Note: The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying reverse() to the same list a second time.

#Finding the Length of a List
#You can quickly find the length of a list by using the len() function
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
print(len(Cars))







