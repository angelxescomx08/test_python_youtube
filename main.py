pares_distintos = []
for x in range(3):
    for y in range(3):
        if x != y:
            pares_distintos.append((x, y))
print(pares_distintos)

pares_distintos = [(x,y)for x in range(3) for y in range(3) if x != y]
print(pares_distintos)