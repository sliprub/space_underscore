"""
        ___________
space_underscore.py
        ___________
_ _ _ _ _ _
DESCRIPTION: A Python utility for batch renaming files with various character transformations.

    This Python script provides actions to modify filenames and directories by applying various transformations 
    such as:    renaming, 
                deleting characters, 
                replacing characters, 
    and         adding characters between or around groups. 

        It supports previewing changes, applying them, and undoing them using log files. Transformations are applied to 
        filenames and directories based on the provided arguments, and changes can be previewed before being executed.
        
        The script uses log files to track changes, enabling an undo action that reverts the last renaming operation.

_ _ _ _ _ 
HAPPUNEDU: 

happuneduchan wen I wnned lll du spaces 2 b underscores. den got carried away with features.... hopefully this will have a use...

_ _ _ _
SETUP:

    1: Open Terminal in the folder containing space_underscore.py.
    2: Provide Arguments to the Script: The script expects two required arguments:

    action: The operation you want to perform (either preview, rename, or undo).
    directory: The path to the directory where changes will be applied.

        The script expects two required arguments: action and directory.
        These must be provided when you run it.

Basic syntax for running the script:

            python3 space_underscore.py <action> <directory> [<transformation_arguments>]

Example:
    python3 space_underscore.py rename ./my_files --space_

Core Actions
-----------
preview : Show changes without applying them
    python3 space_underscore.py preview /path/to/directory --space_

rename  : Apply the transformations
    python3 space_underscore.py rename /path/to/directory --space_

undo    : Revert the last rename operation
    python3 space_underscore.py undo /path/to/directory

Available Transformations
-----------------------
--space_                             : Replaces spaces with underscores
--space <char>                       : Replaces spaces with custom character
--delete <char>                      : Deletes a specific character
--delete_multiples <char1,char2,...> : Deletes multiple characters
--replace_char <old_char>,<new_char> : Replaces one character with another
--add_between <group1>,<group2>,<char>: Adds character between two groups
--add_after <group>,<char>          : Adds character after a group
--add_before <group>,<char>         : Adds character before a group

Examples
--------
Replace spaces with underscores:
    python3 space_underscore.py rename ./files --space_

Delete character 'T':
    python3 space_underscore.py rename ./files --delete T

Multiple transformations:
    python3 space_underscore.py rename ./files --space_ --delete T

Log Files
---------
The script maintains logs for all operations:
- rename_log.json: Tracks all renamed files
- delete_log.json: Tracks deleted characters
- replace_log.json: Tracks character replacements
- add_log.json: Tracks character additions

Troubleshooting
--------------
1. Permission Issues:
   - Ensure you have write permissions in the target directory
   - Run with sudo if needed (careful!)

2. Log File Issues:
   - Check if log files exist and are writable
   - Clear log files if they become corrupted

3. Common Errors:
   - Invalid characters in paths
   - Missing permissions
   - File already exists

Notes
-----
- Always use 'preview' first to verify changes
- Undo only works for the most recent operation
- Multiple transformations are applied in order
- Backup important files before bulk renaming
"""


import os
import argparse
import json

# Define the log file for tracking changes
LOG_FILE = 'rename_log.json'

# Function to print the logo at the end
def print_logo():
    """Prints a logo for the script."""
    logo = r"""
|                                    _______________________________  |
|                                         /      ○      __________    |
|  ABCD   EFGH   IJKLM  NOPQR   STUVW          ⬭      ⨀_________     
| X       Y   Z  1   2  3       4         ∅‌            underscore     |
|  567    89!@   #$%^&  *       ()_+        ◌      ◯                  |
|     ,   .      /   <  >       ?      ⦿       ␀          ⚬      ␀     
| |}{\    ]      [   "  :';-=   SPACE      ␣         ⊗                   
|                                                            ␀           
| U   U  N   N  DDDD   EEEEE  RURR    SLIP  RUBXX  GOO  ©copy  ™ronged
| U   M  AK  I  S   P  P      P  ⨀   S      C     R  O  T   U  M      
| U   U  2 ○ ◯  C   D  EGRR   RUFF    SSS ‌‌ ‌‌ ‌‌C     O   O  RRRR  EEEE   |
| Ū   N  U  BS  U   A  E      R  R       S  C     G   O  A  R  F      |
| UUUUU  N   N  MDUM   PEEEE  R   R  SLUT   COCKX  GOO   P   E ENiSx  |
|---------------------------------------------------------------------|
"""
    print(logo)
    print("SPACE_UNDERSCORE ( _)\n")

