# import minesweep.sweep as sweep
from pyramid.view import view_config, view_defaults
import uuid
import minesweep.sweep as swp

@view_defaults(renderer='templates/mytemplate.pt')
class MineSweeperView(object):
    # Hashmap containing user related data, such as
    # minefield map, name, high score, etc
    users = {}

    def __init__(self, request):
        print "View.__init__"
        self.request = request

        # Get the grid matching the user cookie.
        if 'player_id' not in self.request.session:
            SIZE = 10
            MINES = 9
            board = swp.create_board(SIZE, MINES)
            print(board)

            uid = str(uuid.uuid4())
            self.request.session['player_id'] = uid
            MineSweeperView.users[uid] = board.to_list()
            print "New player_id:", self.request.session
            print "Minefield    :", MineSweeperView.users[uid]
        else:
            uid = self.request.session['player_id']
            print "Old player_id exists:", self.request.session['player_id']
            print "Minefield    :", MineSweeperView.users[uid]


    @view_config(route_name='home', request_method='GET')
    def home(self):
        print "View.home", self
        return {}

    @view_config(route_name='newgame_json', renderer='json')
    def newgame(self):
        # Discard existing game, if any
        print "View.newgame", self
        uid = self.request.session['player_id']
        new_minefield = MineSweeperView.users[uid]
        return {'new_minefield':new_minefield}

    @view_config(route_name='play_json', renderer='json')
    def play(self):
        print "View.play", self
        updated_minefield = []
        return {'updated_minefield':updated_minefield}
