import argparse
import sys
import os


def parse_args(args):
    parser = argparse.ArgumentParser(description='Gets the path and content.')
    parser.add_argument('-p', '--path', nargs='?', help="Wipe the following path.")
    parser.add_argument('-f', '--file', nargs='?', help="Wipe using contents of the following file.")
    parser.add_argument('-t', '--text', nargs='?', help="Wipe using the following text.")

    if len(args) != 4:
        parser.print_help()
        return None


def main():
    args = parse_args(sys.argv)


if __name__ == '__main__':
    main()
