import sys
from fileutilities import FileUtilities as util
from llminterface import LLMInterface


def main():
    if len(sys.argv) < 1:
        raise Exception("No input file given.")

    input_file = sys.argv[1]
    input = util.read_file(input_file)

    llm = LLMInterface()
    python_code = llm.convert_pseudocode(input)

    util.write_file("temp.py", python_code)
    util.execute_script("temp.py")
    util.delete_file("temp.py")


main()