# Function to preview transformations on filenames
def preview_files(directory, transformations):
    print(f"Preview of transformations in directory: {directory}")
    for filename in os.listdir(directory):
        new_name = apply_transformations(filename, transformations)
        print(f"Old name: {filename} -> New name: {new_name}")

# Function to rename files based on the transformations
def rename_files(directory, transformations):
    print(f"Renaming files in directory: {directory}")
    changes = []  # List to store changes

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        new_name = filename  # Start with the original filename

        # Apply transformations to each filename
        new_name = apply_transformations(new_name, transformations)
        
        # If the new name is different from the old name, rename the file
        if filename != new_name:  # Only rename if names are different
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            
            try:
                os.rename(old_path, new_path)  # Rename the file
                changes.append({'old': filename, 'new': new_name})  # Store the change
                print(f"Renamed: Old name: {filename} -> New name: {new_name}")
            except Exception as e:
                print(f"Error renaming {filename} to {new_name}: {e}")

    # After renaming, log the changes (if any)
    if changes:
        log_changes(changes)

# Function to apply transformations to a filename
def apply_transformations(filename, transformations):
    """Apply all transformations to the filename."""
    new_name = filename
    for transformation in transformations:
        print(f"Applying transformation: {transformation}")  # Debugging line
        
        # Handle each transformation separately
        if transformation.startswith('--space '):
            char = transformation.split(' ')[1]
            new_name = new_name.replace(' ', char)
        
        elif transformation.startswith('--replace_char '):
            try:
                old_char, new_char = transformation.split(' ')[1].split(',')
                if len(old_char) != 1 or len(new_char) != 1:
                    print(f"Warning: Invalid characters in --replace_char {transformation}")
                    continue
                new_name = new_name.replace(old_char, new_char)
            except ValueError:
                print(f"Error: Invalid format for --replace_char. Expected 'old,new' but got {transformation}")
        
        elif transformation.startswith('--delete '):
            char = transformation.split(' ')[1]
            new_name = new_name.replace(char, '')
        
        elif transformation.startswith('--delete_multiples '):
            chars = transformation.split(' ')[1].split(',')
            for char in chars:
                new_name = new_name.replace(char, '')
        
        elif transformation.startswith('--add_between '):
            try:
                print(f"Raw input: '{transformation}'")
                args = transformation[len('--add_between '):]
                print(f"Args: '{args}'")
                
                parts = [p for p in args.split(',')]
                print(f"Parts: {[repr(p) for p in parts]}")
                
                if len(parts) == 3:
                    group1, group2, char = parts
                    group1 = group1.strip("'")
                    group2 = group2.strip("'")
                    char = char.strip().strip("'")
                    
                    print(f"group1='{group1}' ({len(group1)} chars)")
                    print(f"group2='{group2}' ({len(group2)} chars)")
                    print(f"char='{char}' ({len(char)} chars)")
                    
                    if group1 == " " and group2 == " ":
                        print("Space case!")
                        # Replace only exact occurrences of two spaces
                        new_name = new_name.replace("  ", f" {char} ")
                    else:
                        print("General case!")
                        # Ensure we are not inadvertently adding characters between every character
                        new_name = new_name.replace(group1 + group2, group1 + char + group2)
                else:
                    print(f"Error: Expected 3 parts, got {len(parts)}")
            except Exception as e:
                print(f"Error: {e}")
        
        elif transformation.startswith('--add_after '):
            parts = transformation.split(' ')[1].split(',')
            group, char = parts
            new_name = new_name.replace(group, group + char)
        
        elif transformation.startswith('--add_before '):
            parts = transformation.split(' ')[1].split(',')
            group, char = parts
            new_name = new_name.replace(group, char + group)
        
        elif transformation.startswith('--reduce_duplicates '):
            try:
                # Parse the transformation string
                char, instances_str = transformation.split(' ')[1].split(',')
                instances = instances_str.split('-')
                instances = [int(i) for i in instances if i.isdigit()]
                apply_to_all = 'all' in instances_str

                # Logic to reduce duplicates
                count = 0
                new_name_list = list(new_name)
                
                for i in range(len(new_name_list) - 1):
                    if new_name_list[i] == char and new_name_list[i + 1] == char:
                        count += 1
                        if apply_to_all or count in instances:
                            new_name_list[i + 1] = ''  # Remove the duplicate
                new_name = ''.join(new_name_list)
            except ValueError:
                print(f"Error: Invalid format for --reduce_duplicates. Expected 'char,instances' but got {transformation}")

    return new_name

