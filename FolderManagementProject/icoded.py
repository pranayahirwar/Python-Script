import os
import sys
import shutil
import json
from subprocess import PIPE, run

#? Global Variable.
GAME_DIR_PATTERN = "game"
GAME_CODE_EXTENSION = ".go"
COMMANDS = ["go", "build"]

# Fucntion to get all the paths that contain GAME in them.
def allgame_dir_full_path(source):
    game_path = []

    for root, dirs, file in os.walk(source):
        for directory in dirs:
            if GAME_DIR_PATTERN in directory.lower():
                path = os.path.join(source, directory)
                game_path.append(path)

        break  
    return game_path

#// Function to remove all some particular word from the file we are going to copy, to destination.
def newPathNameForTargetStripper(paths, to_strip):
    newpath = []
    for xpath in paths:
        _, dir_name = os.path.split(xpath)
        new_dir_name = dir_name.replace(to_strip, "")
        newpath.append(new_dir_name)
    return newpath

#// Function to copy all the file content to another dir, in the recursive mode. If source directory contain subfolders in them, it all get copied to target dir all the subfolder including.
def copy_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

#// Function to strip paths from those path with contain game in them
def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

#// Function to create metadata file.
def create_metadata(path, game_dir):
    data = {
        "GameListName": game_dir,
        "Count": len(game_dir)
    }

    with open(path, 'w') as f:
        json.dump(data, f)

#// Functoin to compile code but for passing the command to subprocess we will create another funtion which will give command to function.
def compile_game_code(code_path):
    code_file_name = None
    for root, dirs, files in os.walk(code_path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break    

    if code_file_name is None:
        return
    
    command_to_run_code = COMMANDS + [code_file_name]
    commandToRun(command_to_run_code, code_path)
    # print(command_to_run_code)

#// Function which will call subprocess to run code from code_file_name
def commandToRun(command, path):
    cwd = os.getcwd()
    os.chdir(path)

    #* Removed the universal_newline, because it was notworking because of that.
    # result = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    result = run(command, stdout=PIPE, stdin=PIPE)
    print("COMPLIED GO CODE -> ", result)
    os.chdir(cwd)


def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    wheregamepresent = allgame_dir_full_path(source_path)
    new_game_dir = newPathNameForTargetStripper(wheregamepresent, "_game")
    # print(newpathName)
    create_dir(target_path)

    for src, dst in zip(wheregamepresent, new_game_dir):
        dest_target = os.path.join(target_path, dst)
        copy_overwrite(src, dest_target)
        compile_game_code(dest_target)

    json_target_path = os.path.join(target_path, "metadata.json")
    create_metadata(json_target_path, new_game_dir)
     
"""
 Source: Dir in which you are going to look for data.
 Target: Where all those data are going to be stored.

 Ex command - python main.py data zulpher
"""  


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception('Please provide, SOURCE && TARGET')
    source, target = args[1:]
    main(source, target)
    