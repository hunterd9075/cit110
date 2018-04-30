# CTI-110 
# P3HW1 - Age Classifier 
# DeOnna Hunter
# 4/30/2018

def main ():
    

    age = int(input("Please enter age to be examined.  "))



        
    if age<=1:
        print ("This person is an infant.")

    elif age<13 :
        print ("This person is a child.")

    elif age<20:
        print ("This person is a teenager.")

    else:
        age>=20
        print ("This person is an adult.")

main()
