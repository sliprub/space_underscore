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
