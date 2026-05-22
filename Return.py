def Sum(*a):
    return sum(a)
x = Sum(1,2,7,5,7,9,8)
if x%2==0:
    print(f"Even:{x}")
else:
    print(f"odd:{x}")
