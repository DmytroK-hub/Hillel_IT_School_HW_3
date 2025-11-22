lst1 = [2, 32, 1, 9, 0, 2, 7, 21]

if len(lst1) > 0:
	x = lst1.pop()
	lst1 = [x] + lst1

print(lst1)