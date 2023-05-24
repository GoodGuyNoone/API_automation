
"""Method for verifying responses"""
class Checking():

    """Status code checking method"""
    @staticmethod
    def check_status_code(response, status_code):
        assert response.status_code == status_code, f"Get status code different from expected. " \
                                                    f"Got {response.status_code} instead {status_code}"
        print(f"Got expected status code: {status_code}")
