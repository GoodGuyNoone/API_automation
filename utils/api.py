import json
from utils.http_methods import HttpMethods


"""Methods for testing google maps api"""

base_url = "https://rahulshettyacademy.com"
key = "qaclick123"


class GoogleMapsApi():
    """Method for creating new place"""
    @staticmethod
    def create_new_place():
        json_create_new_place = {
                "location": {
                    "lat": -38.383494,
                    "lng": 33.427362
                },
                "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
                "types": ["shoe park", "shop"],
                "website": "http://google.com",
                "language": "French-IN"
            }

        post_resource = "/maps/api/place/add/json"
        post_url = f"{base_url}{post_resource}?key={key}"
        print(post_url)
        result_post = HttpMethods.post(post_url, json_create_new_place)
        print(result_post.json())
        return result_post

    """Method for verifying created place"""
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"
        get_url = f"{base_url}{get_resource}?key={key}&place_id={place_id}"
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.json())
        return result_get

    """Method for changing created place"""
    @staticmethod
    def put_new_place(place_id):
        get_resource = "/maps/api/place/update/json"
        put_url = f"{base_url}{get_resource}?key={key}"
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,
            "address":"Lenina street 100, RU",
            "key": key
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.json())
        return result_put

    """Method for deleting created place"""
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"
        delete_url = f"{base_url}{delete_resource}?key={key}"
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id,
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.json())
        return result_delete

