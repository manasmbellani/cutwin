#!/usr/bin/python

import sys
import argparse

DESCRIPTION = """Minimalist cut for Windows, currently following options
are implemented:

    -d              delimiter
    -f              field number to get

Example:
    * Prepare input
        echo "how? are you? going" >>test.txt
        
    * Pipe the contents of the text file to the file to execute:
        type test.txt | cut.exe -d"?" f2
"""

def parse_user_args():
    parser = argparse.ArgumentParser(description=DESCRIPTION,
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-d", "--delimiter", dest="delimiter", required=True,
                        action="store", help="delimiter")
    parser.add_argument("-f","--fieldnum", dest="fieldnum", required=True,
                        action="store", help="field number")
    args = parser.parse_args()
    delimiter = args.delimiter
    fieldnum  = args.fieldnum
    return (delimiter, fieldnum)

if __name__ == "__main__":
    
    # Parser user-provided arguments
    delimiter, fieldnum = parse_user_args()

    # Take user input via pipe, or directly from stdin
    piped_input = sys.stdin.read().rstrip()
    
    # Convert fieldnum to number
    try:
        if int(fieldnum):
            fieldnum = int(fieldnum)
            if fieldnum < 1:
                raise ValueError
    except ValueError:
        print "[-] Field number {} is invalid".format(fieldnum)
        sys.exit(1)

    # Get the relevant field
    for line in piped_input.split("\n"):
        line_stripped = line.rstrip()
        if line_stripped:
            field_values = line_stripped.split(delimiter)
            if len(field_values) < fieldnum:
                print ""
            else:
                print field_values[fieldnum-1]

