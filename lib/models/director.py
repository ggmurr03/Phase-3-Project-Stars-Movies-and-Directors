import sqlite3
from movie import Movie
from star import Star


CONN = sqlite3.connect("filmdatabase.db")
CURSOR = CONN.cursor()


class Director:

    def __init__(self, name, royalties_per_film, id=None):
        self.id = id
        self.name = name
        self.royalties_per_film = royalties_per_film

    @property
    def royalties_per_film(self):
        return self._royalties_per_film

    @royalties_per_film.setter
    def royalties_per_film(self, value):
        if isinstance(value, float):
            self._royalties_per_film = value
        else:
            raise ValueError("Royalties must be floating point number.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS directors
            (id INTEGER PRIMARY KEY,
            name TEXT,
            royalties_per_film FLOAT
            );

        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS directors;

        """
        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        director = cls(id=row[0], name=row[1], royalties_per_film=row[2])
        return director

    @classmethod
    def get_all_directors(cls):
        sql = "SELECT * FROM directors;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    def save(self):
        sql = """
            INSERT INTO directors (name, royalties_per_film)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.royalties_per_film))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, royalties_per_film):
        director = cls(name, royalties_per_film)
        director.save()
        return director

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM directors
            WHERE id = ?
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    def total_royalties(self):

        directed_movies = [
            movie for movie in Movie.get_all_movies() if movie.director_id == self.id
        ]
        return f"${self.royalties_per_film * len(directed_movies):.2f}"

    def stars_worked_with(self):
        directed_movies = [movie for movie in Movie.all if movie.director_id == self.id]
        star_ids = set([movie.star_id for movie in directed_movies])
        return [Star.find_by_id(star_id).name for star_id in star_ids]

    def movies(self):
        return set([movie.title for movie in Movie.all if movie.director_id == self.id])

    def total_gross(self):
        return f"${sum([float(movie.box_office) for movie in Movie.get_all_movies() if movie.director_id == self.id]):.2f}"
