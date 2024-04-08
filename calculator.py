import math

print("1. Arithmatic Operations")
print("2. Angles")
print("3. Percentages")
print("4. Exponential Operations (like squre & cube so on...)")
print("5. Rectangle")
print("6. TRiangle")
print("7. Cricle")
print("8. Sphere")
print("9. Exit")

choice = int(input("Enter your choice: "))
#Arithmatic
if choice == 1:
    frst_num=float(input("Enter the first number : "))
    scnd_num=float(input("Enter the second number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(frst_num + scnd_num)
    elif choice == 2:
        print(frst_num - scnd_num)
    elif choice == 3:
        print(frst_num * scnd_num)
    elif choice == 4:
        if scnd_num == 0:
            print("Cannot divide by zero")
        else:
            print(frst_num / scnd_num)
    elif choice == 5:
        print("Exit")
    else:
        print("Invalid choice")
#Angles
elif choice == 2:
    print("1- sin\t")
    print("2- cos\t")
    print("3- tan\t")
    print("4- cosec\t")
    print("5- sec\t")
    print("6- cot\t")
    print("7- Exit\n")
    
    deg=float(input("Enter the degree : "))
    choice = int(input("Enter your choice : "))
    num=float(deg * math.pi / 180)
    
    if choice == 1:
        result=math.sin(num)
        print(result)
    elif choice == 2:
        result=math.cos(num)
        print(result)
    elif choice == 3:
        result=math.tan(num)
        print(result)
    elif choice == 4:
        num1=math.sin(num)
        result = 1 / num1
        print(result)
    elif choice == 5:
        num1=math.cos(num)
        result = 1 / num1
        print(result)
    elif choice == 6:
        num1=math.tan(num)
        result = 1 / num1
        print(result)
    elif choice == 7:
        print("Exit")
    else:
        print("Invalid choice")
#Percentage
elif choice == 3:
    print("1- percent\t")
    print("2- exit\n")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        frst_num=float(input("Enter First number"))
        scnd_num=float(input("Enter Second number"))
        result=(frst_num / scnd_num) *100
        print(result)
    elif choice == 2:
        print("Exit")
    else:
        print("Invalid choice")
#Exponential
elif choice == 4:
    frst_num=float(input("Enter the first number : "))
    scnd_num=float(input("Enter the second number: "))
    result= frst_num ** scnd_num
    print(result)
#Rectangular
elif choice == 5:
    print("1. Perimeter of rectangular")
    print("2. Area of rectangular")
    print("3. Exit")
    
    length=float(input("Length of rectangular : "))
    width=float(input("Width of rectangular : "))
    choice=int(input("Enter your Choice : "))
    if choice==1:
        result=2*(length+width)
        print(result)
    elif choice==2:
        result=length*width
        print(result)
    elif choice==3:
        print("Exit")
    else :
        print("Invalid choice")
#Triangle
elif choice == 6:
    print("1. Scalene Triangle ")  #visambahau tribhuj
    print("2. Equilateral Triangle ") #sambahu tribhuj
    print("3. Isosceles Triangle ") #samdubahau tribhuj
    print("4. Basic Triangle Formula")
    print("5. Exit")
    
    choice = int(input("Enter your choice"))
    if choice == 1:
        print("1. Perimater of Scalene Triangle")
        print("2. Area of Scalene Triangle")
        print("3. Exit")
        
        choice = int(input("Enter your choice"))
        frst_num = int(input("Enter First side of the scalene triangle : "))
        scnd_num = int(input("Enter Second side of the scalene triangle : "))
        thrd_num = int(input("Enter Third side of the scalene triangle : "))
        if choice == 1: 
            result = frst_num + scnd_num + thrd_num
            print(result)
        elif choice == 2:
            num = (frst_num + scnd_num + thrd_num) / 2
            result = ((num - frst_num) * (num - scnd_num) * (num - thrd_num)) ** (1/2)
            print(result)
        elif choice == 3:
            print("Exit")
        else:
            print("Invalid choice")
    elif choice == 2:
        print("1. Perimater of Equilateral Triangle")
        print("2. Area of Equilateral Triangle")
        print("3. Exit")
        
        choice = int(input("Enter your choice"))
        frst_num = int(input("Enter First side of the equilateral triangle : "))
        
        if choice == 1:
            result = 3 * frst_num 
            print(result)
        elif choice == 2:
            result = ((3**0.5)/4)*(frst_num**2)
            print(result)
        elif choice == 3:
            print("Exit")
        else:
            print("Invalid choice")
    elif choice == 3:
        print("1. Perimater of Isosceles Triangle")
        print("2. Area of Isosceles Triangle")
        print("3. Exit")
        
        choice = int(input("Enter your choice"))
        
        frst_num = int(input("Enter the Base of Isosceles Triangle"))
        scnd_num = int(input("Enter same side value of the isosceles triangle : "))
        # thrd_num = int(input("Enter Second side of the isosceles triangle : "))
        
        if choice == 1:
            #preimeter = 2a + b ||where b = base & a = same side value
            result = frst_num + 2 * scnd_num 
            print(result)
        elif choice == 2:
            height =float((scnd_num ** 2) - ((frst_num ** 2)/4) ** 0.5)
            result = (frst_num * height) / 2 
            print(result)
        elif choice == 3:
            print("Exit")
        else:
            print("Invalid choice")
    elif choice == 4:
        print("1. Perimater of Right Angle Triangle Formula")
        print("2. Area of Right Angle Triangle Formula")
        print("3. Exit")
        
        choice = int(input("Enter your choice"))
        
        frst_num = int(input("Enter Base of the Right Angle Triangle : "))
        scnd_num = int(input("Enter Perpendicular side of the Right Angle Triangle : "))
        thrd_num = int(input("Enter Hypotenuse side of the Right Angle Triangle : "))
        
        if choice == 1:
            result = frst_num + scnd_num + thrd_num
            print(result)
        elif choice == 2:
            result = (frst_num * scnd_num) / 2
            print(result)
        elif choice == 3:
            print("Exit")
        else:
            print("Invalid choice")
    elif choice == 5:
        print("Exit")
#Circle

elif choice == 7:
    print("1. Perimeter of Circle")
    print("2. Area of Circle")
    print("3. Exit")
    
    choice = int(input("Enter your choice"))
    num = float(input("Enter the Radius"))
    
    if choice == 1:
        result = 2 * math.pi * num
        print(result)
    elif choice == 2:
        result = math.pi * num ** 2
        print(result)
    elif choice == 3:
        print("Exit")
    else:
        print("Invalid choice")

#Sphere 

elif choice == 8:
    print("1. Diameter of Sphere")
    print("2. Circumference of Sphere")
    print("3. Surface Area of Sphere")
    print("4. Volume of Sphere")
    print("5. Exit")
    
    choice = int(input("Enter your choice"))
    num = int(input("Enter the radius of the sphere"))
    
    if choice == 1:
        result = 2 * num
        print(result)
    elif choice == 2:
        result = 2 * math.pi * num
        print(result)
    elif choice == 3:
        result = 4 * math.pi * num ** 2
        print(result)
    elif choice == 4:
        result = 4 * math.pi * num ** 3
        print(result)
    elif choice == 5:
        print("Exit")
    else:
        print("Invalid choice")

#Cylinder

elif choice == 9:
    print("Exit")
else:
    print("please Enter a valid choice")