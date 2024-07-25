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

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-b',
                        '--board',
                        help='Initial Board State',
                        metavar='str',
                        type=str,
                        default='.' * 9)

    parser.add_argument('-p',
                        '--player',
                        help='A named integer argument',
                        choices='XO',
                        metavar='Player',
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='Cell',
                        metavar='str',
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='cell value',
                        action='store_true')
    

    args = parser.parse_args()
    if any ([args.player, args.cell] and not all([args.player,args.cell])): # condition to check the player and cell combination
        parser.error("Must provide both player and Cell or None")

    if not re.search('^[.XO]{9}$',args.board): # regex to match the pattern when --boards in passed
        parser.error(f'--board "{args.board}" must be character of 9 length and in ., X, O')

    if args.player and args.cell and args.board[args.cell -1] in 'XO': # if the cell is already occupied
        parser.error(f'--cell "{args.cell}" already Taken')




def format_board(board):
    """Format the playing board"""
    return board

def find_winner(board):
    """Determine the winner of the match based on board state , if no winner present return draw"""
    pass


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
