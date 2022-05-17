# CustomWiper
A Python package that wipes data by overwriting it with custom content.
Be careful, there are no warnings and sanity checks. I'm not responsible
if you wipe your hard drive with precious family photos or something.

## Motivation
I've written CustomWiper to brush up on my Python skills and to learn
basic stuff about Jenkins. The continuous integration is performed
by my Jenkins instance (accessible at
[jenkins.darkognu.eu](https://jenkins.darkognu.eu/)).

## Usage

```console
[darkognu@ArchLenovo src]$ ./wiper
usage: __main__.py [-h] [-p [PATH]] [-f [PATH]] [-t [TEXT]]

Wipe a file, directory, or disk, all with your custom content.

options:
  -h, --help            Show this help message and exit.
  -p [PATH], --path [PATH]
                        Wipe the following path.
  -f [PATH], --file [PATH]
                        Wipe using contents of the following file. The file will be loaded into RAM, so using big files is discouraged
  -t [TEXT], --text [TEXT]
                        Wipe using the following text.

--file and --text can't appear simultaneously.
```

## Results

```console
[darkognu@ArchLenovo src]$ sudo ./CustomWiper --path /dev/loop0 --text "life sucks "
[darkognu@ArchLenovo src]$ sudo xxd /dev/loop0 | head
00000000: 6c69 6665 2073 7563 6b73 206c 6966 6520  life sucks life 
00000010: 7375 636b 7320 6c69 6665 2073 7563 6b73  sucks life sucks
00000020: 206c 6966 6520 7375 636b 7320 6c69 6665   life sucks life
00000030: 2073 7563 6b73 206c 6966 6520 7375 636b   sucks life suck
00000040: 7320 6c69 6665 2073 7563 6b73 206c 6966  s life sucks lif
00000050: 6520 7375 636b 7320 6c69 6665 2073 7563  e sucks life suc
00000060: 6b73 206c 6966 6520 7375 636b 7320 6c69  ks life sucks li
00000070: 6665 2073 7563 6b73 206c 6966 6520 7375  fe sucks life su
00000080: 636b 7320 6c69 6665 2073 7563 6b73 206c  cks life sucks l
00000090: 6966 6520 7375 636b 7320 6c69 6665 2073  ife sucks life s
```
