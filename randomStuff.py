l = [[i, i * i] for i in range(1, 101)]
print(l)

l = tuple(l)
print(l)

print(*l)

print("")

l = [(i, i * i) for i in range(1, 101)]
print(*l)

l = tuple(l)
print(l)

print(*l)
