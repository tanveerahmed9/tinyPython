#!/usr/bin/env python3
"""
Author : Tanveer Ahmed
Date   : 2024-07-21
Purpose: Create Howler Module
When user Passes a string lets say (This is outrageous!) , this should print (THIS IS OUTRAGEOUS!), 
if the user passes content of the file it should read content and print the all upperCase as described above
The program should give the way to output the result to a file , when the output to file option is given it should print in the screen

"""

"""
Validations to be done

1) When user passes the --board or -b parameter , the values can be either x or o or . and in total it has be to be length of exactly 9
   for example x...00.x. --> Pass x..00 --> Fail , x....oooD --> fail
2) --cell value can only be from 1-9
3) --player can only take x and 0
3) --player and --cell both should go together or dont go at all 

"""


import argparse
import re

# --------------------------------------------------
def get_args():
       """Get command-line arguments"""

       parser = argparse.ArgumentParser(
           description='Create Howler Module',
           formatter_class=argparse.ArgumentDefaultsHelpFormatter)

       parser.add_argument('-b',
                           '--board',
                           help='Initial Board State',
                           metavar='board',
                           type=str,
                           default='.' * 9)

       parser.add_argument('-p',
                           '--player',
                           help='Player (X or O)',
                           choices='XO',
                           metavar='Player',
                           type=str,
                           default=None)

       parser.add_argument('-c',
                           '--cell',
                           help='Cell (1-9)',
                           metavar='cell',
                           type=int,
                           choices=range(1, 10),
                           default=None)

       args = parser.parse_args()

       if any([args.player, args.cell]) and not all([args.player, args.cell]):
           parser.error("Must provide both player and cell or neither")

       if not re.search('^[.XO]{9}$', args.board):
           parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

       if args.cell and args.board[args.cell - 1] in 'XO':
           parser.error(f'Cell "{args.cell}" already taken')

       return args


def format_board(board):
    """Format the playing board"""
    cells = [str(i) if c == '.' else c for i, c in enumerate(board, 1)]
    bar = '-------------'
    cells_template = '| {} | {} | {} |'
    board = '\n'.join([
        bar,
        cells_template.format(*cells[:3]),
        bar,
        cells_template.format(*cells[3:6]),
        bar,
        cells_template.format(*cells[6:]),
        bar
    ])
    return board

def find_winner(board):
    """Determine the winner of the match based on board state , if no winner present return draw"""
    winning = ([0,1,2], [3,4,5], [6,7,8], [0,4,8], [1,4,7], [2,5,8])
    for player in ['X', 'O']:
        for i , j , k in winning:
           combo = [board[i], board[j], board[k]] 
           if combo == [player,player,player]:
               return player 


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()
    board = list(args.board)
    print(format_board(board))

    if args.player and args.cell:
        board[args.cell -1] = args.player

    winner = find_winner(board)
    print(f'{winner} has Won!' if winner else 'No Winner')
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
