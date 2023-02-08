# grep = global regular expression print
Grep is a command-line tool used for searching and filtering text-based data. It is used to quickly search through a file, or multiple files, for simple patterns and basic regular expressions (BREs). Grep can also be used to filter output from other commands, or to search for specific patterns within a file.

Examples:

	Find all occurrences of the pattern ‘patricia’ in a file:

               $ grep 'patricia' myfile

    Same as above but looking only for complete words:

               $ grep -w 'patricia' myfile

    Find all occurrences of the pattern ‘.Pp’ at the beginning of a line:

               $ grep '^\.Pp' myfile

    Find all lines in a file which do not contain the words ‘foo’ or ‘bar’:

               $ grep -v -e 'foo' -e 'bar' myfile
        
        
#  AWK
AWK is a programming language, created by Aho, Weinberger & Kernighan, designed for text processing and typically used as a data extraction and reporting tool. It is a powerful command-line tool that allows users to parse text files and perform operations on the data contained within them. AWK can be used to search for patterns within a file, perform calculations on the data, and print out the results.

Examples:
       
       length($0) > 72
       Print lines longer than 72 characters.
       { print $2, $1 }
       Print first two fields in opposite order.

       BEGIN { FS = ",[ \t]*|[ \t]+" }
             { print $2, $1 }

              Same, with input fields separated by comma and/or spaces and
              tabs.

            { s += $1 }
       END  { print "sum is", s, " average is", s/NR }

              Add up first column, print sum and average.
              /start/, /stop/
              Print all lines between start/stop pairs.

       BEGIN     {    # Simulate echo(1)
            for (i = 1; i < ARGC; i++) printf "%s ", ARGV[i]
            printf "\n"
            exit }
