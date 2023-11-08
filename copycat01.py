#!/usr/bin/env python3
"""Doing some things to directories and files using additional code"""
"""Written (sort of) by RyGilly"""

#import additional code
import shutil
import os

def main():
#move into the below directory
    os.chdir("/home/student/mycode/")

#copy the below file
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#copy an entire directory
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()

