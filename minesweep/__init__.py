from pyramid.session import SignedCookieSessionFactory
from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    my_session_factory = SignedCookieSessionFactory('mysecret')
    config = Configurator(settings=settings)
    config.set_session_factory(my_session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('newgame_json', '/api/newgame.json')
    config.add_route('play_json', '/api/play.json')
    config.add_route('flag_json', '/api/flag.json')
    config.scan()
    return config.make_wsgi_app()
