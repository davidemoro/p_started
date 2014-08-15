import os
from pyramid.config import Configurator
from pyramid.settings import asbool


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    # TODO: change PRODUCTION with something of more specific
    production_config = asbool(settings.get('PRODUCTION', 'false'))
    production = os.environ.get('PRODUCTION', production_config)
    config.include('pyramid_chameleon')

    if production:
        config.add_static_view('static', 'static', cache_max_age=3600)
    else:
        config.add_static_view('scripts', 'p_started:webapp/app/scripts', cache_max_age=3600)
        config.add_static_view('styles', 'p_started:webapp/app/styles', cache_max_age=3600)
        config.add_static_view('images', 'p_started:webapp/app/images', cache_max_age=3601)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
