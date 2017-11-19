# first_food = input("Name your favourite food :")
# print(first_food)
# second_food = input("Name your next favourite food :")
# print(second_food)
# print("Your favourite foods are " + first_food + " and " + second_food)
# input("press any button to exit!")

# bill = float(input("Type the amount on your bill"))
# print("The bill incuding the tip is: " + str(bill * 1.15))

car_price = float(input("Enter the base price of the car: "))
tax = 0.1
license_fee = 0.04
dealer_prep = 400
dest_charges = 350

print("The total on road drive away cost of the vehicle is " + str((car_price * (1 + tax) * (1 + license_fee)) + dealer_prep + dest_charges))

input("Press any key to exit")