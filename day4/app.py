import sys
import cmd

class app(cmd.Cmd):

    prompt = " ~$ "
    
    def do_create(self, line):
        print("Command Create\n")

    def do_list(self, line):
        print("Command List\n")

    def do_exit(self, line):
        print()
        sys.exit()

if __name__ == "__main__":
    app().cmdloop()