
#Write a Python program that takes an integer input from the user and prints whether it is even or odd.
a = int(input("Enter the number: "))
if a%2 == 0:
 print("Even Number")
else:
 print("odd Number")
#Positive, Negative, or Zero
a = int(input("The number "))
if a>0:
 print("Postive Number")
elif a<0:
 print("Negative Number")
elif a==0:
 print("Neutral Mumber")
#Age Group Checker
#Take age as input and classify:Below 13: Child 13–19:Teenager 20–59: Adult60 and above: Senior
num = int(input("The number "))
if num<13:
 print("The child")
elif num >= 13 and num <= 19:
 print("Teenager")
elif num == 60:
 print("Adults")
elif num>= 60:
 print("Senior")
#Write a Python program that asks the user to enter their age, then prints the ticket price based on the following rules:👶 Below 5 years: Ticket is Free🧒 5 to 12 years: Ticket price is ₹100👦 13 to 17 years: Ticket price is ₹150👨 18 to 59 years: Ticket price is ₹250👴 60 and above: Ticket price is ₹120❌ Negative age or 0: Print "Invalid age"
Ticket = int(input("Enter the number"))
if num<=0:
 print("Invalid age")
elif Ticket<5:
 print("The ticket is free")
elif Ticket<=5 and Ticket<=12:
  print("The ticket price is 100")
elif Ticket<=13 and Ticket<=17:
 print("The ticket price is 250")
elif Ticket<=18 and Ticket<=59:
 print("The ticket price is 250")
else:
 print("The ticket price is 120")

 



