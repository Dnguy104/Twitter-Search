import sys, lucene
import json
from os import path, listdir

from org.apache.lucene.document import Document, Field, StringField, TextField, FieldType
from org.apache.lucene.util import Version
from org.apache.lucene.store import RAMDirectory
from java.nio.file import Paths
from datetime import datetime

from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory


from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser

# INDEXER-----------------------------------------------------

"""
This method returns a document which afterwards can be added to the IndexWriter.
"""
# def create_document(line, file):
    # print line
    # print "time: " + o['created_at']
    # print "\n"
    # return doc

# Initialize lucene and the JVM
def search_files(q):
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    BASE_DIR = path.dirname(path.abspath(sys.argv[0]))
    INPUT_DIR = BASE_DIR + "/input/"
    INDEX_DIR = BASE_DIR + "/lucene_index/"

    print "init"

    NoT = 100000 # Number of Tokens
    # lucene.initVM()

    print "done"

    # directory = RAMDirectory()
    index_path = Paths.get(INDEX_DIR)
    directory = SimpleFSDirectory(index_path)

    analyzer = StandardAnalyzer()
    analyzer = LimitTokenCountAnalyzer(analyzer, NoT)

    # return "Finished Indexing"

    searcher = IndexSearcher(DirectoryReader.open(directory))

    analyzer = StandardAnalyzer()

    print "analyzer"

    # search_loop(searcher, analyzer)

    # return "Finished Searching"


# SEARCH ---------------------------------------------------------------

# def search_loop(searcher, analyzer):
    # while True:
    print "\nEnter a blank line to quit."
    # command = raw_input("Query: ")
    command = q
    # command = "hello"
    if command == '':
        return
    print "Searching for:", command
    query = QueryParser("text", analyzer).parse(command)
    start = datetime.now()
    scoreDocs = searcher.search(query, 10).scoreDocs
    duration = datetime.now() - start
    print "%s total matching documents in %s:" % (len(scoreDocs), duration) + "\n"
    arr = []
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        # print doc['username']
        # print scoreDoc.score
        data = {}
        data['score'] = scoreDoc.score
        data['username'] = doc['username']
        data['text'] = doc['text']
        data['time'] = doc['time']
        print data
        # json_data = json.dumps(data.__dict__)
        arr.append(data)
        print "\n"
    print "\n------------------------------------------------------"
    return arr
# index_files()

def hello():
    print "hi"

if __name__ == '__main__':
    hello()
