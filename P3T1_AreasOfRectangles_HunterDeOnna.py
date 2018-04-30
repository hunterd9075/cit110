# CTI-110 
# P3T1_AreasOfRectangles.py
# DeOnna Hunter
# 4/30/18

# R1 Dimensions
length1 =  int(input("Enter the length of Rectangle 1: "  ))

width1 = int(input("Enter the width of Rectangle 1: "  ))

#R2 Dimensions 
length2 =  int(input("Enter the length of Rectangle 2: "  ))

width2 = int(input("Enter the width of Rectangle 2: "  ))

#R1 and R2 Area Calculations

area1 = length1 * width1

area2 = length2 * width2

#Which is bigger

if area1>area2:
    print ("Rectangle 1 is bigger.")

elif area2>area1:
     print ("Rectangle 2 is bigger")

else:
    print ("They are both equal in area.")

