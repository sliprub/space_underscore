```
                                     _______________________________
|                                         /      ○      __________  
|  ABCD   EFGH   IJKLM  NOPQR   STUVW          ⬭      ⨀_________
| X       Y   Z  1   2  3       4         ∅           underscore    
|  567    89!@   #$%^&  *       ()_+        ◌      ◯                  
|     ,   .      /   <  >       ?      ⦿       ␀          ⚬      ␀     
| |}{\    ]      [   "  :';-=   SPACE      ␣         ⊗   ©copy_™ronged              
                                                            ␀           

SPACE_UNDERSCORE ( _)
```

# space_underscore

**DESCRIPTION:** A Python utility for batch renaming files with various character transformations.

This Python script provides actions to modify filenames and directories by applying various transformations such as:
- renaming
- deleting characters
- replacing characters
- adding characters between or around groups

It supports previewing changes, applying them, and undoing them using log files. Transformations are applied to filenames and directories based on the provided arguments, and changes can be previewed before being executed.

The script uses log files to track changes, enabling an undo action that reverts the last renaming operation.

## Why?

I wanted all spaces to be underscores...

## SETUP

1. Open Terminal in the folder containing space_underscore.py.
2. Provide Arguments to the Script: The script expects two required arguments:
   - **action**: The operation you want to perform (either preview, rename, or undo).
   - **directory**: The path to the directory where changes will be applied.

Basic syntax for running the script:
```bash
python3 space_underscore.py <action> <directory> [<transformation_arguments>]
```

Example:
```bash
python3 space_underscore.py rename ./my_files --space_
```

With alias (after installation):
```bash
space_ rename ./my_files --space_
# or
space_underscore rename ./my_files --space_
```

## Core Actions

**preview** : Show changes without applying them
```bash
python3 space_underscore.py preview /path/to/directory --space_
```

**rename** : Apply the transformations
```bash
python3 space_underscore.py rename /path/to/directory --space_
```

**undo** : Revert the last rename operation
```bash
python3 space_underscore.py undo /path/to/directory
```

## Available Transformations

- `--space_` : Replaces spaces with underscores
- `--space <char>` : Replaces spaces with custom character
- `--delete <char>` : Deletes a specific character
- `--delete_multiples <char1,char2,...>` : Deletes multiple characters
- `--replace_char <old_char>,<new_char>` : Replaces one character with another
- `--add_between <group1>,<group2>,<char>`: Adds character between two groups
- `--add_after <group>,<char>` : Adds character after a group
- `--add_before <group>,<char>` : Adds character before a group

## Examples

Replace spaces with underscores:
```bash
python3 space_underscore.py rename ./files --space_
```

Delete character 'T':
```bash
python3 space_underscore.py rename ./files --delete T
```

Multiple transformations:
```bash
python3 space_underscore.py rename ./files --space_ --delete T
```

## Log Files

The script maintains logs for all operations:
- rename_log.json: Tracks all renamed files
- delete_log.json: Tracks deleted characters
- replace_log.json: Tracks character replacements
- add_log.json: Tracks character additions

## Troubleshooting

1. **Permission Issues:**
   - Ensure you have write permissions in the target directory
   - Run with sudo if needed (careful!)

2. **Log File Issues:**
   - Check if log files exist and are writable
   - Clear log files if they become corrupted

3. **Common Errors:**
   - Invalid characters in paths
   - Missing permissions
   - File already exists

## Notes

- Always use 'preview' first to verify changes
- Undo only works for the most recent operation
- Multiple transformations are applied in order
- Backup important files before bulk renaming

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.
