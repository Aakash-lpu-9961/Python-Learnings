# Recursion : Recursive V/S Iterative Approach

print("This is a test program, Learning20.py")

# def function1(str1):
#     function1(str1)
#     # print("This is" + str1)
#
# function1("Aakash")



# n! = n * (n-1) * (n-2) * (n-3) ........* 1
# n! = n * (n-1)!


def factorial_iterative(n):
    """

    :param n: Integer
    :return: n * (n-1) * (n-2) * (n-3) *........* 1

    """
    fac =1
    for i in range(n):
        fac = fac * (i+1)
    return fac

p = int(input("Enter Number:"))
print("Factorial using Iterative Method: \n", factorial_iterative(p))







def factorial_recursive(n):
    """

    :param n:Integer
    :return:  n * (n-1) * (n-2) * (n-3) *........* 1

    """

    if n ==0 or n== 1:
        return 1
    else:
        return n * factorial_recursive(n-1)


q = int(input("Enter Number:"))
print("Factorial using Recursive Method: \n", factorial_recursive(q))