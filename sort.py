if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    a=sorted(arr)
    n=max(a)
    i=0
    while(a[i]<n):
        x=a[i]
        i+=1
    print(x)
