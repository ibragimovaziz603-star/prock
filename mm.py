import pygame
import sys

pygame.init()

# ============ SOZLAMALAR ============
WIDTH, HEIGHT = 640, 700
SQUARE = 80
BOARD_SIZE = 8
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("♟️ Shaxmat O'yini")

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
BG = (40, 40, 40)
TEXT_COLOR = (255, 255, 255)

font = pygame.font.SysFont("Segoe UI Symbol", 60)
small_font = pygame.font.SysFont("Arial", 20, bold=True)
big_font = pygame.font.SysFont("Arial", 32, bold=True)

board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
]

PIECES = {
    'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚', 'p': '♟',
    'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
}

selected = None
current_turn = 'white'
valid_moves = []
last_move = None
game_over = False
status_msg = "OQ yurishi"


def is_white(piece):
    return piece.isupper()


def is_black(piece):
    return piece.islower()


def get_piece_moves(board, row, col):
    piece = board[row][col]
    if not piece:
        return []

    moves = []
    white = is_white(piece)
    p = piece.lower()

    def enemy(r, c):
        if not (0 <= r < 8 and 0 <= c < 8):
            return False
        target = board[r][c]
        if not target:
            return False
        return (white and is_black(target)) or (not white and is_white(target))

    def empty(r, c):
        return 0 <= r < 8 and 0 <= c < 8 and board[r][c] == ''

    if p == 'p':
        direction = -1 if white else 1
        start_row = 6 if white else 1
        if empty(row + direction, col):
            moves.append((row + direction, col))
            if row == start_row and empty(row + 2 * direction, col):
                moves.append((row + 2 * direction, col))
        for dc in [-1, 1]:
            nr, nc = row + direction, col + dc
            if enemy(nr, nc):
                moves.append((nr, nc))

    elif p == 'r':
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if empty(nr, nc):
                    moves.append((nr, nc))
                elif enemy(nr, nc):
                    moves.append((nr, nc))
                    break
                else:
                    break
                nr += dr
                nc += dc

    elif p == 'b':
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if empty(nr, nc):
                    moves.append((nr, nc))
                elif enemy(nr, nc):
                    moves.append((nr, nc))
                    break
                else:
                    break
                nr += dr
                nc += dc

    elif p == 'q':
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if empty(nr, nc):
                    moves.append((nr, nc))
                elif enemy(nr, nc):
                    moves.append((nr, nc))
                    break
                else:
                    break
                nr += dr
                nc += dc

    elif p == 'k':
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = row + dr, col + dc
                if empty(nr, nc) or enemy(nr, nc):
                    moves.append((nr, nc))

    elif p == 'n':
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                       (1, -2), (1, 2), (2, -1), (2, 1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                if empty(nr, nc) or enemy(nr, nc):
                    moves.append((nr, nc))

    return moves


def draw_board():
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            color = LIGHT if (r + c) % 2 == 0 else DARK
            pygame.draw.rect(screen, color, (c * SQUARE, r * SQUARE, SQUARE, SQUARE))
    for i in range(8):
        num = small_font.render(str(8 - i), True, (80, 80, 80))
        screen.blit(num, (3, i * SQUARE + 3))
        letter = small_font.render(chr(ord('a') + i), True, (80, 80, 80))
        screen.blit(letter, (i * SQUARE + SQUARE - 18, 8 * SQUARE - 22))


def draw_pieces():
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece:
                text_shadow = font.render(PIECES[piece], True, (0, 0, 0))
                screen.blit(text_shadow, (c * SQUARE + 12, r * SQUARE + 8))
                color = (255, 255, 255) if is_white(piece) else (30, 30, 30)
                text = font.render(PIECES[piece], True, color)
                screen.blit(text, (c * SQUARE + 10, r * SQUARE + 5))


def draw_highlights():
    if last_move:
        fr, fc, tr, tc = last_move
        s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        s.fill((255, 215, 0, 80))
        screen.blit(s, (fc * SQUARE, fr * SQUARE))
        screen.blit(s, (tc * SQUARE, tr * SQUARE))
    if selected:
        r, c = selected
        s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        s.fill((100, 200, 100, 150))
        screen.blit(s, (c * SQUARE, r * SQUARE))
    for r, c in valid_moves:
        center = (c * SQUARE + SQUARE // 2, r * SQUARE + SQUARE // 2)
        if board[r][c]:
            pygame.draw.circle(screen, (220, 50, 50), center, SQUARE // 2 - 4, 4)
        else:
            s = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
            pygame.draw.circle(s, (50, 100, 50, 120), (SQUARE // 2, SQUARE // 2), 12)
            screen.blit(s, (c * SQUARE, r * SQUARE))


def draw_status():
    panel = pygame.Rect(0, 8 * SQUARE, WIDTH, HEIGHT - 8 * SQUARE)
    pygame.draw.rect(screen, BG, panel)
    msg = status_msg
    if game_over:
        msg = status_msg + "  —  R bosing"
    text = big_font.render(msg, True, TEXT_COLOR)
    rect = text.get_rect(center=(WIDTH // 2, 8 * SQUARE + 30))
    screen.blit(text, rect)
    hint = small_font.render("R - qaytadan  |  ESC - chiqish", True, (180, 180, 180))
    hint_rect = hint.get_rect(center=(WIDTH // 2, 8 * SQUARE + 55))
    screen.blit(hint, hint_rect)
    color = (255, 255, 255) if current_turn == 'white' else (60, 60, 60)
    pygame.draw.circle(screen, color, (30, 8 * SQUARE + 30), 12)
    pygame.draw.circle(screen, (150, 150, 150), (30, 8 * SQUARE + 30), 12, 2)


def check_king_captured():
    has_white_king = any('K' in row for row in board)
    has_black_king = any('k' in row for row in board)
    if not has_white_king:
        return "QORA YUTDI!"
    if not has_black_king:
        return "OQ YUTDI!"
    return None


def main():
    global selected, current_turn, valid_moves, last_move, game_over, status_msg

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    board[:] = [
                        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                        ['', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', ''],
                        ['', '', '', '', '', '', '', ''],
                        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                    ]
                    selected = None
                    current_turn = 'white'
                    valid_moves = []
                    last_move = None
                    game_over = False
                    status_msg = "OQ yurishi"

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                col = x // SQUARE
                row = y // SQUARE

                if 0 <= row < 8 and 0 <= col < 8:
                    piece = board[row][col]

                    if selected:
                        sr, sc = selected
                        if (sr, sc) == (row, col):
                            selected = None
                            valid_moves = []
                        elif (row, col) in valid_moves:
                            board[row][col] = board[sr][sc]
                            board[sr][sc] = ''
                            last_move = (sr, sc, row, col)
                            result = check_king_captured()
                            if result:
                                game_over = True
                                status_msg = result
                            else:
                                current_turn = 'black' if current_turn == 'white' else 'white'
                                status_msg = "QORA yurishi" if current_turn == 'black' else "OQ yurishi"
                            selected = None
                            valid_moves = []
                        elif piece and ((current_turn == 'white' and is_white(piece)) or
                                        (current_turn == 'black' and is_black(piece))):
                            selected = (row, col)
                            valid_moves = get_piece_moves(board, row, col)
                        else:
                            selected = None
                            valid_moves = []
                    else:
                        if piece and ((current_turn == 'white' and is_white(piece)) or
                                      (current_turn == 'black' and is_black(piece))):
                            selected = (row, col)
                            valid_moves = get_piece_moves(board, row, col)

        screen.fill(BG)
        draw_board()
        draw_highlights()
        draw_pieces()
        draw_status()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()