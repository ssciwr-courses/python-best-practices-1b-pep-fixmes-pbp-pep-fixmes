import os
import re
import subprocess
from pathlib import Path


def test_flake8():
    # Get the repository directory
    current_dir = Path(__file__).resolve().parents[1]
    input_file_path = current_dir / "chapter1"
    # run flake8 on the example files
    command = "flake8 {}".format(input_file_path)
    failure = 0
    try:
        subprocess.check_output(command, shell=True)
    except subprocess.CalledProcessError as e:
        failure = e.returncode
    # if there are some, print the differences and calculate no of errors
    if failure == 1:
        os.system("flake8 {}".format(input_file_path))
        print("Please try again!")
    else:
        print("No stylistic errors found!")
    assert failure == 0


def test_german_name():
    # Kreis in example 2
    current_dir = Path(__file__).resolve().parents[1]
    input_file = current_dir / "chapter1" / "example2.py"
    # figure out if the word "Kreis" is in the file
    with open(input_file, "r") as f:
        file_content = f.read()
    assert "Kreis" not in file_content


def test_intrinsic_function():
    # check variable name in example3
    current_dir = Path(__file__).resolve().parents[1]
    input_file = current_dir / "chapter1" / "example3.py"
    # make sure the intrinsic "list" function is not used as a variable name
    with open(input_file, "r") as f:
        file_content = f.read()
    # find all appearances of "list" in the file
    find_list = [i.start() for i in re.finditer("list", file_content)]
    not_accepted_characters = [" ", ":"]
    failure = 0
    for i in find_list:
        check_last_character = file_content[i + 4]
        if check_last_character in not_accepted_characters:
            print(
                """Found 'list' as variable name in the file!
                Please change the variable name."""
            )
            print(file_content[i:i+5])
            failure = 1
    assert failure == 0
