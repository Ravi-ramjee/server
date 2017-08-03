import os


infile = open("input.txt", "w")
outfile = open("output.txt", "r")

while True:
    cmd = input("> ")
    if cmd == "QUIT_SHELL":
        break
    infile.write(cmd)
    print(outfile.read())

infile.close()
outfile.close()

