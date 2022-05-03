# * 찍기

for x in range(1, 6):
    for y in range(x, 5):
        print(' ', end='')
    for y in range(1, x+1):
        print('*', end=' ')
    print()


#print('Hello', end=' ')
#print('World')
'''
for i in range(0, 5):
	for j in range(0, 4-i):
		print(end=" ")
	for j in  range(0, i+1):
		print("*", end=" ")
	print()
'''