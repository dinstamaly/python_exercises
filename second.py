
def fact(a):
    if a == 0:
        return 1
    return a * fact(a-1)


while True:
    x = int(input())
    if x == -1:
        break
    print(fact(x))
