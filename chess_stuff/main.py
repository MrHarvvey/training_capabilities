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

    fed = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    list_of_elements = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8',
                        'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7',
                        'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6',
                        'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5',
                        'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4',
                        'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3',
                        'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2',
                        'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1']

    def __init__(self, **params):
        for name, value in params.items():
            if name == 'fend':
                self.fend = value
            else:
                self.fend = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        self.start_position = []
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
            self.start_position.append({key: value})
        return self.start_position


class Moves:
    def __init__(self):
        self.positions =

    # def change_position(self, position):
    #     self.start_position_list()
    #     start_pos = position[0:2].lower()
    #     stop_pos = position[2:4].lower()
    #     for item in self.start_position:
    #         if item.key == start_pos:


class Move():

    def __init__(self):
        self.current_position = Fen().start_position()

mariola = Move()
print(mariola.current_position)




fen = "1nb1kbnr/pp1pp1pp/8/r1pq4/4PP2/1P6/1P1P1PPP/RNBQKBNR w KQk - 0 1"
my_newfen = Fen(fen)

print(my_newfen.start_position_list())