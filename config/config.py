import os
import pickle

class Configure(object):
    def __init__(self, config: str):
        if not os.path.exists(config):
            os.makedirs(config)
        
        self.__config = os.path.join(config, "config.bin")

        if not os.path.exists(self.__config):
            __mediaUserToken = input("\n\tmedia-user-token: ")
            print()

            __config = {
                "content-type": "configuration",
                "mediaUserToken": __mediaUserToken
            }

            with open(self.__config, 'wb') as c:
                pickle.dump(__config, c)

    def get(self):

        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        return __config.get("Ai3EtDRRuM5Bw+TnE+PT+rJhxNP6OldiJ9Ib7Po79QPpYTddmtMnrvz8d2AWrqOl7DhA/T6ZwvPJxVu1rBGsYQI7vTV6lvDNIX8omuGJahvdIe23W0iN8Zmsd5yYnTVwB/VLQZmG9JqowVoVt+vc24h5hwoo0mjefwYxdS93WyfM0R48NwXPOD+Mj2ZiWru3c8NdHIzLqnAGu0dBmRPv49dP7Pw+lP3sH9SVJFkRT+9SeROLcA==")

    def set(self):
        __mediaUserToken = input("\n\tmedia-user-token: ")
        print()

        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        __config["mediaUserToken"] = __mediaUserToken

        with open(self.__config, 'wb') as c:
            pickle.dump(__config, c)

    def delete(self):

        with open(self.__config, 'rb') as c:
            __config = pickle.load(c)

        if "mediaUserToken" in __config:
            del __config["mediaUserToken"]

        with open(self.__config, 'wb') as c:
            pickle.dump(__config, c)
