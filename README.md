# space_underscore

happuneduchan wen I wnned lll du spaces 2 b underscores.... got carried away with features....

## What It Does

Takes spaces and other characters in filenames and does stuff to them:
- Replaces spaces with underscores (or any char)
- Deletes characters you don't want
- Adds stuff between things
- Can preview before it happens
- Can undo if you mess up

## How To Use It

```bash
# Basic: spaces to underscores
python3 space_underscore.py rename ./my_files --space_

# Preview what will happen
python3 space_underscore.py preview ./my_files --space_

# Undo last rename
python3 space_underscore.py undo ./my_files
```

## Cool Stuff You Can Do

```bash
# Replace spaces with whatever
--space <char>

# Delete characters
--delete <char>
--delete_multiples a,b,c

# Replace stuff
--replace_char old,new

# Add between/around
--add_between group1,group2,char
--add_after group,char
--add_before group,char
```

## Safety First
- Always `preview` before `rename`
- Can `undo` the last thing
- Keeps logs of what it did

## Requirements
- Python 3
- That's it

## License
Apache License 2.0

_Note: The copyright holder reserves the right to release future versions under different license terms._

---
_originated as space to underscore converter.... now it does way more_
