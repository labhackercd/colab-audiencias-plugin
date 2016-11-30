from django.contrib.sites.models import Site
from colab.plugins import helpers
import requests


def login_user(sender, user, request, **kwargs):
    prefix = helpers.get_plugin_prefix('colab_audiencias', regex=False)
    base_url = Site.objects.get_current().domain
    base_url = "{}/{}".format(base_url, prefix)
    remote_user_data = '{"email": "%s", "name": "%s" }' % (user.email,
                                                           user.username)
    headers = {'Auth-user': user.username,
               'Remote-User-Data': remote_user_data}

    response = requests.get(base_url, headers=headers)
    session = response.cookies.get('audiencias_session')
    request.COOKIES.set("audiencias_session", session)


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('audiencias_session')
