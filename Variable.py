length =100
breadth =200
print(length,breadth)

#To check the ram location we can write the program like this
print(id(length), id(breadth))

#if we allocate the same value for length and braedth ram value will be also same only
length_1 =100
breadth_2 =100
print(id(length_1), id(breadth_2))
#to print the value we have to write the statement than add the variable name /n for new line
print('The value of the length_1 is\n', length_1 / length)
#f string,.method
#for f-string is used to print the statement add varaible name in curly braces
print(f"The value of length {length_1}")
#we can print the value by adding multiple variable 
print(f"The value of length {length_1} ,{length}")
#Use f-strings if you are using Python 3.6+ (better readability & performance).
#Use .format() if you need compatibility with older Python versions.
#logging
import logging  # This is using the logging module

logging.basicConfig(level=logging.INFO)  # Set the logging level
logging.info("This is an info message.")  # This logs an info message




