import sys
from restaurant import Restaurant

message = '''
Enter for  
1) Add customer
2) Display count 
1) Exit
'''
if __name__ == '__main__':
    restaurant = Restaurant()
    restaurant.work()
    while True:
        try:
            option = int(input(message))

            if option == 1:
                restaurant.on_new_customer()
            elif option == 2:
                print("Cusomers left in restaurant %d" % restaurant.customers)
            elif option == 3:
                print("Bye!!!")
                sys.exit(0)

        except Exception:
            continue
