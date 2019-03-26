import pygame
import os

b_bishop = pygame.image.load(os.path.join("img", "black_bishop.png"))
b_king = pygame.image.load(os.path.join("img", "black_king.png"))
b_knight = pygame.image.load(os.path.join("img", "black_knight.png"))
b_pawn = pygame.image.load(os.path.join("img", "black_pawn.png"))
b_queen = pygame.image.load(os.path.join("img", "black_queen.png"))
b_rook = pygame.image.load(os.path.join("img", "black_rook.png"))

w_bishop = pygame.image.load(os.path.join("img", "white_bishop.png"))
w_king = pygame.image.load(os.path.join("img", "white_king.png"))
w_knight = pygame.image.load(os.path.join("img", "white_knight.png"))
w_pawn = pygame.image.load(os.path.join("img", "white_pawn.png"))
w_queen = pygame.image.load(os.path.join("img", "white_queen.png"))
w_rook = pygame.image.load(os.path.join("img", "white_rook.png"))

b = [b_bishop, b_king, b_knight, b_pawn, b_queen, b_rook]
w = [w_bishop, w_king, w_knight, w_pawn, w_queen, w_rook]

B = []
W = []

for img in b:
    B.append(pygame.transform.scale(img, (55, 55)))

for img in w:
    W.append(pygame.transform.scale(img, (55, 55)))


class Piece:
    img = -1
    rect = (113, 113, 525, 525)
    startX = rect[0]
    startY = rect[1]

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.selected = False

    def valid_moves(self, board) -> list:
        pass

    def click(self):
        pass

    def isSelected(self):
        return self.selected

    def draw(self, win, board):
        if self.color == "w":
            drawThis = W[self.img]
        else:
            drawThis = B[self.img]

        if self.selected:
            moves = self.valid_moves(board)
            for move in moves:
                x = 33 + round(self.startX + (move[0] * self.rect[2] / 8))
                y = 33 + round(self.startY + (move[1] * self.rect[2] / 8))
                pygame.draw.circle(win, (255, 0, 0), (x, y), 10)

        x = 5 + round(self.startX + (self.col * self.rect[2] / 8))
        y = 5 + round(self.startY + (self.row * self.rect[2] / 8))

        if self.selected:
            pygame.draw.rect(win, (255, 0, 0), (x, y, 55, 55), 2)

        win.blit(drawThis, (x, y))


class Bishop(Piece):
    img = 0

    def valid_moves(self, board):
        return []


class King(Piece):
    img = 1

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        if i > 0:
            # top left
            if j > 0:
                p = board[i - 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i - 1))
                elif p.color != self.color:
                    moves.append((j - 1, i - 1))

            # top middle
            p = board[i - 1][j]
            if p == 0:
                moves.append((j, i - 1))
            elif p.color != self.color:
                moves.append((j, i - 1))

            # top right
            if j < 7:
                p = board[i - 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i - 1))
                elif p.color != self.color:
                    moves.append((j + 1, i - 1))

        if i < 7:
            # bottom left
            if j > 0:
                p = board[i + 1][j - 1]
                if p == 0:
                    moves.append((j - 1, i + 1))
                elif p.color != self.color:
                    moves.append((j - 1, i + 1))

            # bottom middle
            p = board[i + 1][j]
            if p == 0:
                moves.append((j, i + 1))
            elif p.color != self.color:
                moves.append((j, i + 1))

            # bottom right
            if j < 7:
                p = board[i + 1][j + 1]
                if p == 0:
                    moves.append((j + 1, i + 1))
                elif p.color != self.color:
                    moves.append((j + 1, i + 1))

        # middle left
        if j > 0:
            p = board[i][j - 1]
            if p == 0:
                moves.append((j - 1, i))
            elif p.color != self.color:
                moves.append((j - 1, i))

        # middle right
        if j < 7:
            p = board[i][j + 1]
            if p == 0:
                moves.append((j + 1, i))
            elif p.color != self.color:
                moves.append((j + 1, i))
        return moves


class Knight(Piece):
    img = 2

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []

        # down left
        if i < 6 and j > 0:
            p = board[i + 2][j - 1]
            if p == 0:
                moves.append((j - 1, i + 2))
            elif p.color != self.color:
                moves.append((j - 1, i + 2))

        # up left
        if i > 1 and j > 0:
            p = board[i - 2][j - 1]
            if p == 0:
                moves.append((j - 1, i - 2))
            elif p.color != self.color:
                moves.append((j - 1, i - 2))

        # down right
        if i < 6 and j < 7:
            p = board[i + 2][j + 1]
            if p == 0:
                moves.append((j + 1, i + 2))
            elif p.color != self.color:
                moves.append((j + 1, i + 2))

        # up right
        if i > 1 and j < 7:
            p = board[i - 2][j + 1]
            if p == 0:
                moves.append((j + 1, i - 2))
            elif p.color != self.color:
                moves.append((j + 1, i - 2))
        return moves


class Pawn(Piece):
    img = 3

    def __init__(self, row, col, color):
        super().__init__(row, col, color)
        self.first = True
        self.queen = False

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        if self.color == "b":
            if self.first:
                if i < 6:
                    p = board[i + 2][j]
                    if p == 0:
                        moves.append((j, i + 2))

            if i < 7:
                p = board[i + 1][j]
                if p == 0:
                    moves.append((j, i + 1))

                # diagonal
                if j < 7:
                    p = board[i + 1][j + 1]
                    if p != 0 and p.color != self.color:
                        moves.append((j + 1, i + 1))

                if j > 0:
                    p = board[i + 1][j - 1]
                    if p != 0 and p.color != self.color:
                        moves.append((j - 1, i + 1))
        else:
            if self.first:
                if i > 1:
                    p = board[i - 2][j]
                    if p == 0:
                        moves.append((j, i - 2))

            if i > 0:
                p = board[i - 1][j]
                if p == 0:
                    moves.append((j, i - 1))

                # diagonal
                if j < 7:
                    p = board[i - 1][j + 1]
                    if p != 0 and p.color != self.color:
                        moves.append((j + 1, i - 1))

                if j > 0:
                    p = board[i - 1][j - 1]
                    if p != 0 and p.color != self.color:
                        moves.append((j - 1, i - 1))
        return moves


class Queen(Piece):
    img = 4

    def valid_moves(self, board):
        """
        i = self.row
        j = self.col

        moves = []

        # up right diagonal
        currentCol = j
        for row in range(0, 8):
            if currentCol - 1 >= 0:
                m1 = board[row][currentCol - 1]
            if currentCol + 1 <= 7:
                m2 = board[row][currentCol + 1]

            currentCol += 1
        """
        return []


class Rook(Piece):
    img = 5

    def valid_moves(self, board):
        i = self.row
        j = self.col

        moves = []
        # up
        for x in range(i, -1, -1):
            p = board[i][j]
            if p == 0:
                moves.append((j, x))
                break

        # down
        for x in range(i, 8, 1):
            p = board[i][j]
            if p == 0:
                moves.append((j, x))
                break

        # left
        for x in range(j, -1, -1):
            p = board[i][j]
            if p == 0:
                moves.append((x, i))
                break

        # right
        for x in range(j, 8, 1):
            p = board[i][j]
            if p == 0:
                moves.append((x, i))
                break

        return moves
