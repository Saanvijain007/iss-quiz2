#assuming that the file is in the same directory as the script and filename exists
# code to prompt the user to enter a filename and then count the number of lines in that file.
#!/bin/bash

echo -n "Enter filename: "
read filename

lines=$(wc -l < "$filename")
echo "Line count: $lines"
