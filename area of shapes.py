def sq():
    a = int(input("Enter side: "))
    print("Area of square =", a * a)

def rect(a, b):
    print("Area of rectangle =", a * b)

def tri():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    print("Area of triangle =", 0.5 * b * h)

def cir():
    r = int(input("Enter radius: "))
    print("Area of circle =", 3.14 * r * r)

print("1. Square")
print("2. Rectangle")
print("3. Triangle")
print("4. Circle")

ch = int(input("Enter any choice: "))

if ch == 1:
    sq()

elif ch == 2:
    a = int(input("Enter length: "))
    b = int(input("Enter breadth: "))
    rect(a, b)

elif ch == 3:
    tri()

elif ch == 4:
    cir()

else:
    print("Invalid choice")
