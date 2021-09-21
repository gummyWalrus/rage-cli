#!/bin/python3
import sys
import re
import os
from time import sleep

def print_help():
    print(
        '''
        USAGE
            ragecli <software> [OPTIONS]
            for a list of available options use ragecli -h or --help 
        '''
    )
    exit(84)

def print_man():
    print(
        '''
        Ragecli prints a customized string, that's all. It can help when you are in pain because of a software or lib not working.
        USAGE
            ragecli <software> [OPTIONS]
            for a list of available options use ragecli -h or --help
        CUSTOMIZATION
            Use $USER and $SOFTWARE in the passphrase to place your values.
        OPTIONS
            --phrase sets your custom phrase, this is where you set variables position
            --user sets your user name, if not specified, $USER env var will be used
        '''
    )

def main():
    phrase = "$SOFTWARE qui ne marche pas rend $USER fou !"
    user = os.environ.get('USER')
    soft = None
    for arg in sys.argv:
        print(arg)
        if arg.startswith("--phrase"):
            phrase = re.search(r"=(.+)", arg)
            if phrase != None:
                phrase = phrase.group()
            else:
                print('Missing argument for option "--phrase".\nExample : --phrase=<your phrase>')
                print_help()
        elif arg.startswith('--user'):
            user = re.search(r"=(.+)", arg)
            if user != None:
                user = soft.group()
            else:
                print('Missing argument for option "--user".\nExample : --user=<your name>')
                print_help()
        else: 
            soft = arg
    if soft == None:
        print("software name is required")
        print_help()
    phrase = phrase.replace("$SOFTWARE", soft)
    phrase = phrase.replace("$USER", user)
    return phrase


try:
    phrase = main()
    while 42:
        print(phrase)
        sleep(1)
except KeyboardInterrupt:
    exit(84)
