import json


class Checking():

    """Status code checking method"""
    @staticmethod
    def check_status_code(response, status_code):
        assert response.status_code == status_code, f"Get status code different from expected. " \
                                                    f"Got {response.status_code} instead {status_code}"
        print(f"Got expected status code: {status_code}")

    """Verify required fields"""
    @staticmethod
    def check_json_params(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All fields presented")

    """Method for verifying parameters values"""
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        print(f"{check_info} = {expected_value}")
        assert check_info == expected_value
        print(f"{field_name} is correct")
