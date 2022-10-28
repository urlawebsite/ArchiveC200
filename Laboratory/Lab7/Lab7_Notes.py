print([2*i for i in range(4)])

res = []
for i in range(4):
    res += [2*i]
print(res)

print([[i, j] for i in range(4) for j in range(3)])
