import sqlite3
import sys
import argparse

def getHeader(fileName):
    """Extracts the one line header from a file to be used as column names. """
    f = open(fileName,"r")
    header = f.readline().strip()
    cList = header.split(d)
    f.close()
    return cList

def createTable(cList,tableName):
    """ Creates an SQLite table with the given name. """
    cSQL = "CREATE table %s (" % (tableName)
    for column in colList:
        cSQL = cSQL + column + ","
    cSQL = cSQL[:-1] + ")"
    c.execute(cSQL)
    
def loadTable(fileName,tableName):
    print 'called', fileName, tableName
    iSQL = ''
    """ Loads a sqlite table with a given text file bypassing the header. """
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
parser.add_argument('--one', help='Main text file where the SQL command is executed on', required=True)
parser.add_argument('--two', help='Second text file', required=False)
parser.add_argument('--sql', help='SQL statement', required=True)
parser.add_argument('--delimit', help='Column delimiter', required=False, default = "\t")
#parser.add_argument('--saveDB', help='Do you want the SQLite database to be saved on disk?', required=False,action='store_true')
#parser.add_argument('--useDB', help='The file given in --one is a sqlite database.', required = False,action='store_true')
args = vars(parser.parse_args())

print args
#sys.exit()


uSQL = args['sql'].strip()
fName = args['one'].strip()
conn = sqlite3.connect(":memory:")
#conn  = sqlite3.connect("one.db")
c = conn.cursor()


#determining the delimiter

d = args['delimit']
colList = getHeader(fName)
createTable(colList,"one")

loadTable(fName,"one")
conn.commit()


if args['two'] == None:
    #one table operation
    executeSQL(uSQL)
else:
    #need to load the second filefName = args['two'].strip()
    colList = getHeader(fName)
    createTable(colList,"two")
    loadTable(fName,"two")
    conn.commit()
    executeSQL(uSQL)
    
conn.close()


    




