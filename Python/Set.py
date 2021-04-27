yo = {"set",0,10,4.5,"yoyo"}
print(yo)
print(type(yo))
print(len(yo))
for value in yo:
	print(value)
print()
print(0 in yo)
yo.add("sasha")
print(yo)
yo.add("sasha")
print(yo)
batata = {33}
yo.update(batata)
print(yo)
b = [0,5,10]
yo.update(b)
print(yo)
yo.remove(0)
yo.discard(1)
print(yo)
yo.pop()
print(yo)


print()
print()
a = {2,4,6,8,10,12,14,16,18,20}
b = {3,6,9,12,15,18,21,24,27,30}
print(b)
print(a)
#a.intersection_update(b)
c = a.intersection(b)
print(a) 
print(b) 
print(c)