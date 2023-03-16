import sys
import cmd

class app(cmd.Cmd):

    prompt = " ~$ "
    
    def do_create(self, line):
        if line != "":
            with open("names.txt", "a") as file:
                file.write(f"{line}\n")

        else:
            name = input("Name: ").strip()
            with open("names.txt", "a") as file:
                file.write(f"{name}\n")

        print()

    def do_list(self, line):
        names = []
        with open("names.txt") as file:
            names = file.readlines()

        for i in names:
            print(f"{i}", end="")

        print()

    def do_exit(self, line):
        print()
        sys.exit()

if __name__ == "__main__":
    app().cmdloop()