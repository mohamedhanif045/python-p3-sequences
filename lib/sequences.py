def print_fibonacci(length):
    fibonacci_list = []

    # Generate the Fibonacci sequence up to the given length
    for i in range(length):
        if i == 0:
            fibonacci_list.append(0)
        elif i == 1:
            fibonacci_list.append(1)
        else:
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    
    # Print the result
    print(fibonacci_list)
