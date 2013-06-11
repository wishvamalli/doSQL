doSQL.py (c) 2013 Wishva Herath
Version = 0.1

This python script allows you to execute SQL statements on text files. 

doSQL usage
-----------
usage: doSQL.py [-h] --one ONE [--two TWO] --sql SQL [--delimit DELIMIT]

doSQL allows the execution of SQL statements on text files in the command
line.

optional arguments:
  -h, --help         show this help message and exit
  --one ONE          Main text file where the SQL command is executed on
  --two TWO          Second text file
  --sql SQL          SQL statement
  --delimit DELIMIT  Column delimiter


doSQL features
-------------
Can do any SQL statement (SELECT, JOIN, GROUP BY, ORDER etc.)
Can combine commands by piping
Can take in different delimiters
(Relatively) fast

how does doSQL work
-------------------
1. read  one (or two) text files.
2. figure out their column names
3. add them as seperate tables on an SQLite db
4. execute the SQL
5. print the results


