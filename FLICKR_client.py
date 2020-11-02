import urllib.request
import json
import flickrapi


class Flickr_client:

    def get_photo_list(self, search_key, number_photos=100):
        api_key = u"70d3f51fc4482fcfa7ada4079416c8cf"
        api_secret = u"596b55163695a009"

        flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
        photos = flickr.photos.search(
            api_key=api_key, text=search_key, per_page=number_photos)

        photo_list = []
        for photo in photos["photos"]["photo"]:
            photo_list.append(photo)

        return photo_list
