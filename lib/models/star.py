import sqlite3

from movie import Movie


CONN = sqlite3.connect("filmdatabase.db")
CURSOR = CONN.cursor()


class Star:

    def __init__(self, name, rate_per_movie, id=None):
        self.id = id
        self.name = name
        self.rate_per_movie = rate_per_movie

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            raise ValueError("Name must be a string, between 1 and 25 characters.")

    @property
    def rate_per_movie(self):
        return self._rate_per_movie

    @rate_per_movie.setter
    def rate_per_movie(self, value):
        if isinstance(value, float):
            self._rate_per_movie = value
        else:
            raise ValueError("Rate must be a floating point value.")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS stars
            (id INTEGER PRIMARY KEY,
            name TEXT,
            rate_per_movie FLOAT
            );

        """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS stars;

        """
        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        star = cls(id=row[0], name=row[1], rate_per_movie=row[2])
        return star

    @classmethod
    def get_all_stars(cls):
        sql = "SELECT * FROM stars;"
        return [cls.instance_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    @classmethod
    def create(cls, name, rate_per_movie):
        star = cls(name, rate_per_movie)
        star.save()
        return star

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM stars
            WHERE name = ?
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM stars
            WHERE id = ?
            LIMIT 1;
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return cls.instance_from_db(row)

    def save(self):
        sql = """
            INSERT INTO stars (name, rate_per_movie)
            VALUES (?, ?);
        """
        CURSOR.execute(sql, (self.name, self.rate_per_movie))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def update(self):
        sql = """
            UPDATE stars SET name = ?, rate_per_movie = ? WHERE id = ?;
        """
        CURSOR.execute(sql, (self.name, self.rate_per_movie, self.id))
        CONN.commit()
        return self

    def delete(self):
        sql = """
            DELETE FROM stars WHERE id = ?;
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    def average_gross(self):
        count = len([movie for movie in Movie.all if movie.star_id == self.id])
        total = sum(
            [movie.box_office for movie in Movie.all if movie.star_id == self.id]
        )
        return f"{total/count:.2f}"

    def movies(self):
        return set([movie.title for movie in Movie.all if movie.star_id == self.id])

    def top_grossing_movie(self):
        star_movies = [movie for movie in Movie.all if movie.star_id == self.id]

        if not star_movies:
            return None

        top_movie = max(star_movies, key=lambda movie: movie.box_office)

        return top_movie.title
