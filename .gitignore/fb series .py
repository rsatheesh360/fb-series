def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter no of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print (fibonacci(i))
    print (fibanocci(i))
