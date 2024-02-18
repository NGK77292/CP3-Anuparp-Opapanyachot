floor = int(input("PyramidFloor: "))
star = 0
for i in range(floor):
    print((floor-(i+1)) * " " +(star+1)*"*")
    star +=2

