from mind_core.test import APITestCase, APIClient
from mind_core import status
from mind_jwt.settings import api_settings


class APIJWTClient(APIClient):
    def login(self, **credentials):
        """
        Returns True if login is possible; False if the provided credentials
        are incorrect, or the user is inactive.
        """

        response = self.post('/api-token-auth/', credentials, format='json')
        if response.status_code == status.HTTP_200_OK:
            self.credentials(
                HTTP_AUTHORIZATION="{0} {1}".format(api_settings.JWT_AUTH_HEADER_PREFIX, response.data['token']))

            return True
        else:
            return False


class APIJWTTestCase(APITestCase):
    client_class = APIJWTClient
