#!/usr/bin/env python3

import shutil
import os

def main():
    os.chdir("/home/student/mycode/")

    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # The following line will create the directory if it does not exist already
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()

