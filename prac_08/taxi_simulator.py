"""
CP1404 | Prac_08 | Dannielle Jones

"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi
MENU = "Q) uit, C) hoose taxi, D) rive \n>>> "


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0
    print("Let's Drive!")
    choice = input(MENU).upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
                # print(current_taxi)
            except IndexError:
                print("Invalid taxi choice")
        elif choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                # print(current_taxi)
                print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
                total_cost += current_taxi.get_fare()
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_cost))
        choice = input(MENU).upper()
    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
