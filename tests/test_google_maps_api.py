from utils.checking import Checking
from utils.api import GoogleMapsApi


"""Creation, changing and deletion of new location"""
class TestCreatePlace():

    def test_create_new_place(self):
        print("Post Method")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json().get("place_id")
        Checking.check_status_code(result_post, 200)

        print("Get Method -> Post")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Put method")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Get Method -> Put")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Delete method")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Get Method -> Delete")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
