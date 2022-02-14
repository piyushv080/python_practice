#Print Table of Any Number 
num = int(input("Enter table which you want:\n"))

#using while loop
a = 0
while a<=num:  
    a+=1;
    print(num,'x',a,'=',(num*a))

#using for loop

for i in range(1, 11):
    print(num,'x',i,'=',(num*i))
    