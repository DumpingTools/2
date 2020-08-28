"""
Project: 
author: DumpingTools
Python version: Python 3+
Tested on: Unix
--------------------------

"""
import argparse
import code
import os
import shutil
import time
import re
import subprocess

"""
Example Arguments
"""
parser = argparse.ArgumentParser()
parser.add_argument("-exploit", help="Performs DAST/SAST and generates an exploit writeup")
args = parser.parse_args()

if args.exploit:
    out = "Output" # decompiled data goes here
    d = shutil.copy(args.exploit, os.getcwd())
    os.system("apktool d " + args.exploit)
    print(os.listdir())
    print("----------------------")
    print(os.getcwd())
    print("-----Insert path to folder-----")
    x = "" #x variable
    """
    If you want to speed up the process by excluding the x input() then comment it out and add directory in the x variable
    """
    x = input("path=") #insert path to directory
    os.chdir(x)
    print(os.getcwd())
    print("----------------------")
    succesful_exe = 0
    failed_exe = 1
    default_files = ["AndroidManifest.xml",
            "apktool.yml",
            "resources.arsc"]
    default_folders = ["original",
            "res",
            "smali",
            "assents",
            "lib",
            "unknown",
            "smali_assets",
            "smali_classes2"]
    print(os.listdir())
    i = 0
    for default_files in os.listdir(x):
        print("---/\-----/\---/\---\nChecking",default_files[i])
        with open(default_files[i]) as check:
            checking = re.match(".com")
            i = i + 1
            if default_files.startswith(default_files[0]):
                with open(default_files[0], "rb") as BinaryXML:
                    array = bytearray(BinaryXML.read())
                    
                 # Project not finished - deprecated.



