# The lord of the rings

def samechars(s1,s2,prev):

    n1=len(s1)
    n2=len(s2)

    #print s1,s2,prev,n1,n2
    #Stopping Conditions:
    if n2==0:
        return True
    if n1==0:
        return False
    
    curr=s2[0]

    #Recursive Calls:
    

    if prev!=curr:

        if s1[0]==curr:
            prev=curr
            return samechars(s1[1:n1],s2[1:n2],prev)
        else:
            return samechars(s1[1:n1],s2,prev)
    elif curr==prev:
        return samechars(s1,s2[1:n2],prev)


def main():
    while True:
        s1=raw_input("Enter s1: ")
        s2=raw_input("Enter s2: ")

        if samechars(s1,s2,""):
            print "True\n"
        else:
            print "False" 

main()
    
