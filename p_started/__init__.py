import os
from pyramid.config import Configurator
from pyramid.settings import asbool


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    import pdb; pdb.set_trace()
    production_config = asbool(settings.get('PRODUCTION', 'false'))
    production = os.environ.get('PRODUCTION', production_config)
    config.include('pyramid_chameleon')

    if production:
        config.add_static_view('static', 'static', cache_max_age=3600)
    else:
        config.add_static_view('static', 'static', cache_max_age=3600)
        config.add_static_view('scripts', 'webapp/app/scripts', cache_max_age=3600)
        config.add_static_view('styles', 'webapp/app/styles', cache_max_age=3600)
        config.add_static_view('images', 'webapp/app/images', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
