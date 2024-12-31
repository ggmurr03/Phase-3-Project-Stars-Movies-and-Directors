# lib/cli.py
from star import Star
from director import Director
from movie import Movie


# See main menux
# welcome message, options:x
# 0 exit programx
# 1 See all starsx
# 2 See all moviesx
# 3 See all directorsx
# when see all stars (1), options:x
# 0 exit programx
# 1 add/ create new starx
# 2 find star by idx
# 3 update starx
# 4 delete starx

# when find by id(2), get all others and options:
# 0 exit programx
# 1 average grossx
# 2 moviesx
# 3 topgrossing moviex


# when 3 see all directors:

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
            print(
                """
 ______  _______  ______   ______   ______ 
/ |        | |   | |  | | | |  | \ / |     
'------.   | |   | |__| | | |__| | '------.
 ____|_/   |_|   |_|  |_| |_|  \_\  ____|_/

        """
            )

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
                print("\nBack to main menu.")
            elif choice2 == "3":
                print("\nUpdate star")
                print("\nFind star to update by id: ")
                staridupdate = int(input("\n Enter star ID: "))
                star_by_id_update = Star.find_by_id(staridupdate)
                star_by_id_update.name = input("Update name: ")
                star_by_id_update.rate_per_movie = float(
                    input("Update earnings per movie: ")
                )
                star_by_id_update.update()
                print(
                    f"{star_by_id_update.name} | ${star_by_id_update.rate_per_movie:.2f}"
                )
            elif choice2 == "4":
                print("\nDelete star")
                print("\nFind star to delete by id: ")
                stariddelete = int(input("\n Enter star ID: "))
                star_to_delete = Star.find_by_id(stariddelete)
                star_to_delete.delete()
            elif choice2 == "5":
                print(
                    "\n0. Exit the program \n1. Average gross \n2. Star's movies \n3. Star's top grossing movie \n"
                )
                movie_list = Movie.get_all_movies()
                choice3 = input(">")
                if choice3 == "0":
                    exit_program()
                elif choice3 == "1":
                    print("\nFind star by id: ")
                    staridaverage = int(input("\n Enter star ID: "))
                    star_for_movies_average = Star.find_by_id(staridaverage)
                    print(star_for_movies_average.average_gross())

                elif choice3 == "2":
                    print("\nFind star by id: ")
                    staridformovies = int(input("\n Enter star ID: "))
                    star_for_movies = Star.find_by_id(staridformovies)
                    print(star_for_movies.movies())
                elif choice3 == "3":
                    print("\nFind star by id: ")
                    staridfortop = int(input("\n Enter star ID: "))
                    star_for_top_grossing = Star.find_by_id(staridfortop)
                    print(star_for_top_grossing.top_grossing_movie())
                else:
                    print("Invalid choice")

            else:
                print("Invalid choice")
        elif choice == "2":
            all_movies = Movie.get_all_movies()
            print(
                """
 _________   ______   _     _  _____  ______  ______ 
| | | | | \ / |  | \ | |   | |  | |  | |     / |     
| | | | | | | |  | | \ \   / /  | |  | |---- '------.
|_| |_| |_| \_|__|_/  \_\_/_/  _|_|_ |_|____  ____|_/
                  
                  """
            )
            for movie in all_movies:
                print(
                    f"{movie.title} | {movie.star_id} | {movie.director_id} | ${movie.box_office:.2f} | {movie.genre}"
                )
        elif choice == "3":
            all_movies = Movie.get_all_movies()
            all_directors = Director.get_all_directors()
            print(
                """
 _____   _____  ______   ______  ______ _______  ______   ______   ______ 
| | \ \   | |  | |  | \ | |     | |       | |   / |  | \ | |  | \ / |     
| |  | |  | |  | |__| | | |---- | |       | |   | |  | | | |__| | '------.
|_|_/_/  _|_|_ |_|  \_\ |_|____ |_|____   |_|   \_|__|_/ |_|  \_\  ____|_/
                  
                  """
            )
            for director in all_directors:
                print(
                    f"{director.id} | {director.name} | ${director.royalties_per_film:.2f}"
                )

            print(
                "\nSelect your choice: \n0. Exit the program \n1. Director's total royalties \n2. Associated stars \n3. Director's movies \n4. Director's total gross"
            )
            choice4 = input(">")
            if choice4 == "0":
                exit_program()

            elif choice4 == "1":
                print("Find director by ID ")
                director_id = int(input("Enter ID: "))
                director_total_royalties = Director.find_by_id(director_id)
                print(director_total_royalties.total_royalties())
            elif choice4 == "2":
                print("Find director by ID ")
                director_id = int(input("Enter ID: "))
                director_stars = Director.find_by_id(director_id)
                print(director_stars.stars_worked_with())
            elif choice4 == "3":
                print("Find director by ID ")
                director_id = int(input("Enter ID: "))
                director_movies = Director.find_by_id(director_id)
                print(director_movies.movies())
            elif choice4 == "4":
                print("Find director by ID ")
                director_id = int(input("Enter ID: "))
                director_total_gross = Director.find_by_id(director_id)
                print(director_total_gross.total_gross())
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def menu1():
    print(
        """
 ______   ______     ______ _____  _        _________ 
/ |  | \ | |  \ \   | |      | |  | |      | | | | | \

| |  | | | |  | |   | |----  | |  | |   _  | | | | | |
\_|__|_/ |_|  |_|   |_|     _|_|_ |_|__|_| |_| |_| |_|

        """
    )
    print(
        "\nWelcome to the film database, where you can explore \nmovies, their stars and directors and \nexecute CRUD, association, and aggregate operations."
    )
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. See all stars \n2. See all movies \n3. See all directors")


def menu2():

    print(
        "\nSelect your choice: \n0. Exit the program \n1. Add new star \n2. Find star by id \n3. Update star \n4. Delete star \n5. More..."
    )


if __name__ == "__main__":
    main()
