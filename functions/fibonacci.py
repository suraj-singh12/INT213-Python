# program to print fibonacci series upto n terms
def fibonacci(terms):
    first = 0
    second = 1
    
    print(first,second,end=" ")
    terms -= 2
    while terms > 0:
        next = first + second
        first = second
        second = next
        
        print(next,end=" ")
        terms -= 1
    print()


n = int(input(("Enter the number of terms(>2): ")))
fibonacci(n)
