#!/usr/bin/env bash

echo "Installing space_underscore..."

# Choose command name
echo "Which command name would you prefer?"
echo "1) space_"
echo "2) space_underscore"
read -p "Choose (1/2): " choice

case $choice in
    1) CMD="space_" ;;
    *) CMD="space_underscore" ;;
esac

# Install script
cp space_underscore.py ~/Desktop/Software/scripts/$CMD
chmod +x ~/Desktop/Software/scripts/$CMD

# Create and install man page
mkdir -p /usr/local/share/man/man1/
cat > /usr/local/share/man/man1/$CMD.1 << 'EOL'
.TH SPACE_UNDERSCORE 1
.SH NAME
space_underscore \- A Python utility for batch renaming files with various character transformations
.SH SYNOPSIS
.B space_underscore
action directory [options]
.SH DESCRIPTION
happuneduchan wen I wnned lll du spaces 2 b underscores. den got carried away with features.... hopefully this will have a use...

This script provides actions to modify filenames and directories by applying various transformations 
such as: renaming, deleting characters, replacing characters, and adding characters between or around groups.

It supports previewing changes, applying them, and undoing them using log files.
.SH ACTIONS
.TP
.B preview
Show changes without applying them
    space_underscore preview /path/to/directory --space_
.TP
.B rename
Apply the transformations
    space_underscore rename /path/to/directory --space_
.TP
.B undo
Revert the last rename operation
    space_underscore undo /path/to/directory
.SH OPTIONS
.TP
.B \-\-space_
Replaces spaces with underscores
.TP
.B \-\-space <char>
Replaces spaces with custom character
.TP
.B \-\-delete <char>
Deletes a specific character
.TP
.B \-\-delete_multiples <char1,char2,...>
Deletes multiple characters
.TP
.B \-\-replace_char <old_char>,<new_char>
Replaces one character with another
.TP
.B \-\-add_between <group1>,<group2>,<char>
Adds character between two groups
.TP
.B \-\-add_after <group>,<char>
Adds character after a group
.TP
.B \-\-add_before <group>,<char>
Adds character before a group
.SH LOG FILES
The script maintains logs for all operations:
.TP
.B rename_log.json
Tracks all renamed files
.TP
.B delete_log.json
Tracks deleted characters
.TP
.B replace_log.json
Tracks character replacements
.TP
.B add_log.json
Tracks character additions
.SH EXAMPLES
Replace spaces with underscores:
.PP
    space_underscore rename ./files --space_
.PP
Delete character 'T':
.PP
    space_underscore rename ./files --delete T
.PP
Multiple transformations:
.PP
    space_underscore rename ./files --space_ --delete T
.SH NOTES
- Always use 'preview' first to verify changes
- Undo only works for the most recent operation
- Multiple transformations are applied in order
- Backup important files before bulk renaming
.SH LICENSE
Apache License 2.0
(The copyright holder reserves the right to release future versions under different license terms.)
EOL

echo "Done! Installed as: $CMD"
echo "Try: $CMD preview . --space_"
