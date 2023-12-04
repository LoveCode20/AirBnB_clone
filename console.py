#!/usr/bin/env python3
"""
Creation of a console that performs Command line interpreting
"""
import cmd


class Console(cmd.Cmd):
    prompt = "(hbnb)"

    def do_EOF(self, line):
        """method that defines the end of the line"""
        return True
    
    def do_quit(self, line):
        """method that defines the quit command"""
        return self.do_EOF(line)
if __name__ == '__main__':
    Console().cmdloop()
