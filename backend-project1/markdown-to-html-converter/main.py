import markdown
import os
import sys

args = sys.argv
if len(args) != 4:
    print("Usage: python main.py markdown input.md output.html")
    sys.exit(1)

command = args[1]

match command:
    case "markdown":
        input_file_path = args[2]
        output_file_path = args[3]

        if not os.path.isfile(input_file_path):
            print("Invalid input file path.")
            sys.exit(1)
        
        with open(input_file_path) as f:
            markdown_text = f.read()

        html_text = markdown.markdown(markdown_text, extensions=['tables'])

        with open(output_file_path, "w") as f:
            f.write(html_text)
    case _:
        print("Invalid command.")
        sys.exit(1)
