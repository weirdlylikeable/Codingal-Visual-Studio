def constantcomplexity(n):
    iterations=0
    print("Number of iterations to be performed is:", n)
    iterations+=1
    print("These many iterations have been performed:", iterations)

constantcomplexity(20)
constantcomplexity(60)

def OnTime(n):
    iterations1=0
    for i in range(1,n+1):
        iterations1+=1
    print("These many iterations have been performed:", iterations1)

OnTime(20)
OnTime(40)

def OnSquareTime(n):
    iterations2=0
    for i in range(0,n):
        for j in range(0,n):
            iterations2+=1
    print("When the value of n is",n, "the amount of iterations are:", iterations2)

OnSquareTime(7)
OnSquareTime(10)