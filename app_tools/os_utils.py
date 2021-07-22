import os
import shutil
import sys


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


def copy_tmp_file(old_file):
    new_file = old_file + "tmp"
    shutil.copy(old_file, new_file)
    print("Make copy {}. Done!".format(new_file))
