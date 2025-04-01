length =100
breadth =200
print(length,breadth)

#To check the ram location we can write the program like this
print(id(length), id(breadth))

#if we allocate the same value for length and braedth ram value will be also same only
length_1 =100
breadth_2 =100
print(id(length_1), id(breadth_2))
#to print the value we have to write the statement than add the variable name
print('the value of the length_1 is ',length_1)
