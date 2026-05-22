def fun3(a, b, c, d):
    print(a, b, c, d)

def fun2(**b):
    print(b)
    fun3(**b)       #unpacking a=75 etc
fun2(a=75, b=30, c=40, d=70)