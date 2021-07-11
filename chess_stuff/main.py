# from stockfish import Stockfish
#
# stockfish = Stockfish("stockfish_14_linux_x64_avx2/stockfish_14_x64_avx2")
#
# """""(pawn = "P", knight = "N", bishop = "B", rook = "R", queen = "Q" and king = "K")"""
#
#
# stockfish.set_fen_position("1r1r2k1/5ppp/2B5/p2bP3/5P1P/4n3/1PPR2P1/2KR4 w - - 0 1")
#
# print(stockfish.get_top_moves(5))



class PieceElement:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name, self.color


class Fen:
    list_of_elements = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
                        'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
                        'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
                        'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
                        'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
                        'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
                        'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
                        'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']

    def __init__(self, **params):
        self.fend = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        for name, value in params.items():
            if name == 'fend':
                self.fend = value
        self.start_position = {}
        self.list_positions = []
        self.positions = self.fend[:-13]
        self.wP = PieceElement('P', 'w')
        self.bp = PieceElement('p', 'b')
        self.wK = PieceElement('K', 'w')
        self.bk = PieceElement('k', 'b')
        self.wQ = PieceElement('Q', 'w')
        self.bq = PieceElement('q', 'b')
        self.wR = PieceElement('R', 'w')
        self.br = PieceElement('r', 'b')
        self.wN = PieceElement('N', 'w')
        self.bn = PieceElement('n', 'b')
        self.wB = PieceElement('B', 'w')
        self.bb = PieceElement('b', 'b')

    def _list_fen_values(self):
        for value in self.positions:
            if value.isnumeric():
                for _ in range(int(value)):
                    self.list_positions.append(None)
            if value == 'P':
                self.list_positions.append(self.wP.name)
            if value == 'p':
                self.list_positions.append(self.bp.name)
            if value == 'K':
                self.list_positions.append(self.wK.name)
            if value == 'k':
                self.list_positions.append(self.bk.name)
            if value == 'Q':
                self.list_positions.append(self.wQ.name)
            if value == 'q':
                self.list_positions.append(self.bq.name)
            if value == 'R':
                self.list_positions.append(self.wR.name)
            if value == 'r':
                self.list_positions.append(self.br.name)
            if value == 'N':
                self.list_positions.append(self.wN.name)
            if value == 'n':
                self.list_positions.append(self.bn.name)
            if value == 'B':
                self.list_positions.append(self.wB.name)
            if value == 'b':
                self.list_positions.append(self.bb.name)
        return self.list_positions

    def start_position_list(self):
        self._list_fen_values()
        for key, value in zip(self.list_of_elements, self.list_positions):
            self.start_position[key] = value
        return self.start_position


class Moves:
    def __init__(self):
        self.curr_position = (Fen().start_position_list()).copy()

    def current_position(self):
        return self.curr_position

    def change_position(self, position):
        start_pos = position[0:2].lower()
        stop_pos = position[2:4].lower()

        for key, value in self.curr_position.items():
            if key == start_pos:
                moved_obj = value
        self.curr_position[start_pos] = None
        self.curr_position[stop_pos] = moved_obj
        return self.curr_position

    def curr_fen(self):
        self.positions2 = ""
        self.pos_temp = 0
        self.prev_value = 0
        for ix, value in enumerate(self.curr_position.values()):
            if ix % 8 == 0:
                self.positions2 += "/"
                if self.pos_temp > 0:
                    self.positions2 += str(self.pos_temp)
                    self.pos_temp = 0
            if not value:
                self.pos_temp += 1
            else:
                self.positions2 += value
                if self.pos_temp > 0:
                    self.positions2 += str(self.pos_temp)
                    self.pos_temp = 0
            self.prev_value = value

        return self.positions2








ruchy = Moves()
# print(ruchy.curr_position)
# ruchy.change_position('d2d4')
# print(ruchy.curr_position)
print(ruchy.curr_fen())









# fen = "1nb1kbnr/pp1pp1pp/8/r1pq4/4PP2/1P6/1P1P1PPP/RNBQKBNR w KQk - 0 1"
# my_newfen = Fen()
#
# print(my_newfen.start_position_list())