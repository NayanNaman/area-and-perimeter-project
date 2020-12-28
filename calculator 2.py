print ("This is a CALCULATOR which finds perimeter or area of the shapes given below:")
print ("1)Square")
print ("2)Rectangle")
print ("3)Rhombus")
print ("4)Parallelogram")
#1="Square"
#2="Rectangle"
#3="Rhombus"
#4="Paralellogram"
y=int(input("Please enter the serial number of the shape that you want to find here:"))
#your shape
if y<1:
    print ("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
    y=int(input("\nPlease enter the serial number of the above given shape here:"))
elif y>4:
    print ("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
    y=int(input("\nPlease enter the serial number of the above given shape here:"))
elif y<5 and y>0:
    print ("\nYou chose:")
    if y<2 and y>0:
        print ("Square")
    elif y<3 and y>1:
        print ("Rectangle")
    elif y<4 and y>2:
        print ("Rhombus")
    elif y<5 and y>3:
        print ("Parallelogram")
#mensuration choice
    print ("\nWhich of the following do you want to find?")
    print ("1) Perimeter")
    print ("2) Area")
    z=int(input("Please enter the serial number of the above given options: "))
    if z>2 or z<1:
        print("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
        print ("\nWhich of the following do you want to find?")
        print ("1) Perimeter")
        print ("2) Area")
        z=int(input("Please enter the serial number of the above given options: "))
    elif z>1 and z<3:
        print ("\nYou chose to find area")
    elif z>0 and z<2:
        print("\nYou chose to find perimeter")
  
#perimeter of square
    if y<2 and y>0 and z>0 and z<2:
        p1=int(input("\nPlease enter the length of the side of the square: "))
        a=p1*4
        print("\nThe perimeter of the square is: ",int(a))
#area of square
    elif y<2 and y>0 and z>1 and z<3:
        a1=int(input("\nPlease enter the length of the side of the square: "))
        b=a1*a1
        print("\nThe area of the square is: ",int(b))
#perimeter of rectangle
    elif y<3 and y>1 and z>0 and z<2:
        p2l=int(input("\nPlease enter the length of the rectangle: "))
        p2b=int(input("Please enter the breadth of the rectangle: "))
        c=2*(p2l+p2b)
        print("\nThe perimeter of the rectangle is: ",int(c))
#area of the rectangle
    elif y<3 and y>1 and z>1 and z<3:
        a2l=int(input("\nPlease enter the length of the rectangle: "))
        a2b=int(input("Please enter the breadth of the rectangle: "))
        d=a2l*a2b
        print("\nThe area of the rectangle is: ",int(d))
#perimeter of rhombus
    elif y<4 and y>2 and z>0 and z<2:
        p3=int(input("\nPlease enter the length of the side of the rhombus: "))
        e=p3*4
        print("\nThe perimeter of the rhombus is: ",int(e))
#area of rhombus
    elif y<4 and y>2 and z>1 and z<3:
        a3=int(input("\nPlease enter the length of the side of the rhombus: "))
        f=a3*a3
        print("\nThe area of the rhombus is: ",int(f))
#perimeter of parallelogram
    elif y<5 and y>3 and z>0 and z<2:
        p4l=int(input("\nPlease enter the length of the parallelogram: "))
        p4b=int(input("Please enter the breadth of the parallelogram: "))
        g=2*(p4l+p4b)
        print("\nThe perimeter of the parallelogram is: ",int(g))
#area of parallelogram
    elif y<5 and y>3 and z>1 and z<3:
        a4l=int(input("\nPlease enter the base of the parallelogram: "))
        a4b=int(input("Please enter the height of the parallelogram: "))
        h=a4l*a4b
        print("\nThe area of the parallelogram is: ",int(h))

#second time
#second time

for x in range (1,1000000001):
    print("\nDo you want to continue?")
    print ("1)Yes")
    print("2)No")
    w=int(input("Please enter the serial number of the above options here: "))
    if w<3 and w>1:
        print ("\nTHANK YOU FOR USING THIS CALCULATOR!")
        break
    elif w>2 or w<1:
        print ("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
        print("\nDo you want to continue?")
        print ("1)Yes")
        print("2)No")
        w=int(input("Please enter the serial number of the above option here: "))
    
    if w>0 and w<2:
        print ("\nHere you go again.")
        print ("1)Square")
        print ("2)Rectangle")
        print ("3)Rhombus")
        print ("4)Parallelogram")
#1="Square"
#2="Rectangle"
#3="Rhombus"
#4="Paralellogram"
        y=int(input("Please enter the serial number of the shape that you want to find here:"))
#your shape
        if y>4:
            print ("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
            y=int(input("\nPlease enter the serial number of the above given shape here:"))
        print ("\nYou chose:")
        if y<2 and y>0:
            print ("Square")
        elif y<3 and y>1:
            print ("Rectangle")
        elif y<4 and y>2:
            print ("Rhombus")
        elif y<5 and y>3:
            print ("Parallelogram")
#mensuration choice
        print ("\nWhich of the following do you want to find?")
        print ("1) Perimeter")
        print ("2) Area")
        z=int(input("Please enter the serial number of the above given options: "))
        if z>2:
            print("\nINVALID, you didn't enter a number that was given in the options. TRY AGAIN!")
            print ("\nWhich of the following do you want to find?")
            print ("1) Perimeter")
            print ("2) Area")
            z=int(input("Please enter the serial number of the above given options: "))
        elif z>1 and z<3:
            print ("\nYou chose to find area")
        elif z>0 and z<2:
            print("\nYou chose to find perimeter")
#perimeter of square
        if y<2 and y>0 and z>0 and z<2:
            p1=int(input("\nPlease enter the length of the side of the square: "))
            a=p1*4
            print("\nThe perimeter of the square is: ",int(a))
#area of square
        elif y<2 and y>0 and z>1 and z<3:
            a1=int(input("\nPlease enter the length of the side of the square: "))
            b=a1*a1
            print("\nThe area of the square is: ",int(b))
#perimeter of rectangle
        elif y<3 and y>1 and z>0 and z<2:
            p2l=int(input("\nPlease enter the length of the rectangle: "))
            p2b=int(input("Please enter the breadth of the rectangle: "))
            c=2*(p2l+p2b)
            print("\nThe perimeter of the rectangle is: ",int(c))
#area of the rectangle
        elif y<3 and y>1 and z>1 and z<3:
            a2l=int(input("\nPlease enter the length of the rectangle: "))
            a2b=int(input("Please enter the breadth of the rectangle: "))
            d=a2l*a2b
            print("\nThe area of the rectangle is: ",int(d))
#perimeter of rhombus
        elif y<4 and y>2 and z>0 and z<2:
            p3=int(input("\nPlease enter the length of the side of the rhombus: "))
            e=p3*4
            print("\nThe perimeter of the rhombus is: ",int(e))
#area of rhombus
        elif y<4 and y>2 and z>1 and z<3:
            a3=int(input("\nPlease enter the length of the side of the rhombus: "))
            f=a3*a3
            print("\nThe area of the rhombus is: ",int(f))
#perimeter of parallelogram
        elif y<5 and y>3 and z>0 and z<2:
            p4l=int(input("\nPlease enter the length of the parallelogram: "))
            p4b=int(input("Please enter the breadth of the parallelogram: "))
            g=2*(p4l+p4b)
            print("\nThe perimeter of the parallelogram is: ",int(g))
#area of parallelogram
        elif y<5 and y>3 and z>1 and z<3:
            a4l=int(input("\nPlease enter the base of the parallelogram: "))
            a4b=int(input("Please enter the height of the parallelogram: "))
            h=a4l*a4b
            print("\nThe area of the parallelogram is: ",int(h))
