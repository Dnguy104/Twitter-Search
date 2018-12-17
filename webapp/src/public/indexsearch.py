# import sys, lucene
# import json
# from os import path, listdir
#
# from org.apache.lucene.document import Document, Field, StringField, TextField, FieldType
# from org.apache.lucene.util import Version
# from org.apache.lucene.store import RAMDirectory
# from java.nio.file import Paths
# from datetime import datetime
#
# from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
# from org.apache.lucene.analysis.standard import StandardAnalyzer
# from org.apache.lucene.index import IndexWriter, IndexWriterConfig
# # from org.apache.lucene.store import SimpleFSDirectory
#
#
# from org.apache.lucene.search import IndexSearcher
# from org.apache.lucene.index import DirectoryReader
# from org.apache.lucene.queryparser.classic import QueryParser
#
# # INDEXER-----------------------------------------------------
#
# """
# This method returns a document which afterwards can be added to the IndexWriter.
# """
# # def create_document(line, file):
#     # print line
#     # print "time: " + o['created_at']
#     # print "\n"
#     # return doc
#
# # Initialize lucene and the JVM
# def index_files(q):
#     BASE_DIR = path.dirname(path.abspath(sys.argv[0]))
#     INPUT_DIR = BASE_DIR + "/input/"
#     INDEX_DIR = BASE_DIR + "/lucene_index/"
#
#     NoT = 100000 # Number of Tokens
#     print "------------------------------------------------------"
#     print "PyLucene Demo started (lucene_demo.py)"
#     print "Python version: %d.%d.%d" % (sys.version_info.major,
#                                           sys.version_info.minor,
#                                           sys.version_info.micro)
#     print 'Lucene version:', lucene.VERSION
#     print "------------------------------------------------------\n"
#     lucene.initVM()
#
#     # index_path = Paths.get(INDEX_DIR)
#     directory = RAMDirectory()
#
#     analyzer = StandardAnalyzer()
#     analyzer = LimitTokenCountAnalyzer(analyzer, NoT)
#     config = IndexWriterConfig(analyzer)
#     writer = IndexWriter(directory, config)
#
#     print "Number of indexed documents: %d\n" % writer.numDocs()
#     for input_file in listdir(INPUT_DIR): # iterate over all input files
#         print "Current file:", input_file
#         if input_file.endswith(".json"):
#             with open(INPUT_DIR+input_file) as f:
#                 for line in f:
#                     # doc = create_document(line, input_file) # call the create_document function
#                     o = json.loads(line)
#                     doc = Document() # create a new document
#                     doc.add(TextField("filename", input_file, Field.Store.YES))
#                     # print file
#                     doc.add(TextField("username", o['user']['screen_name'], Field.Store.YES))
#                     # print "username: " + o['user']['screen_name']
#                     doc.add(TextField("text", o['text'], Field.Store.YES))
#                     # print "text: " + o['text']
#                     if o['user']['location']:
#                         doc.add(TextField("location", o['user']['location'], Field.Store.YES))
#                         # print "location: " + o['user']['location']
#                     doc.add(TextField("time", o['created_at'], Field.Store.YES))
#                     writer.addDocument(doc) # add the document to the IndexWriter
#     print "\nNumber of indexed documents: %d" % writer.numDocs()
#     writer.close()
#     print "Finished\n"
#     print "-----------------------------------------------------"
#     # return "Finished Indexing"
#
#     searcher = IndexSearcher(DirectoryReader.open(directory))
#
#     analyzer = StandardAnalyzer()
#
#     # search_loop(searcher, analyzer)
#
#     # return "Finished Searching"
#
#
# # SEARCH ---------------------------------------------------------------
#
# # def search_loop(searcher, analyzer):
#     # while True:
#     print "\nEnter a blank line to quit."
#     # command = raw_input("Query: ")
#     command = q
#     # command = "hello"
#     if command == '':
#         return
#     print "Searching for:", command
#     query = QueryParser("text", analyzer).parse(command)
#     start = datetime.now()
#     scoreDocs = searcher.search(query, 50).scoreDocs
#     duration = datetime.now() - start
#     print "%s total matching documents in %s:" % (len(scoreDocs), duration) + "\n"
#     arr = []
#     for scoreDoc in scoreDocs:
#         doc = searcher.doc(scoreDoc.doc)
#         # print doc['username']
#         # print scoreDoc.score
#         data = {}
#         data['score'] = scoreDoc.score
#         data['username'] = doc['username']
#         data['text'] = doc['text']
#         data['time'] = doc['time']
#         print data
#         # json_data = json.dumps(data.__dict__)
#         arr.append(data)
#         print "\n"
#     print "\n------------------------------------------------------"
#     return arr
# # index_files()
#
# def hello():
#     print "hi"
#
# if __name__ == '__main__':
#     hello()
