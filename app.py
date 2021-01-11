import FLICKR_client
import config
import console_menu
from db_client import DB_client


def main():
    # init
    fl = FLICKR_client.Flickr_client()
    db_cl = DB_client()

    # Program loop
    while True:
        order_photos = console_menu.download_photos()

        # Call API
        photos = fl.get_photo_list(*order_photos)

        # Add to db
        db_cl.add_photos(photos)

        # Get most red picture
        db_cl.get_the_reddest(verbose=True)

        # Add more picture?
        if not console_menu.exit_or_no():
            break


if __name__ == "__main__":
    main()
