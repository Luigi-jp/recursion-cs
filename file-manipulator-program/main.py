import sys

args = sys.argv
command = args[1]
input_file_path = args[2]
output_file_path = args[3]

contents = ""

with open(input_file_path) as f:
    contents = f.read()

match command:
    case "reverse":
        contents = contents[::-1]
    case _:
        print("Invalid command.")
        exit()


with open(output_file_path, "w") as f:
    f.write(contents)