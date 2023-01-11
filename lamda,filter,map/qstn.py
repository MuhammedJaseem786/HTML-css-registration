# write a program to create a lamda function that adds 15 to given number passed in as an argument,
#also create a lamda function that multiplies argument x with argument y and print the results.

x = lambda a : a + 15
print(x(4))

a = lambda x,y: x * y
print(a(5,8))

tuple = [('english',88),('science',90),('maths',97),('social science',82)]
tuple.sort(key=lambda a:a[1],)
print(tuple)
