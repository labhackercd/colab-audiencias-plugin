from colab.plugins import helpers
import requests
import json


def login_user(sender, user, request, **kwargs):
    config = helpers.get_plugin_config('colab_audiencias')
    user_data = {
        'email': user.email,
        'name': user.get_full_name(),
        'avatar': user.profile.avatar.url
    }
    remote_user_data = json.dumps(user_data)
    headers = {'Auth-user': user.username,
               'Remote-User-Data': remote_user_data}

    response = requests.get(config['upstream'], headers=headers)
    session = response.cookies.get('audiencias_session')
    request.COOKIES.set("audiencias_session", session)


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('audiencias_session')
