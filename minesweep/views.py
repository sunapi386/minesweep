# import minesweep.sweep as sweep
from pyramid.view import view_config, view_defaults
import uuid
import minesweep.sweep as swp

@view_defaults(renderer='templates/mytemplate.pt')
class MineSweeperView(object):
    # Hashmap containing user related data, such as
    # minefield map (and perhaps in the future: name, high score, etc.)
    users = {}

    def __init__(self, request):
        print "View.__init__"
        self.request = request

        # Get the grid matching the user cookie.
        if 'player_id' not in self.request.session:
            # size, and mines can be read dynamically
            size = 10
            mines = 10
            board = swp.create_board(size, mines)
            print(board)
            uid = str(uuid.uuid4())
            self.request.session['player_id'] = uid
            MineSweeperView.users[uid] = board
            print "New player_id:", self.request.session
            print "Minefield    :", MineSweeperView.users[uid]

        elif self.request.session['player_id'] not in MineSweeperView.users:
            print "Old player_id exists but not match what's in memory:", \
                self.request.session['player_id']
            uid = self.request.session['player_id']
            size = 10
            mines = 10
            board = swp.create_board(size, mines)
            print(board)
            MineSweeperView.users[uid] = board
            print "Setting new player_id:", self.request.session
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
        size = 10
        mines = 10
        MineSweeperView.users[uid] = swp.create_board(size, mines)
        board = MineSweeperView.users[uid]
        return {'new_minefield':board.to_list()}

    @view_config(route_name='play_json', renderer='json')
    def play(self):
        print "View.play", self

        row = self.request.json.get("row")
        col = self.request.json.get("col")
        flag = "flag" in self.request.json
        print "User requests %s %s %s" % (row, col, flag)

        uid = self.request.session['player_id']
        print "User", uid
        board = MineSweeperView.users[uid]
        print "Loaded %s board %s" % (uid, board)

        move = col + row + ("f" if flag else "")
        swp.make_move(board, move)
        return {'played_minefield':board.to_list(),
                'row':row,
                'col':col}

    @view_config(route_name='flag_json', renderer='json')
    def flag(self):
        print "View.flag", self
        row = self.request.json.get("row")
        col = self.request.json.get("col")
        return {'updated_minefield':[],
                'row':row,
                'col':col}
