import os
import sys

args = sys.argv

if len(args) < 2:
    print("Invalid number of arguments.")
    exit()

command = args[1]

# TODO: バリデーションを関数に切り出す
match command:
    case "reverse":
        if len(args) != 4:
            print("Invalid number of arguments for reverse command.")
            exit()

        if not os.path.isfile(args[2]):
            print("Invalid input file path.")
            exit()
        
        input_file_path = args[2]
        output_file_path = args[3]
    case "copy":
        if len(args) != 4:
            print("Invalid number of arguments for copy command.")
            exit()

        if not os.path.isfile(args[2]):
            print("Invalid input file path.")
            exit()
        
        input_file_path = args[2]
        output_file_path = args[3]
    case "duplicate-contents":
        if len(args) != 4:
            print("Invalid number of arguments for duplicate-contents command.")
            exit()

        if not os.path.isfile(args[2]):
            print("Invalid input file path.")
            exit()
        
        if not args[3].isdigit():
            print("Invalid number of duplicates. Please provide a valid number.")
            exit()

        input_file_path = args[2]
        duplicates_number = int(args[3])
    case "replace-string":
        if len(args) != 5:
            print("Invalid number of arguments for replace-string command.")
            exit()

        if not os.path.isfile(args[2]):
            print("Invalid input file path.")
            exit()

        input_file_path = args[2]
        replace_str = args[3]
        new_str = args[4]
    case _:
        print("Invalid command. \nPlease use one of the following commands: \nreverse, copy, duplicate-contents, replace-string")
        exit()

content = ""

with open(input_file_path) as f:
    content = f.read()

# TODO: コマンドごとに処理を関数に切り出す
match command:
    case "reverse":
        content = content[::-1]
        
        with open(output_file_path, "w") as f:
            f.write(content)
    case "copy":
        with open(output_file_path, "w") as f:
            f.write(content)
    case "duplicate-contents":
        duplicate_content = content
        for i in range(duplicates_number):
            content += f"\n{duplicate_content}"
        
        with open(input_file_path, "w") as f:
            f.write(content)
    case "replace-string":
        content = content.replace(replace_str, new_str)

        with open(input_file_path, "w") as f:
            f.write(content)

