# CustomWiper
A Python package that wipes data by overwriting it with custom content.

```commandline
python __main__.py --help
usage: __main__.py [-h] [-p [PATH]] [-f [PATH]] [-t [TEXT]]

Gets the path and content.

options:
  -h, --help            Show this help message and exit.
  -p [PATH], --path [PATH]
                        Wipe the following path.
  -f [PATH], --file [PATH]
                        Wipe using contents of the following file.
  -t [TEXT], --text [TEXT]
                        Wipe using the following text.

--file and --text can't appear simultaneously.
```
