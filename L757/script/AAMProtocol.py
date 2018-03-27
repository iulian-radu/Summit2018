import requests
import json
import base64


class AAMProtocol:
    def __init__(self, base_url):
        self.base_url = base_url

    @staticmethod
    def safe_print(content):
        print "{0}\n".format(content),

    @staticmethod
    def success(response):
        if response.status_code in [200, 201, 202, 204]:
            return True
        return False

    @staticmethod
    def log_response_if_needed(response):
        if not AAMProtocol.success(response) and response.status_code not in [404]:
            AAMProtocol.safe_print('Error encountered. The server response was: ' % (response.json()))

    def post(self, token, url_fragment, payload):
        url = self.base_url + url_fragment
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        self.safe_print('')
        self.safe_print('AAM API call - POST %s Payload:%s Headers:%s' %
                        (url, str(payload), headers))
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        self.safe_print('AAM Response: %s' % response.status_code)
        AAMProtocol.log_response_if_needed(response)
        return response

    def put(self, token, url_fragment, payload):
        url = self.base_url + url_fragment
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        self.safe_print('')
        self.safe_print('AAM API call - PUT %s Payload:%s Headers:%s' %
                        (url, str(payload), headers))
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        self.safe_print('AAM Response: %s' % response.status_code)
        AAMProtocol.log_response_if_needed(response)
        return response

    def get(self, token, url_fragment):
        url = self.base_url + url_fragment
        self.safe_print('')
        self.safe_print('AAM API call - GET %s' % url)
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)
        self.safe_print('AAM Response: %s' % response.status_code)
        AAMProtocol.log_response_if_needed(response)
        return response

    def delete(self, token, url_fragment):
        url = self.base_url + url_fragment
        self.safe_print('')
        self.safe_print('AAM API call - DELETE %s' % url)
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        response = requests.delete(url, headers=headers)
        self.safe_print('AAM Response: %s' % response.status_code)
        AAMProtocol.log_response_if_needed(response)
        return response

    def get_token(self, client_id, client_secret, user_name, user_password):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(client_id + ':' + client_secret),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(
            self.base_url + '/oauth/token', headers=headers, data='grant_type=password&username=' + user_name +
                                                                  '&password=' + user_password)
        if self.success(response):
            return response.json()['access_token']
        else:
            return None
