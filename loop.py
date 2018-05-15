from __future__ import print_function

print("List Itereation")
l = ["Geeks", "for", "geeks"]
for i in l:
	print(i)


print("\ntouple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)

print("\nString Iteration")
s = "GeeksForGeeks"
for i in s:
	print(i)

print("\nDictionary")

d = dict()
d['abc'] = 123
d['def'] = 456
for i in d:
	print("%s %d"%(i,d[i]))


for i in range(1,5):
	for j in range(i):
		print(i, end=" ")
	print() 
