# CTI-110 
# P3HW2 - Software Sales 
# DeOnna Hunter
# 4/30/2018

def main ():
    

    quantity = float(input("How man package do you want to purchase?  "))



        
    if quantity<10:
        print ("I'm sorry. There is no discount based on your purchase volume. Your cost is: $",99*quantity)

    elif quantity <20 :
        print ("You recieved 10% off. Your cost is: $",89.1*quantity)

    elif quantity <50:
        print ("You recieved 20% off. Your cost is: $",79.2*quantity)

    elif quantity <100:
        print ("You recieved 30% ofr. Your cost is: $",69.3*quantity)

    else:
        quantity>100
        print ("You recieved 40% off. Your cost is: $",59.4*quantity)

main()
