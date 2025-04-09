from loguru import logger
paragraph = "I am good girl i am doing the python code i am also learning the pandas numpy"
paragraph_list = paragraph.lower().split(" ")
print(paragraph_list)
count = 0

for letter in paragraph_list:
    if letter == "i":
        count = count+1
    else:
        continue
    logger.info(f"The valueof the count is {count}")
