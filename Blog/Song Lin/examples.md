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