# Function to log changes (used after renaming files)
def log_changes(changes):
    """ Log the changes to a file """
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w') as log_file:
            json.dump(changes, log_file, indent=4)
    else:
        with open(LOG_FILE, 'r+') as log_file:
            existing_changes = json.load(log_file)
            existing_changes.extend(changes)  # Append the new changes
            log_file.seek(0)
            json.dump(existing_changes, log_file, indent=4)

# Function to undo last operation using log data
def undo_last_operation(directory):
    print(f"Attempting to undo changes in directory: {directory}")

    # Check if log file exists
    if not os.path.exists(LOG_FILE):
        print("No log file found. Nothing to undo.")
        return
    
    with open(LOG_FILE, 'r') as log_file:
        changes = json.load(log_file)
    
    if not changes:
        print("No changes to undo.")
        return

    # Reverse the changes
    for change in reversed(changes):
        old_name = change['new']
        new_name = change['old']
        
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        
        try:
            os.rename(old_path, new_path)  # Rename the file back to its original name
            print(f"Undone: {old_name} -> {new_name}")
        except Exception as e:
            print(f"Error undoing {old_name} to {new_name}: {e}")

    # Clear the log file after undoing
    with open(LOG_FILE, 'w') as log_file:
        json.dump([], log_file, indent=4)  # Empty the log

# Main function to handle the argument parsing and actions
def main():
    parser = argparse.ArgumentParser(description="File renaming utility.")
    parser.add_argument("action", choices=['preview', 'rename', 'undo'], help="Action to perform.")
    parser.add_argument("directory", help="Directory to perform the action in.")
    
    # Optional arguments for transformations
    parser.add_argument("--replace_char", type=str, nargs='?', help="Replace a character in filenames (format: old,new)")
    parser.add_argument("--space", type=str, nargs='?', help="Replace spaces with a given character")
    parser.add_argument("--delete", type=str, nargs='?', help="Delete a specified character from filenames")
    parser.add_argument("--delete_multiples", type=str, nargs='?', help="Delete multiple characters from filenames (comma-separated)")
    parser.add_argument("--add_between", type=str, nargs='?', help="Add a character between two groups in filenames")
    parser.add_argument("--add_after", type=str, nargs='?', help="Add a character after a group in filenames")
    parser.add_argument("--add_before", type=str, nargs='?', help="Add a character before a group in filenames")

    args = parser.parse_args()

    # Perform action based on user input
    if not os.path.isdir(args.directory):
        print(f"Error: The directory '{args.directory}' does not exist or is not accessible.")
        return

    # Parse transformation arguments into a list
    transformations = []
    if args.replace_char:
        transformations.append(f"--replace_char {args.replace_char}")
    if args.space:
        transformations.append(f"--space {args.space}")
    if args.delete:
        transformations.append(f"--delete {args.delete}")
    if args.delete_multiples:
        transformations.append(f"--delete_multiples {args.delete_multiples}")
    if args.add_between:
        transformations.append(f"--add_between {args.add_between}")
    if args.add_after:
        transformations.append(f"--add_after {args.add_after}")
    if args.add_before:
        transformations.append(f"--add_before {args.add_before}")

    # Perform the requested action
    if args.action == 'preview':
        preview_files(args.directory, transformations)
    elif args.action == 'rename':
        rename_files(args.directory, transformations)
    elif args.action == 'undo':
        undo_last_operation(args.directory)

if __name__ == "__main__":
    print_logo()  # Print the logo at the beginning
    main()

