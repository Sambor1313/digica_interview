import config


def download_photos():
    """
    This function get from console 2 parameters:
    - key-word
    - number of photos

    return:
    tuple of key word and number of photos
    """
    key_word = ""
    no_photos = 0

    key_word = input("Search key-words: ")

    while True:
        no_photos = 0
        try:
            no_photos = int(input("Number of photos: "))
            no_photos = no_photos if no_photos != "" else config.default_photo_to_get
            if no_photos < 0:
                raise ValueError()
        except (ValueError):
            print("Number of photos must be positive or empty")
        else:
            break

    return (key_word, no_photos)


def exit_or_no():
    cmd = input("Do you want to add next photos? [Y/n] ")
    if cmd == "Y":
        return True
    return False
