from random import randint

n, m = map(int, input().split())
print(n)
for i in range(m):
    print(randint(0, n - 1), randint(0, n - 1))
