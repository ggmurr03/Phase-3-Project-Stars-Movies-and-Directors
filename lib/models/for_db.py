from director import Director
from movie import Movie
from star import Star


Director.drop_table()
Movie.drop_table()
Star.drop_table()

Director.create_table()
Movie.create_table()
Star.create_table()

# create(cls, name, royalties_per_film):

director1 = Director.create("Ridley Scott", 18000000.00)
director2 = Director.create("David Fincher", 17500000.00)
director3 = Director.create("Derrick Borte", 3800000.00)
director4 = Director.create("John Carpenter", 8000000.00)
director5 = Director.create("James Cameron", 48000000.00)


# # create(cls, title, star_id, director_id, box_office, genre)

movie1 = Movie.create("Alien", 1, 1, 78955000.00, "Sci-Fi")
movie2 = Movie.create("Alien 3", 1, 2, 55473000.00, "Sci-Fi")
movie3 = Movie.create("Robin Hood", 2, 1, 105269000.00, "Action")
movie4 = Movie.create("Unhinged", 2, 3, 20800000.00, "Thriller")
movie5 = Movie.create("Halloween", 3, 4, 47000000.00, "Horror")
movie6 = Movie.create("Halloween II", 3, 4, 57000000.00, "Horror")
movie7 = Movie.create("True Lies", 3, 5, 146282000.00, "Action")
movie8 = Movie.create("Avatar", 4, 5, 785000000.00, "Sci-Fi")
movie9 = Movie.create("Escape from New York", 5, 4, 26000000.00, "Action")
movie10 = Movie.create("Escape from LA", 5, 4, 25477000.00, "Action")

# # create(cls, name, rate_per_movie)

star1 = Star.create("Sigourney Weaver", 12000000.00)
star2 = Star.create("Russel Crowe", 15000000.00)
star3 = Star.create("Jaime Lee Curtis", 6500000.00)
star4 = Star.create("Sam Worthington", 4322000.00)
star5 = Star.create("Kurt Russell", 8050000.00)
