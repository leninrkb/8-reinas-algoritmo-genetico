import chess
import chess.svg


def dibujarTablero(tablero, n):
    tableroAjedrez = chess.Board()
    tableroAjedrez.clear()
    for i in range(n):
        for j in range(n):
            if tablero[i][j]:
                tableroAjedrez.set_piece_at(chess.square(i, j), chess.Piece(5, chess.WHITE))
    return tableroAjedrez.fen()

def guardarTablero(dibujo, nombre):
    tablero = chess.Board(dibujo)
    tablerosvg = chess.svg.board(board=tablero)
    archivo = open(nombre, "w")
    archivo.write(tablerosvg)
    archivo.close()
    print("guardado...")
    
def guardar(tablero, nombre,  n):
    dibujo = dibujarTablero(tablero, n)
    guardarTablero(dibujo, nombre)