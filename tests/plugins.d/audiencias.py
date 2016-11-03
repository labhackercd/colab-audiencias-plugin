
from django.utils.translation import ugettext_lazy as _
from colab.plugins.utils.menu import colab_url_factory

name = 'colab_audiencias_plugin'
verbose_name = 'Colab Audiencias Plugin Plugin'

upstream = 'localhost'
# middlewares = []

urls = {
    'include': 'colab_audiencias_plugin.urls',
    'prefix': '^colab_audiencias_plugin/',
}

menu_title = _('colab_audiencias_plugin')

url = colab_url_factory('colab_audiencias_plugin')

# Extra data to be exposed to plugin app config
extra = {}

menu_urls = (
# Example of menu URL:
#    url(display=_('Public Projects'), viewname='colab_audiencias_plugin',
#        kwargs={'path': 'public/projects'}, auth=False),

# Example of authenticated user menu URL:
#    url(display=_('Profile'), viewname='colab_audiencias_plugin',
#        kwargs={'path': 'profile'}, auth=True),
)
