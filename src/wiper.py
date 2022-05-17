from dataclasses import dataclass
from pathlib import Path
from argparse import ArgumentParser
from sys import argv, exit


@dataclass
class Data:
    path: Path
    content: bytes


def inflate(content):
    while len(content) < 32768:
        content += content

    return content


def interpret_args(args):
    path = Path(args.path)

    if not path.exists():
        print("The path you're trying to wipe ({0}) is invalid."
              .format(args.path))
        exit()

    if args.text is not None:
        return Data(path, inflate(str.encode(args.text)))

    content_path = Path(args.file)

    if not content_path.exists():
        print("Your file path ({0}) is invalid."
              .format(args.file))
        exit()

    try:
        with open(content_path, "r+b") as file:
            return Data(path, inflate(file.read()))
    except IOError:
        file.close()


def parse_args(args):
    parser = ArgumentParser(
        description="Wipe a file, directory, or disk,"
                    "all with your custom content.",
        add_help=False,
        epilog="--file and --text can't appear simultaneously.")

    parser.add_argument('-h', '--help', action='store_true',
                        help="Show this help message and exit.")
    parser.add_argument('-p', '--path', nargs='?',
                        help="Wipe the following path.",
                        metavar='PATH')
    parser.add_argument('-f', '--file', nargs='?',
                        help="Wipe using contents of the following file."
                             "The file will be loaded into RAM, so using big"
                             "files is discouraged",
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


def wipe_file(path, content, pos):
    # For block devices
    if path.is_block_device():
        try:
            with open(path, "w+b") as file:
                while True:
                    file.write(content)
        except IOError:
            return 0

    # For files
    try:
        size = path.stat().st_size
        write_pos = 0
        with open(path, "w+b") as file:
            while write_pos < size:
                available_content = len(content) - pos
                available_len = size - write_pos
                if available_len > available_content:
                    file.write(content[pos:])
                    pos = 0
                    write_pos += available_content
                else:
                    file.write(content[pos:pos + available_len])
                    pos += available_len
                    write_pos = size

                if pos > len(content):
                    pos = 0

    except IOError:
        print("Can't overwrite " + str(path))

    return pos


def main():
    args = parse_args(argv[1:])

    if args.path.is_file() or args.path.is_block_device():
        wipe_file(args.path, args.content, 0)
    else:
        pos = 0
        for path in args.path.rglob("*"):
            if path.is_file():
                pos = wipe_file(path, args.content, pos)


if __name__ == '__main__':
    main()
