import sys
import random

def insertionSort(arr):
    for i in range(1,len(arr)):
        value=arr[i]
        position=i-1
        while position>=0 and arr[position]>value:
            arr[position+1]=arr[position]
            position-=1
        arr[position+1]=value
    print(arr)

def selectionSort(arr):
    for x in range(len(arr)):
        max_position=x
        #for y in range(1,x+1):
        for y in range(x+1, len(arr)):
            if(arr[y] < arr[max_position]):
                max_position=y
        temp=arr[x]
        arr[x]=arr[max_position]
        arr[max_position]=temp
    print(arr)

arr=[]
if (len(sys.argv)==2):
    size=1000
    arr=random.sample(range(size),size)

    if(sys.argv[1]=="G=I"):
        insertionSort(arr)
    elif(sys.argv[1]=="G=S"):
        selectionSort(arr)
    else:
        print("please check your argument")

if (len(sys.argv)==4):
    s=sys.argv[1]
    n=s.split("N=")
    size=int(n[1])

    if(sys.argv[2]=="S=A"):
        for i in range(size):
            arr.append(i)
    elif(sys.argv[2]=="S=R"):
        print("ent")
        arr=random.sample(range(size),size)
        print("exit")
    elif(sys.argv[2]=="S=D"):
        for i in range(size):
            arr.append(size-i)
    else:
        print("check 2nd argument")
        sys.exit(1)

    if(sys.argv[3]=="G=I"):
        print("ient")
        insertionSort(arr)
        print("iexit")
    elif(sys.argv[3]=="G=S"):
        print("Sent")
        selectionSort(arr)
    else:
        print("check 3rd argument")
        sys.exit(1)
