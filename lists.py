family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
print(family)

family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
print(family[1])

#So to know the position of the element in the list, you need to know that the elements are numbered from 0,1,2,3 etc in theor order from the left

family = ['Charles', 'Angella', 'Perry', 'mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
print(family[3].upper())

#So from there you can mix up the methods and strips and the lines and tabs etc

family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
just = f"{family[1]} \n{family[5]}"
print(just)

#You can request several elements from a list using an f-string. Just create variables with values and combine the values in one string with an f-string. You can also add methods

family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
promise = f"{family[1]} \n{family[3].lower()} \t{family[5]} \n\t{family[7]} \n{family[0].upper()}"
print(promise)

#When you need the last element in the list, you use index (-1)

family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
print(family[-1])

#You can even use elements from list to do other things like in a string

family = ['Charles', 'Angella', 'Perry', 'Mercy', 'Victor', 'Praise', 'Comfort', 'Trevor']
Dad = f"The Tindyebwas \n{family[0]} is the head of the family; He is the father in this family."
Mum = f"{family[1]} is the co-head of the family; She is the mother in this family."
Sisters = f"{family[2]}, {family[3]}, and {family[6]} are the sisters in this family."
Brothers = f"{family[4]}, {family[5]}, and {family[7]} are the brothers in this family."
Final = f"{Dad.title()} \n{Mum.title()} \n{Sisters.title()} \n{Brothers.title()}"
print(Final)

#Modifying Elements in a List. To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
print(Cars)
#Above code shows normal list printing

Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars[1] = 'Audi'
print(Cars)
#As you can see we have substituted the element (value) number 1 from Benz to Audi

#Adding Elements to a List - Ways
#1. Appending Elements to the End of a List (Adding items to list - added item goes to end of list)

Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars.append('Lexus')
print(Cars)
#So when we are appending (adding) element to list we do not need to use a variable

#We can even add(append) elements to an empty list
Cars = []
Cars.append('subaru'.title())
Cars.append('Benz')
Cars.append('Toyota')
Cars.append('Mazda')
Cars.append('lexus'.title())
print(Cars)
#So here I appended elements to an empty list and for some I added the title method

#Inserting Elements into a List: You can add a new element at any position in your list by using the insert() method. You do this by specifying the index of the new element and the value of the new item:
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars.insert(0, 'Range Rover')
print(Cars)
#Range Rover was insterted at position 0

#Removing elements from list: If you know the position of the item you want to remove from a list, you can use the del statement
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
del Cars[1]
print(Cars)
#As you can see 'Benz' has been deleted from list
#you can no longer access the value that was removed from the list after the del statement is used.

#Removing an Item Using the pop() Method
#The pop() method removes the last item in a list, but it lets you work with that item after removing it. 
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars_popped = Cars.pop()
print(Cars)
print(Cars_popped)
#We start by defining and printing the list Cars. Then we pop a value from the list, and assign that value to the variable Cars_popped 2. We print the list 3 to show that a value has been removed from the list. Then we print the popped value 4 to prove that we still have access to the value that was removed. The output shows that the value 'Mazda' was removed from the end of the list and is now assigned to the variable popped_motorcycle:

#How might this pop() method be useful? Imagine that the cars in the list are stored in chronological order, according to when we owned them. If this is the case, we can use the pop() method to print a statement about the last car we bought:
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars_popped = Cars.pop()
Final = f"The lastest car I bought is a {Cars_popped.title()}"
print(Final)
#The lastest car I bought is a Mazda

#Popping Items from Any Position in a List
#You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses:
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars_popped = Cars.pop(0)
Final = f"The oldest car I bought is a {Cars_popped.title()}"
print(Final)
#Here because I added index position in (), I can use the car

#Recap about del statement and pop() method
#Remember that each time you use pop(), the item you work with is no longer stored in the list. If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.

#Removing an Item by Value
#Sometimes you won’t know the position of the value you want to remove from a list. If you only know the value of the item you want to remove, you can use the remove() method.
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
Cars_new = Cars.remove('Toyota')
print(Cars)
#Toyota has been removed

#You can also use the remove() method to work with a value that’s being removed from a list. Let’s remove the value 'Benz' and print a reason for removing it from the list:
Cars = ['Subaru', 'Benz', 'Toyota', 'Mazda']
too_expensive = 'Benz'
Cars.remove(too_expensive)
Final = f"I am taking the {too_expensive} because it is too expensive."
print(Final)






