# write a recursive function to calculate the sum of first n natural numbers

n=5
def sum(n):
    if n==1:
        return 1
    else:
        return n + sum(n-1)
s=sum(n)
print(f"The sum of {n} natural number is = {s}") #using f_string