#!/usr/bin/env python3
"""
Creation of a console that performs Command line interpreting
"""
import cmd


class Console(cmd.Cmd):
    prompt = "(hbnb)"
if __name__ == '__main__':
    Console().cmdloop()
