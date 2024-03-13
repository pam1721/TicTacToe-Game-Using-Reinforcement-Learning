from game_logic import TicTacToe
from r1_agent import RLAgent
def play_game():
    game = TicTacToe()
    player_symbol = input("Choose your symbol (X or O): ").upper()
    while player_symbol not in ['X', 'O']:
        player_symbol = input("Invalid symbol. Please choose X or O: ").upper()
    if player_symbol == 'X':
        player = RLAgent('X')
        opponent = RLAgent('O')
    else:
        player = RLAgent('O')
        opponent = RLAgent('X')
    while not game.game_over():
        if game.current_winner is None:
            game.print_board()
            if game.current_winner is None and player.symbol == 'X':
                print("It's your turn.")
                available_moves = game.available_moves()
                player_action = int(input("Enter your move (0-8): "))
                while player_action not in available_moves:
                    player_action = int(input("Invalid move. Please enter your move (0-8): "))
                game.make_move(player_action, player.symbol)
                if game.game_over():
                    break
            if game.current_winner is None and opponent.symbol == 'X':
                print("Opponent's turn.")
                available_moves = game.available_moves()
                opponent_action = opponent.choose_action(available_moves, game.board)
                game.make_move(opponent_action, opponent.symbol)
                if game.game_over():
                    break
            if game.current_winner is None and player.symbol == 'O':
                print("It's your turn.")
                available_moves = game.available_moves()
                player_action = int(input("Enter your move (0-8): "))
                while player_action not in available_moves:
                    player_action = int(input("Invalid move. Please enter your move (0-8): "))
                game.make_move(player_action, player.symbol)
                if game.game_over():
                    break
            if game.current_winner is None and opponent.symbol == 'O':
                print("Opponent's turn.")
                available_moves = game.available_moves()
                opponent_action = opponent.choose_action(available_moves, game.board)
                game.make_move(opponent_action, opponent.symbol)
                if game.game_over():
                    break
    game.print_board()
    if game.current_winner:
        print(f"{game.current_winner} wins!")
    else:
        print("It's a tie!")
play_game()
