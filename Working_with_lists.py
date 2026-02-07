#In this chapter you’ll learn how to loop through an entire list using just a few lines of code, regardless of how long the list is. Looping allows you to take the same action, or set of actions, with every item in a list. As a result, you’ll be able to work efficiently with lists of any length, including those with thousands or even millions of items.

#Looping Through an Entire List
#When you want to do the same action with every item in a list, you can use Python’s for loop.

Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(Car)
#You must put am indentation block (A Tab space) before print

Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(Car.upper())
#If we add some juice like upper case etc

#A Closer Look at Looping
#The name given to the temporary variable in the for loop can be anything however it is good to choose somethign reasonable maybe closer to the name of the list

#Doing More Work Within a for Loop
#You can do just about anything with each item in a for loop.

Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(f"{Car.title()}, is a very good car")
#We just told each car in our list that it is a good car

#You can also write as many lines of code as you like in the for loop. Every indented line following the line for magician in magicians is considered inside the loop, and each indented line is executed once for each value in the list.
Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(f"{Car.title()}, is not only the fastest but {Car.upper()} is also the most expensive")
    print(f"It is better to only buy {Car.title()} when you have good money and good roads.")
#So literally py will print the same codes for each item and then go onto the other item and do the same

#So to remove the congession we can use the \n like to space our sentences
Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(f"{Car.title()}, is not only the fastest but {Car.upper()} is also the most expensive")
    print(f"It is better to only buy {Car.title()} when you have good money and good roads. \n")

#Doing Something After a for Loop
#What happens once a for loop has finished executing? You wanna maybe move to another program etc
#Any lines of code after the for loop that are not indented are executed once without repetition.
Cars = ['Benz', 'Toyota', 'Mazda', 'Maybach', 'Subaru']
for Car in Cars:
    print(f"{Car.title()}, is not only the fastest but {Car.upper()} is also the most expensive")
    print(f"It is better to only buy {Car.title()} when you have good money and good roads. \n")
print(f"All in all Cars are beautiful")