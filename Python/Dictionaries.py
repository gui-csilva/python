meudic = {
	"jogo": "Fortnite",
	"tipo": "Battle Royale",
	"ano": 2017
}

print(meudic)
print(type(meudic))
print(len(meudic))
print(meudic["jogo"])
print(meudic.get("ano"))
a = meudic.values()
print(a)
b = meudic.keys()
print(b)
c = meudic.items()
print(c)

meudic["season"] = 6
meudic["chapter"] = 2
print(meudic)
print(a)
print(b)
print(c)

meudic.update({"bom jogador" : "pro player"})
print(meudic)

meudic.pop("bom jogador")
print(meudic)
meudic.popitem() #deleta o último
print()
print("printando as keys do meu dicionário")
for k in meudic:
	print(k)
	print(meudic[k])
	print()
#print()
#for k in meudic:
#	print(meudic[k])

print("fazendo loops")
for x in meudic.keys():
	print(x)
print()
for x in meudic.values():
	print(x)
print()
for k,v in meudic.items():
	print(k)
	print(v)