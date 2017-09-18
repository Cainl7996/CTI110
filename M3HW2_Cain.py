# CTI-110
# Larissa Cain
# M3HW2 - Software Sales
# 9/13/2017

def main():
    #This program displays the number of packages purchased and
    #defines it's discount, then creates a total with discount applied.

    package = 99.00
    quantity = int(input('Packages ordered: '))
    #discount = 0

    if quantity < 10:
        print('No Discount')
    elif quantity < 20:
        discount = .1
        print('Discount = 10%')
    elif quantity < 50:
        discount = .2
        print('Discount = 20%')
    elif quantity < 100:
        discount = .3
        print('Discount = 30%')
    elif quantity >= 100:
        discount = .4
        print('Discount = 40%')

    #Creating a variable for subTotal subdiscount and totalPrice
        
    subTotal = quantity * package        
    subDiscount = subTotal * discount    
    totalPrice = subTotal - subDiscount

    print('subTotal is:', subTotal)
    print('Discount is:', subDiscount)
    print('totalPrice is:', totalPrice)
    

main()


    
