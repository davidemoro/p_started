#from pyramid.view import view_config

#@view_config(route_name='home', renderer='webapp/app/index.html')
def my_view(request):
    return {'project': 'p_started'}
