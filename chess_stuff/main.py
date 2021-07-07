from stockfish import Stockfish

stockfish = Stockfish("stockfish_14_linux_x64_avx2/stockfish_14_x64_avx2")

"""""(pawn = "P", knight = "N", bishop = "B", rook = "R", queen = "Q" and king = "K")"""


stockfish.set_fen_position("1r1r2k1/5ppp/2B5/p2bP3/5P1P/4n3/1PPR2P1/2KR4 w - - 0 1")

print(stockfish.get_top_moves(5))