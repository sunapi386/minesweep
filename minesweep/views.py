# import minesweep.sweep as sweep
from pyramid.view import view_config, view_defaults

@view_defaults(renderer='templates/mytemplate.pt')
class MineSweeperView(object):

    def __init__(self, request):
        print "View.__init__"
        self.request = request
        # Get the grid matching the user cookie.

    @view_config(route_name='home', request_method='GET')
    def home(request):
        print "View.home"
        return {}

    @view_config(route_name='newgame_json', renderer='json')
    def newgame(request):
        # Discard existing game, if any
        print "View.newgame", request
        return {'sweepsize': 5, 'mines': 1}

    @view_config(route_name='play_json', renderer='json')
    def play(request):
        print "View.play", request
        return {'field': 0}