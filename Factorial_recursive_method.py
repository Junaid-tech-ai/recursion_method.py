# write a recursive function to calculate the factorial of (n) number.
n=7
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
f=factorial_recursive(n)
print(f"The factorial of {n} is {f}" )

# ----------------------------------

