from dataclasses import dataclass
from pathlib import Path
import argparse
import sys


@dataclass
class Data:
    path: Path
    content: bytes


def interpret_args(args):
    path = Path(args.path)

    if not path.exists():
        print("The path you're trying to wipe ({0}) is invalid."
              .format(args.path))
        sys.exit()

    if args.text is not None:
        return Data(path, args.text)

    try:
        with Path(args.file) as file:
            return Data(path, file.read_bytes())
    except IOError as e:
        print("Can't read " + args.file)
        print("I/O Error ({0}): {1}".format(e.errno, e.strerror))
        sys.exit()


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Gets the path and content.',
        add_help=False,
        epilog="--file and --text can't appear simultaneously.")

    parser.add_argument('-h', '--help', action='store_true',
                        help="Show this help message and exit.")
    parser.add_argument('-p', '--path', nargs='?',
                        help="Wipe the following path.",
                        metavar='PATH')
    parser.add_argument('-f', '--file', nargs='?',
                        help="Wipe using contents of the following file.",
                        metavar='PATH')
    parser.add_argument('-t', '--text', nargs='?',
                        help="Wipe using the following text.",
                        metavar='TEXT')

    parsed = parser.parse_args(args)

    if (parsed.help or parsed.path is None
            or (parsed.file is not None and parsed.text is not None)
            or (parsed.file is None and parsed.text is None)):
        parser.print_help()
        sys.exit()

    return interpret_args(parsed)


def main():
    args = parse_args(sys.argv[1:])


if __name__ == '__main__':
    main()
