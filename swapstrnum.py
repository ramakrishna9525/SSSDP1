

x = input("Enter 1st input : ")
y = input("Enter 2nd input : ")

print("Before swap : ", f"x={x!r}", f"y={y!r}")

x, y = y, x

print("After swap : ", f"x={x!r}", f"y={y!r}")

#here !r refers to object with string