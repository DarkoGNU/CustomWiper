from dataclasses import dataclass
from pathlib import Path
from argparse import ArgumentParser
from sys import argv, exit


# except IOError as e:
# print("Can't read " + args.file)
# print("I/O Error ({0}): {1}".format(e.errno, e.strerror))
# exit()


@dataclass
class Data:
    path: Path
    content: bytes | Path


def interpret_args(args):
    path = Path(args.path)

    if not path.exists():
        print("The path you're trying to wipe ({0}) is invalid."
              .format(args.path))
        exit()

    if args.text is not None:
        return Data(path, bytes(args.text))

    content_path = Path(args.file)

    if not content_path.exists():
        print("Your file path ({0}) is invalid."
              .format(args.file))
        exit()

    return Data(path, content_path)


def parse_args(args):
    parser = ArgumentParser(
        description='Wipe a file, directory, or disk, all with your custom content.',
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
        exit()

    return interpret_args(parsed)


def wipe_file(path):
    print("unimplemented")


def main():
    args = parse_args(argv[1:])

    if args.path.is_file():
        wipe_file(args.path)
    else:
        for path in args.path.rglob("*"):
            wipe_file(path)


if __name__ == '__main__':
    main()
