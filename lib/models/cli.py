# lib/cli.py
from star import Star
from director import Director
from movie import Movie


# See main menu
# welcome message, options:
# 0 exit program
# 1 See all stars
# 2 See all movies
# 3 See all directors
# when see all stars (1), options:
# 0 exit program
# 1 add/ create new star
# 2 find star by id
# 3 update star
# 4 delete star
# when find by id(2), get all others and options:
# 0 exit program
# 1 average gross
# 2 movies
# 3 topgrossing movie
# when 3 see all directors:
# 0 exit
# 1 find by id
# 1, get all others then:
# 0 exit
# 1 total royalties
# 2 stars worked with
# 3 movies
# 4 total gross


def exit_program():
    print("Goodbye!")
    exit()


def main():
    while True:
        menu1()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            all_stars = Star.get_all_stars()
            for star in all_stars:
                print(f"{star.id} | {star.name} | ${star.rate_per_movie:.2f}")

            menu2()
            choice2 = input(">")
            if choice2 == "0":
                exit_program()
            elif choice2 == "1":
                print("\nAdd new star:")
                star_name = input("Enter star name: ")
                star_rate = float(input("Enter rate per movie: 1"))
                new_star = Star.create(star_name, star_rate)
                print(f"\n***{new_star.name} | ${new_star.rate_per_movie:.2f}***")
                print("\nBack to main menu.")
            elif choice2 == "2":
                print("\nFind star by id:")
                starid = int(input("\n Enter star ID: "))
                star_by_id = Star.find_by_id(starid)
                print(f"\n***{star_by_id.name} | {star_by_id.rate_per_movie:.2f}***")
            elif choice2 == "3":
                pass
            elif choice2 == "4":
                pass
            else:
                print("Invalid choice")
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        else:
            print("Invalid choice")


def menu1():
    print(
        "\nWelcome to the film database, where you can explore \nmovies, their stars and directors and \nexecute CRUD, association, and aggregate operations."
    )
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. See all stars \n2. See all movies \n3. See all directors")


def menu2():
    print(
        "\nSelect your choice: \n0. Exit the program \n1. Add new star \n2. Find star by id \n3. Update star \n4. Delete star"
    )


if __name__ == "__main__":
    main()
