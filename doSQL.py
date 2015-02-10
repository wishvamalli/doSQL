#V2
import sqlite3
import sys
import argparse

#[TODO] enable the scritp to get data sent from pipes
"""
for line in sys.stdin:
    if line == "":
        break
        
        """
        

#[TODO] enable awk like input of columns

def getHeader(fileName,noHead):
    """Extracts the one line header from a file to be used as column names. """
    f = open(fileName,"r")
    header = f.readline().strip()
    cList = header.split(d)
    f.close()
    if noHead == True:
        cList = [x+1 for x in range(len(cList))]
        cList = ["col" + str(x) for x in cList]
    return cList

def createTable(cList,tableName):
    """ Creates an SQLite table with the given name. """
    cSQL = "CREATE table %s (" % (tableName)
    for column in colList:
        cSQL = cSQL + str(column) + ","
    cSQL = cSQL[:-1] + ")"
    print cSQL
    c.execute(cSQL)
    
def loadTable(fileName,tableName):
    """ Loads a sqlite table with a given text file bypassing the header. """

    #[TODO] deal with missing values
    #print 'called', fileName, tableName
    iSQL = ''
    f = open(fileName,"r")
    h = f.readline() #removes the header privided that its one line
    for line in f:
        #print line
        temp = line.strip().split(d)
        iSQL = "INSERT INTO %s VALUES ( " % (tableName)
        for v in temp:
            #if v.isalpha() or v.isalnum():
            iSQL = iSQL + '"' + v + '"' + ","
        """else:
            iSQL = iSQL + v + ","""""
        iSQL = iSQL[:-1] + ")"
    #print "iSQL " , iSQL
        c.execute(iSQL)
    f.close()
    
def executeSQL(sql):
    """ Executes a given sql command. """
    for row in c.execute(sql):
        #print row
        line = ''
        for v in row:
            line  = line+ str(v) +  d
        print line[:-1]

    
parser = argparse.ArgumentParser(description='doSQL allows the execution of SQL statements on text files in the command line.')
parser.add_argument('--one', help='Main text file where the SQL command is executed on')
parser.add_argument('--two', help='Second text file', required=False)
parser.add_argument('--sql', help='SQL statement', required=True)
parser.add_argument('--delimit', help='Column delimiter', required=False, default = "\t")
parser.add_argument('--noHeader', help='The data has no header', required=False,action="store_true",default=False)
parser.add_argument('--colAsNum', help='Identify columns as numbes (col1,col25)', required=False,action="store_true",default=False)
parser.add_argument('--getPipe', help='Recieve data from pipe', required=False,action="store_true",default=False)
#parser.add_argument('--saveDB', help='Do you want the SQLite database to be saved on disk?', required=False,action='store_true')
#parser.add_argument('--useDB', help='The file given in --one is a sqlite database.', required = False,action='store_true')
args = vars(parser.parse_args())

#arg rules
#1. colAsNum should always have noHeader
if args['noHeader'] == True:
    if args['colAsNum'] != True:
        print "Error: --colAsNum must be used with --noHeader"
        sys.exit(1)
        
#2. getPipe should always not have one
if args['getPipe'] == True:
    if args['one']!= None:
        print "Error: --one should not be used when --getPipe is specified"
        sys.exit(1)

print args
#sys.exit()

#if --getPipe is specified get the stdin and save it to a temp file
if args['getPipe'] == True:
    
    pText = ""
    tempFileName  = "tempFile_delete_if_you_see_this.tmp"
    
    for line in sys.stdin:
        pText = pText + line
    f = open(tempFileName,"w")
    f.write(pText)
    f.close()

    

#save args to variables
uSQL = args['sql'].strip()
if args['getPipe']==True:
    fName = tempFileName
else:
    fName = args['one'].strip()
d = args['delimit']

#sqlite stuff
#[[TODO]] I'm not saving the db on disk. Make this user changable
conn = sqlite3.connect(":memory:")
c = conn.cursor()

#get the header or if --noHeader is true simply count the number of cols
colList = getHeader(fName,args['colAsNum'])

#create table
createTable(colList,"one")

#load table
loadTable(fName,"one")
conn.commit()

# deal with the secon file, if specified
if args['two'] == None:
    #one table operation
    executeSQL(uSQL)
else:
    #need to load the second filefName = args['two'].strip()
    colList = getHeader(fName,args['colAsNum'])
    createTable(colList,"two")
    loadTable(fName,"two")
    conn.commit()
    executeSQL(uSQL)
    
conn.close()


    




