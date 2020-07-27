#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def getParser():
    parser = argparse.ArgumentParser(
        description = 'Performs selected operation'
    )

    parser.add_argument('-v', '--vim',
        action  = 'store',
        help    = 'local install vim at PATH',
        metavar = 'PATH'
    )

    return parser


def installVim(path):
    if not os.path.exists(path):
        print('Specified path does not exist')
        sys.exit(1)

    vimDirectory = 'vim'
    vimGithub    = 'https://github.com/vim/vim.git'
    vimLocalPath = path + vimDirectory

    ## XXX: install latest release instead of latest revision
    if os.path.exists(vimLocalPath):
        p = subprocess.Popen(['git', 'pull', 'origin', 'master'],
            cwd = vimLocalPath)
        p.wait()
    else:
        p = subprocess.Popen(['git', 'clone', '--depth', '1', vimGithub,
            vimDirectory], cwd = path)
        p.wait()

    p = subprocess.Popen(['./configure', '--prefix=' + vimLocalPath],
        cwd = vimLocalPath)
    p.wait()
    p = subprocess.Popen(['make'], cwd = vimLocalPath)
    p.wait()
    p = subprocess.Popen(['make', 'install'], cwd = vimLocalPath)
    p.wait()

    return


def main(argv):
    parser = getParser()
    args   = parser.parse_args()

    if args.vim:
        installVim(args.vim)

    return


if __name__ == '__main__':
    main(sys.argv[1:])
