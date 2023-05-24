from requests import Response

from utils.api import GoogleMapsApi

"""Creation, changing and deletion of new location"""
class TestCreatePlace():

    def test_create_new_place(self):
        print("Post Method")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json().get("place_id")

        print("Get Method -> Post")
        result_get = GoogleMapsApi.get_new_place(place_id)

        print("Put method")
        result_put = GoogleMapsApi.put_new_place(place_id)

        print("Get Method -> Put")
        result_get = GoogleMapsApi.get_new_place(place_id)
