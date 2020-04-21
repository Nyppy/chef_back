import requests


class SmsManager:

    EMAIL = 'merkuriy.kursk@gmail.com'
    KEY = 'qhyLl3ijUBAM4yZiPGDwmFxPmxkD'
    URL = 'https://{}:{}@gate.smsaero.ru/v2/sms/send'.format(EMAIL, KEY)

    def __init__(self, phone="79017916089"):
        self.phone = phone

    def send(self, address, apartment, price, phone, food, index):
        # data = {
        #     'number': self.phone,
        #     'text': "CHIEF STREET\r\n{}\r\n{}\r\n{}\r\n{}\r\n{} руб.\r\n\r\nID заказа - {}".format(
        #         address, apartment, phone, food, price, index
        #     ),
        #     'sign': "SMS Aero",
        #     'channel': 'DIRECT'
        # }
        #
        # requests.post(self.URL, json=data)
        return ''


class Firebase:
    data = {
        "push_firebase": {
            'key': "",
            'url': 'https://fcm.googleapis.com/fcm/send'
        }
    }

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'key={}'.format(data['push_firebase']['key'])
    }

    def push(self, to_id, address, apartment, phone, food, price, index):
        data = {
            "data": {
              "requestCode": "200",
            },
            "notification": {
                'title': 'CHIEF STREET',
                'subtitle': 'Новая заявка',
                'body': "CHIEF STREET\r\n{}\r\n{}\r\n{}\r\n{}\r\n{} руб.\r\n\r\nID заказа - {}".format(
                address, apartment, phone, food, price, index
            ),
                'sound': None,
                'badge': None,

            },
            'dry_run': False,

            'priority': 'high',
            'content_available': True,
            "to": to_id
        }

        answer = requests.post(self.data["push_firebase"]["url"], json=data, headers=self.headers)
