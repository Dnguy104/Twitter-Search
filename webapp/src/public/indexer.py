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
def index_files():
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    BASE_DIR = path.dirname(path.abspath(sys.argv[0]))
    INPUT_DIR = BASE_DIR + "/input/"
    INDEX_DIR = BASE_DIR + "/lucene_index/"

    NoT = 100000 # Number of Tokens
    print "------------------------------------------------------"
    print "PyLucene Demo started (lucene_demo.py)"
    print "Python version: %d.%d.%d" % (sys.version_info.major,
                                          sys.version_info.minor,
                                          sys.version_info.micro)
    print 'Lucene version:', lucene.VERSION
    print "------------------------------------------------------\n"
    # lucene.initVM()

    # directory = RAMDirectory()
    index_path = Paths.get(INDEX_DIR)
    directory = SimpleFSDirectory(index_path)

    analyzer = StandardAnalyzer()
    analyzer = LimitTokenCountAnalyzer(analyzer, NoT)
    config = IndexWriterConfig(analyzer)
    writer = IndexWriter(directory, config)

    print "Number of indexed documents: %d\n" % writer.numDocs()
    for input_file in listdir(INPUT_DIR): # iterate over all input files
        print "Current file:", input_file
        if input_file.endswith(".json"):
            with open(INPUT_DIR+input_file) as f:
                for line in f:
                    # doc = create_document(line, input_file) # call the create_document function
                    o = json.loads(line)
                    doc = Document() # create a new document
                    doc.add(TextField("filename", input_file, Field.Store.YES))
                    # print file
                    doc.add(TextField("username", o['user']['screen_name'], Field.Store.YES))
                    # print "username: " + o['user']['screen_name']
                    doc.add(TextField("text", o['text'], Field.Store.YES))
                    # print "text: " + o['text']
                    if o['user']['location']:
                        doc.add(TextField("location", o['user']['location'], Field.Store.YES))
                        # print "location: " + o['user']['location']
                    doc.add(TextField("time", o['created_at'], Field.Store.YES))
                    writer.addDocument(doc) # add the document to the IndexWriter
    print "\nNumber of indexed documents: %d" % writer.numDocs()
    writer.close()
    print "Finished\n"
    print "-----------------------------------------------------"
    # return "Finished Indexing"

#
# index_files()

def hello():
    print "hi"

if __name__ == '__main__':
    hello()
