x = 100
y = 150
z = 300

if (x>= y) and (x >= z):
   largest = x
elif (y >= x) and (y >= z):
   largest = y
else:
   largest = z

print("The largest number between",x,",",y,"and",z,"is",largest)
