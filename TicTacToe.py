import matplotlib.pyplot as plt
import numpy as np

# Initialize the game board (9 positions in a single list).
# Each position can be ' ', 'X', or 'O'.
game_board = [' ' for _ in range(9)]

# This list will store the sequence of moves made by AI (X) or Player (O).
# Each entry is a tuple in the form: ('X' or 'O', position)
game_history = []

def display_board(game_board):
    """
    Display the Tic-Tac-Toe board using Matplotlib.

    :param game_board: A list of 9 characters representing the board state.
                       Each index corresponds to a position from 0 to 8.
    """
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    
    # Draw the 2 vertical and 2 horizontal grid lines.
    for i in range(1, 3):
        ax.plot([0, 3], [i, i], color='black', lw=2)
        ax.plot([i, i], [0, 3], color='black', lw=2)
    
    # Add 'X' or 'O' text to each cell if it is occupied.
    for row in range(3):
        for col in range(3):
            cell_value = game_board[row * 3 + col]
            if cell_value == 'X':
                ax.text(col + 0.5, 2.5 - row, 'X', fontsize=20, 
                        ha='center', va='center', color='red')
            elif cell_value == 'O':
                ax.text(col + 0.5, 2.5 - row, 'O', fontsize=20, 
                        ha='center', va='center', color='blue')
    
    # Remove axes from the figure for a clean look.
    ax.axis('off')
    plt.show()


def evaluate_board_state(game_board):
    """
    Evaluate the board to check if there is a winner.

    :param game_board: Current state of the board, represented as a list of 9 characters.
    :return: 1 if 'X' has won, -1 if 'O' has won, and 0 otherwise.
    """
    win_conditions = [
        # Rows
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        # Columns
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        # Diagonals
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    for condition in win_conditions:
        if (game_board[condition[0]] == game_board[condition[1]] ==
            game_board[condition[2]] != ' '):
            return 1 if game_board[condition[0]] == 'X' else -1
    
    return 0


def minimax_evaluation(game_board, depth, is_maximizing):
    """
    Minimax algorithm to evaluate the optimal move for the AI (X).

    :param game_board: Current state of the board as a list of 9 characters.
    :param depth: Depth of the recursive search (unused here, but often used for alpha-beta pruning).
    :param is_maximizing: Boolean indicating whether we are maximizing (AI) or minimizing (Player).
    :return: The best achievable score from the perspective of the AI:
             +1 if it leads to a winning outcome for X,
             -1 for a winning outcome for O,
             0 for a draw.
    """
    current_score = evaluate_board_state(game_board)

    # If we detect a win or draw, return the corresponding score immediately.
    if current_score == 1:
        return 1  # X has won
    if current_score == -1:
        return -1  # O has won
    if ' ' not in game_board:
        return 0  # Draw

    if is_maximizing:
        # For AI (X), we try to maximize the score.
        best_score = -float('inf')
        for position in range(9):
            if game_board[position] == ' ':
                game_board[position] = 'X'  # Simulate AI's move
                score = minimax_evaluation(game_board, depth + 1, False)
                game_board[position] = ' '  # Undo the move (backtrack)
                best_score = max(score, best_score)
        return best_score
    else:
        # For Player (O), we try to minimize the score.
        best_score = float('inf')
        for position in range(9):
            if game_board[position] == ' ':
                game_board[position] = 'O'  # Simulate Player's move
                score = minimax_evaluation(game_board, depth + 1, True)
                game_board[position] = ' '  # Undo the move (backtrack)
                best_score = min(score, best_score)
        return best_score


def find_best_move_for_ai(game_board):
    """
    Find the optimal move for the AI (X) using the Minimax algorithm.

    :param game_board: Current state of the board as a list of 9 characters.
    :return: The position (0-8) that leads to the best outcome for the AI.
    """
    best_score = -float('inf')
    best_position = -1
    move_analysis = []

    # Iterate over every cell; if it's empty, evaluate the resulting board.
    for position in range(9):
        if game_board[position] == ' ':
            game_board[position] = 'X'  # AI's tentative move
            score = minimax_evaluation(game_board, 0, False)
            move_analysis.append((position, score))
            game_board[position] = ' '  # Undo the move

            # Keep track of the highest score (best move).
            if score > best_score:
                best_score = score
                best_position = position

    print("Move Analysis (Position: Score):", move_analysis)
    return best_position


def plot_evaluation_bar_graph(game_board):
    """
    Plot a bar graph of the evaluation scores for each empty position on the board.

    :param game_board: Current state of the board as a list of 9 characters.
    """
    # Calculate the Minimax score for all empty positions.
    evaluation_scores = [
        minimax_evaluation(game_board, 0, False) if cell == ' ' else None
        for cell in game_board
    ]
    
    print("Scores for empty positions:", evaluation_scores)  # Debug info
    
    # Identify which positions are empty and have a score.
    empty_positions = [
        index for index, score in enumerate(evaluation_scores) if score is not None
    ]
    empty_position_scores = [score for score in evaluation_scores if score is not None]

    print("Positions with scores:", empty_positions)
    print("Scores:", empty_position_scores)
    
    # Only plot if we have at least one empty position.
    if empty_positions and empty_position_scores:
        plt.bar(empty_positions, empty_position_scores, color='blue', label='Empty positions')
        plt.xlabel('Board Position')
        plt.ylabel('Evaluation Score')
        plt.title('Evaluation Scores for Each Empty Position')
        plt.xticks(range(9), range(9))  # Label x-axis as positions 0-8.
        plt.legend()
        plt.show()


# ------------------------------ #
#            GAME LOOP           #
# ------------------------------ #

# Display the initial empty board.
display_board(game_board)

# Continue the game while there is at least one empty space on the board.
while ' ' in game_board:
    # Decide whose turn it is. If there is an odd number of empty spaces, it's AI's turn.
    if game_board.count(' ') % 2 == 1:  
        chosen_move = find_best_move_for_ai(game_board)  # AI decides best move.
        game_board[chosen_move] = 'X'  # Apply AI's move to the board.
        print("AI chose position:", chosen_move)
        game_history.append(('X', chosen_move))  # Record in history.
    else:
        # Player's turn (O). We expect a user input from 0 to 8.
        try:
            chosen_move = int(input("Enter your move (0-8): "))
            if game_board[chosen_move] == ' ':
                game_board[chosen_move] = 'O'
                game_history.append(('O', chosen_move))
            else:
                print("Invalid move! Cell is already occupied.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 0 and 8.")
            continue
    
    # Display the updated board after each move.
    display_board(game_board)

    # Plot a bar graph showing the evaluation scores for the remaining empty positions.
    plot_evaluation_bar_graph(game_board)
    
    # Check if the game has been won or drawn.
    if evaluate_board_state(game_board) == 1:
        print("AI wins!")
        break
    elif evaluate_board_state(game_board) == -1:
        print("Player wins!")
        break
    elif ' ' not in game_board:
        print("It's a draw!")
        break

# ------------------------------ #
#          GAME HISTORY          #
# ------------------------------ #

print("\nGame History:")
for player_symbol, position_moved in game_history:
    # This shows the progression of moves in chronological order.
    print(f"{player_symbol} moved to position {position_moved}")
