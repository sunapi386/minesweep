# import minesweep.sweep as sweep
from pyramid.view import view_config, view_defaults
import uuid

@view_defaults(renderer='templates/mytemplate.pt')
class MineSweeperView(object):

    mapping = {}

    def __init__(self, request):
        print "View.__init__"
        self.request = request

        # Get the grid matching the user cookie.
        session = request.session
        if 'player_id' not in session:
            uid = str(uuid.uuid4())
            session['player_id'] = uid
            MineSweeperView.mapping[uid] = "Some new minefield"
            print "New player_id:", session
            print "Minefield    :", MineSweeperView.mapping[uid]
        else:
            uid = session['player_id']
            print "Old player_id exists:", session['player_id']
            print "Minefield    :", MineSweeperView.mapping[uid]



    @view_config(route_name='home', request_method='GET')
    def home(request):
        print "View.home", request
        return {}

    @view_config(route_name='newgame_json', renderer='json')
    def newgame(request):
        # Discard existing game, if any
        print "View.newgame", request
        new_minefield = []
        return {'new_minefield':new_minefield}

    @view_config(route_name='play_json', renderer='json')
    def play(request):
        print "View.play", request
        updated_minefield = []
        return {'updated_minefield':updated_minefield}