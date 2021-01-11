import sqlite3
from PIL import Image
import io
import math


class DB_client():

    def add_photos(self, new_photos):
        with sqlite3.connect("db.sqlite3") as conn:
            command = "INSERT OR REPLACE INTO Photos VALUES(? ,?, ?)"
            for photo in new_photos:
                conn.execute(command, (photo.get("id"),
                                       photo.get("title"),
                                       photo.get("blob")
                                       ))
            conn.commit()

    def get_photo(self, photo_id):
        with sqlite3.connect("db.sqlite3") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM Photos WHERE id=?", (photo_id,))
            photo = c.fetchone()
            stream = io.BytesIO(photo[2])
            img = Image.open(stream)
            img.show()
            return img

    def get_the_reddest(self, verbose=False):
        picture = None
        with sqlite3.connect("db.sqlite3") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM Photos")
            photos = c.fetchall()
            max_reddish = - 150 * 150
            for photo in photos:
                img = Image.open(io.BytesIO(photo[2]))
                img_hsv = img.convert('HSV')
                pix = img_hsv.getdata()
                redish = sum([
                    math.cos(math.radians(p[0]))
                    * p[1]/100
                    for p in pix])
                if redish > max_reddish:
                    max_reddish = redish
                    picture = photo

        if verbose:
            print("The reddest picture is",
                  picture[1], "[id: ", picture[0], "]")
            self.get_photo(picture[0])
        return picture


if __name__ == "__main__":
    db = DB_client()
    db.get_the_reddest(True)
