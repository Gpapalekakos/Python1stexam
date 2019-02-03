usernumber=int(input("Give me a number\n"))
allnums=[]#listaariumwn
def SieveOfEratosthenes(n):
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            allnums.append(p)


    allnumscounter=[0]*len(allnums)
    number=n
    a=len(allnums)
    restart=True
    while restart:
        for i in range(0,a):
            d=allnums[i]
            b=n%d
            if b==0 and n>1:
                restart=True
                n=n/d
                allnumscounter[i]=allnumscounter[i]+1
                i=0
                break
            elif b!=0 and n>1:
                i=i+1
                restart=False
            else:
                restart=False
                break


    print ('Your number',number,' is the product of:')
    token=0
    counter=len(allnumscounter)
    for i in range(0,counter):
        if allnumscounter[i]!=0:
            print(allnums[i],'**',allnumscounter[i])
            i+=1
        else:
            token+=1
            i+=1
    if token==len(allnumscounter):
        print("YOUR NUMBER IS PRIME")
#if there is at least one allnumscounter[i]!=0 nothing will be added in token .In this way ,it will never
#be equal to len(allnumscounter)


def myltiply(number):
    if number==0:#elegxos
        number=int(input("That's zero.TRY AGAIN\n"))
    elif number<0 :
        number=number*-1
    SieveOfEratosthenes(number)


myltiply(usernumber)
