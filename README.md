4pics-1word-solver
==================

Simple Python script to help you solve the 4pics 1 word game. 

You provide it two arguments - (1) charSet - the jumbled characters (2) number of letters in the final word. 

The program would find all (2)-letter permutations of (1) and output those which are valid words according to the system dictionary at - /usr/share/dict/web2. 

If you don't provide the second  argument, then it assumes the number of letters in the final word same as that of the charSet and converts it into a Jumbled Word Problem and solves it for you.
