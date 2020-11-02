import FLICKR_client


search_text = input("Search key-words:")
number = input("Number of photos:")

fl = FLICKR_client.Flickr_client()
print(fl.get_photo_list(search_text, number))
