import argparse
import sys
import os

def validate_args(args):
    if len(args) == 0:
        print()

    return "xd "


def main():
    print(sys.argv)
    path = validate_args(sys.argv)


if __name__ == '__main__':
    main()
