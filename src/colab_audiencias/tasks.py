from colab_audiencias.views import ColabAudienciasPluginProxyView


def login_user(sender, user, request, **kwargs):
    proxy_view = ColabAudienciasPluginProxyView()
    response = proxy_view.dispatch(request, '')
    session = response.cookies.get('audiencias_session')
    request.COOKIES.set('audiencias_session', session.value)


def logout_user(sender, user, request, **kwargs):
    request.COOKIES.delete('audiencias_session')
