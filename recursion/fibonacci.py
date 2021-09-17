#fibonacci series: 0 1 1 2 3 5 8 13

def fibonacci(terms,first,second,next=1):
    if terms > 2:
        next = first + second
        first = second
        second = next
        return fibonacci(terms-1,first, second,next)
    else:
        return next

numberOfTerms = int(input("Enter no of terms(>2): "))
print(fibonacci(numberOfTerms,0,1))
