def printFizzBuzzCuzz(n):
    for i in range(1, n + 1):
        fizzBuzzCuzzString = ""
        if i % 3 == 0:
            fizzBuzzCuzzString += "fizz"
        if i % 5 == 0:
            fizzBuzzCuzzString += "Buzz"
        if i % 7 == 0:
            fizzBuzzCuzzString += "Cuzz"
        if i % 5 != 0 and i % 3 != 0 and i % 7 != 0:
            fizzBuzzCuzzString = str(i)
        print(fizzBuzzCuzzString)
        
    return

 
printFizzBuzzCuzz(int(input()))






#range(1, n +1) 