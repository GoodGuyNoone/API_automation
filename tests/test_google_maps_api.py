import json

from utils.checking import Checking
from utils.api import GoogleMapsApi


"""Creation, changing and deletion of new location"""
class TestCreatePlace():

    def test_create_new_place(self):
        print("Post Method")
        result_post = GoogleMapsApi.create_new_place()
        place_id = result_post.json().get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_params(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("Get Method -> Post")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_params(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                                'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print("Put method")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_params(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Get Method -> Put")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_params(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                                'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', 'Lenina street 100, RU')

        print("Delete method")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_params(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print("Get Method -> Delete")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_params(result_put, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")



