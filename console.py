#!/usr/bin/env python3
"""Command Interpreter"""
import cmd
import sys
from models.engine.file_storage import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command Interpreter Class"""
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "Amenity", "Place", "Review"]

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True

    def do_help(self, arg):
        """Print help message"""
        super().do_help(arg)

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(f"(args[0])()")
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in objects.items() if args[0] in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        setattr(obj, args[2], eval(args[3]))
        obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
