#max of two
def maximum(a,b):
    if a>=b:
        return a
    else:
        return b

maximum(2,4)

#prime number
start = 11
end = 25
for i in range(start,end+1):
    if i > 1:
        for j in range(0,i):
            if(i%j==0):
                break
            else: 
                print(i)