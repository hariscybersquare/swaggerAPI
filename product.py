import connexion
from connexion.exceptions import OAuthProblem
from flask_injector import inject
from providers.CouchProvider import CouchProvider

TOKEN_DB = {
    'asdf1234567890': {
        'uid': 100
    }
}

def apikey_auth(token, required_scopes):
    info = TOKEN_DB.get(token, None)

    if not info:
        raise OAuthProblem('Invalid token')

    return info

@inject
def read_product( _id, data_provider=CouchProvider)  -> str:
    return data_provider.read_product(_id)
