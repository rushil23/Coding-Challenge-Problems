import random

def sort_k(L,n,k):
    for i in range(n-1):
        if (i==k):
            continue
        i_min=i
        for j in range(i,n):
            if (j!=k):
                if (L[i_min]>L[j]):
                    i_min=j
        L[i_min],L[i]=L[i],L[i_min]

def main():            
    n=10
    L=[3,1,2,4,5,10,9,8,7,6]

    for i in range(n):
         L[i]=random.randint(1,1000)
    print L
    k=5
    sort_k(L,n,k)
    print L
    
main()
