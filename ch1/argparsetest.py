"""
Author = Tanveer Ahmed
Purpose = Hello test
"""
import argparse

def get_args():
    """
    Get and parses the argument
    """
    parser = argparse.ArgumentParser(description="Say The Name")
    parser.add_argument('-n', '--name', metavar='name',help='Name to greet')
    parser.add_argument('-a', '--age', metavar='age', default='0', help='Put the age of the user')
    parser.add_argument('class', help='Put the class of the user')
    return parser.parse_args()

def main():
    """
    main
    """
    args = get_args()
    name = args.name
    age = args.age
    print("Hello " + name +  "How are you?" + "you are " + age + "Years old" )

if __name__ == '__main__':
    main()
