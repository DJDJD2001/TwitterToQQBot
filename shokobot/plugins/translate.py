# Define functions for translate

import hashlib
import random
import requests

from shokobot.plugins.settings import translate_api_url_http as api_url_http
from shokobot.plugins.settings import translate_app_id as app_id
from shokobot.plugins.settings import translate_password as password

def translate(_text : str, _from = 'jp', _to = 'zh'):
    # Parameter:
    #   _text: Text needs to translate
    #   _from: From which language, default to Japanese
    #   _to: To which language, default to Chinese(simplified)
    # Return:
    #   str: Translated text
    
    _salt = str(random.randint(32768, 65536))

    _pre_sign = \
        app_id + \
        _text + \
        _salt + \
        password

    _sign = hashlib.md5(_pre_sign.encode()).hexdigest()

    _params = {
        'q': _text,
        'from': _from,
        'to': _to,
        'appid': app_id,
        'salt': _salt,
        'sign': _sign
    }
    
    try:
        _response = requests.get(api_url_http, params=_params)

        _result_dict = _response.json()

        if 'trans_result' in _result_dict:
            return _result_dict['trans_result'][0]['dst']
        else:
            print('Some errors occured when translating:\n', _result_dict)
    except Exception as e:
        print('Some errors occured when translating: ', e)