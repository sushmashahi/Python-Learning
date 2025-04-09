from loguru import logger
import time
Values = ["orange","apple","bannaa","cherry","guava"]
count = len(Values)-1# yaha length zero se count hota hai na toh isliye aise kr rhe
while(count>0):
    print(Values[count]) #value print hote jayega isko stop ke liye condition laga hoga
    count-=1 # 0 VLAUE loop ke baad o + 1 ,vhir 0 +2 bt 4 plus 1 5 ke liye out of range toh negative krna hoga
    time.sleep(5)# value 5 ke baad print hoga
