MT = ("abcde",21,48,"oi")

print(len(MT))
print(type(MT))

MT1 = tuple((1,2,3,4,5))

print(MT[0])
print(MT[-1])
print(21 in MT)


#print(type(MT1))
print(MT1)
MT1 = list(MT1)
MT1.append("abc")
MT1[0] = "a"
MT1.remove(3)
#print(type(MT1))
#print(MT1)
MT1 = tuple(MT1)
#print(type(MT1))
print(MT1)
oi = MT + MT1
print(oi)