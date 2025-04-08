a = ["abc",2,3,True,False,6,7]
b=[2,3]
#Positive and Negative Indexing
print(a[-1],a[1],a[-3])
#Range of index
print(a[1:4])
#change List value
a[1] = "sushma"
print(a)
#append to add the item at the end
a.append(4)
print(a)
#to insert item at the specific  index
a.insert(1,"sush")
#length method
print(len(a))
#add
c = a + b
print(c)
#reverse
a = a[::-1]
print(a)
#pop method is to dlete the item if pass empty it will consider the last element
print(a.pop())
print(a.pop(2)) #IT WILL delete second item
#Remove Method
a.remove(4)
print(a)