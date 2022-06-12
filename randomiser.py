import random
f=open("words.txt").readlines()
f2=open("words1.txt", "w")
random.shuffle(f)
for x in f:
	f2.write(x)
print("Done")