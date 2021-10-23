def fibonacci(n):
    if(n<0): raise ValueError(f"{n} terms not possible for Fibonacci Series")
    elif(n==0): return []
    elif(n==1): return [1]
    elif(n==2): return [1,1]
    first = 1
    second = 1
    series = [1,1]
    for i in range(n):
        sum = first + second
        series.append(sum)
        first,second = second,sum
    return series

n = int(input("Enter length of Fibonacci Series: "))
print(f"Series: {fibonacci(n)}")