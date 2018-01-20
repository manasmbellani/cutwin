# cutwin
Minimalist cut for Windows, currently following options
are implemented:

    -d              delimiter
    -f              field number to get

## Example:

    * Prepare input
        echo "how? are you? going" >>test.txt
        
    * Pipe the contents of the text file to the file to execute:
        type test.txt | cut.exe -d"?" f2

## Optional Arguments:

  -h, --help            show this help message and exit
  -d DELIMITER, --delimiter DELIMITER
                        delimiter
  -f FIELDNUM, --fieldnum FIELDNUM
                        field number

