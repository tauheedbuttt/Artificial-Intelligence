def menu():
    print("1 - Meter to Kilometer")
    print("2 - Kilometer to Meter")
    print("3 - Centimeter to Meter")
    print("4 - Centimeter to Milimeter")
    print("0 - Quit")
    choice = int(input("Choice: "))
    return choice

def meter_to_kilometer(meter):
    return meter/1000
def kilometer_to_meter(kilometer):
    return kilometer*1000
def centimeter_to_meter(centimeter):
    return centimeter/100
def centimeter_to_milimeter(centimeter):
    return centimeter*10

choice = 1
while(choice!=0):
    choice = menu()
    if(choice == 1):
        meter = int(input("Meter: "))
        print(f"Kilometer: {meter_to_kilometer(meter)}")
    elif(choice == 2):
        kilometer = int(input("Kilometer: "))
        print(f"Meter: {kilometer_to_meter(kilometer)}")
    elif(choice == 3):
        centimeter = int(input("Centimeter: "))
        print(f"Meter: {centimeter_to_meter(centimeter)}")
    elif(choice == 4):
        centimeter = int(input("Centimeter: "))
        print(f"Milimeter: {centimeter_to_milimeter(centimeter)}")
    elif(choice == 0):
        print("Goodbye!!")
    else:
        print("Invalid Input, Try Again\n")
