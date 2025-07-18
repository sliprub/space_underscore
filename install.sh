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
