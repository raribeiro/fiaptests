a = int(input('Enter number 1'))
b = int(input('Enter number 2'))
c = int(input('Enter number 3'))
d = int()
if a > b:
	d = a
	a = b
	b = d
if b > c:
	d = b
	b = c
	c = d
print(c);
