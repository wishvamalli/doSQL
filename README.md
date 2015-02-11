#doSQL  - Run SQL commands on tabular text files

###Revisions
Version = 0.2
doSQL can now read from a pipe and understand either column names or col numbers (col24) in SQL statements


##Description
---

Have a text file and need to perform column based filtering and manupilations? Love SQL but do not want to go through the hassle of uploading the file to an SQL database? Then doSQL is for you!!!

doSQL allows the execution of SQL statements on text files in the command
line. With doSQL you just need to have python to use SQL on text files.

##Usage (revised)
---
~~~
usage: doSQL.py [-h] [--one ONE] [--two TWO] --sql SQL [--delimit DELIMIT]
                [--noHeader] [--colAsNum] [--getPipe]
~~~


~~~
optional arguments:
  -h, --help         show this help message and exit
  --one ONE          Main text file where the SQL command is executed on
  --two TWO          Second text file
  --sql SQL          SQL statement
  --delimit DELIMIT  Column delimiter
  --noHeader         The data has no header
  --colAsNum         Identify columns as numbes (col1,col25)
  --getPipe          Recieve data from pipe
 
~~~





##Features
---
* Supports all standard SQL commands.
* Commands can be chained through pipes.
* Can process files with any delimiter


How does doSQL work
---

Python come with sqlite built in. What doSQL does is simply take the input text file(s) and create a sqlite database on the fly. Then your sql commands are run agains the database. (Yes its quite simple!)



1. read  one (or two) text files.
2. figure out their column names
3. add them as seperate tables on an SQLite db
4. execute the SQL
5. print the results

## Auto-generated Documentation
You can find the auto-generated document [here](https://dl.dropboxusercontent.com/u/3432985/web/doSQL/html/index.html).

## Download / Links
Find the project on [GITHUB](https://github.com/wishvamalli/doSQL) [https://github.com/wishvamalli/doSQL].

doSQL was a weekend project by [Wishva Herath](https://au.linkedin.com/in/wishva) 



 
 





