def direction(l):
    output = []

    for e in l:
        e = e.replace('e', 'w')
        e = e.replace('a', 'e')
        e = e.replace('E', 'W')
        e = e.replace('A', 'E')

        output.append(e)

    return output


print(direction(["east", "EAST", "eastEAST"]) == ["west", "WEST", "westWEST"])
print(direction(["eAsT EaSt", "EaSt eAsT"]) == ["wEsT WeSt", "WeSt wEsT"])
print(direction(["east EAST", "e a s t", "E A S T"]) == ["west WEST", "w e s t", "W E S T"])
