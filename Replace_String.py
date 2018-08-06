# Replace String

def replace_str(newbase,target,rep,i):
    n=len(newbase)
    t=len(target)
    r=len(rep)
    if (target not in newbase)or(target==rep):
        return newbase
    if (i+t)>n:
        return newbase
    if (newbase[i:i+t]==target):
        newbase=newbase[:i]+rep+newbase[(i+t):]
        return replace_str(newbase,target,rep,i+r)
    else:
        return replace_str(newbase,target,rep,i+1)

    

def main():
    while True: 
        b=raw_input("Base: ")
        t=raw_input("Target: ")
        r=raw_input("Rep: ")

        print replace_str(b,t,r,0)

main()

    
