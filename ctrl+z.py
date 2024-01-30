stack=[]
def pash(x):        #string have deleting in range
    stack.append(x)
strin=[]
def pash1(a):       #string with one delet
    strin.append(a)
stack2=[]
def pash2(x):       #the range of string are deleting
    stack2.append(x)
stac3=[]            #the opration

def display(): #function to return the last elemnt and print him
    if len(stac3)<1:
        print("there is nothing to return")
    else:
        n=stac3.pop(0)
        if n==1:
                xx=strin.pop(0)
                x.append(xx)
            #print(x)
        elif n==2:
            b=stack2.pop(0)
            a=stack2.pop(0)
            for i in range(a,b+1):
                hi=stack.pop(0)
                x.insert(i,hi)
        
    text=''.join(x)
    print("result = ",text)

a=input("inter the string :") #the main string that we are procsses it
print(a)
x=list(a)  

while True:
    print("inter opreation 1-dlet 1 char 2-delet range 3-break")
    choise=int(input())
    if choise == 1:
        x1=x.pop()
        pash1(x1)
        print(x)
        print(strin)
        stac3.append(choise)
        
    if choise == 2:
        a1=int(input("inter range 1"))
        b1=int(input("inter range 2"))
        if a1>len(x) or b1>len(x):
            print("out of the range")
        else:
            pash2(a1)
            pash2(b1)
            for i in range(a1,b1+1):
                    pash(x[i])
            
            del x[a1:b1+1]             
            print (x)
            stac3.append(choise)
        
    if choise == 3:
        break

strin.reverse()
stac3.reverse()
stack2.reverse()
gg=len(stac3)
while gg!=0: #check the number of opration thet we do in string
    choise=int(input("1- ctrl+z  2- break"))
    if choise==1:
        display()
        gg-=1
    else:
        break