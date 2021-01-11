import urllib.request
from urllib.request import urlopen
import json
import flickrapi
import os
import config


class Flickr_client:

    def get_photo_list(self, search_key, number_photos=100):
        api_key = config.flickr_api_key
        api_secret = config.flickr_api_secret

        # Get new bunch of photos
        flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
        if search_key:
            photos = flickr.photos.search(
                api_key=api_key, text=search_key, per_page=number_photos, sort="relevance")
        else:
            photos = flickr.photos.getRecent(
                api_key=api_key, per_page=number_photos
            )

        # Prepare list
        photo_list = []
        for photo in photos["photos"]["photo"]:
            photo_url = flickr.photos.getSizes(
                api_key=api_key, photo_id=photo["id"])
            photo_url = [pu['source'] for pu in photo_url['sizes']
                         ["size"] if pu["label"] == "Large Square"]
            photo_blob = urlopen(photo_url[0]).read()
            photo["blob"] = photo_blob
            photo_list.append(photo)

        return photo_list
