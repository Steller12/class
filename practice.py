f = [0, 1]
N = 10
for term in range(3, N + 1):
    value = f[term - 2] + f[term - 3]
    f.append(value)
print(f)