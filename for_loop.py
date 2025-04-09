from loguru import logger
print("check")
Values = ["orange","Apple","Bannana"]
for fruits in Values:
    logger.info(fruits)
    #range method 
for i in range(1,5): #but here problem you are range from 1 to 5 but for dynamic case you have to count length than add range
    logger.info(i) #values 1 se 4 
for i in range(len(Values)):
    logger.info(i)
   # logger.info(f"The values of fruits {i} is {Values}") #The value of 0 ,1,2 is coming becaus eit count from 0 so to check from 1 we can use i +1
    logger.info(f"The values of fruits {i+1} is {Values[i]}")
