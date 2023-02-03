# Credits :- https://youtu.be/R2bhO0kZZnQ?list=PL7yh-TELLS1F3KytMVZRFO-xIo_S2_Jg1

# Basic XML Processing can be done using SAX and DOM
# SAX is a simple API for XML
# DOM is a Document Object Model

# SAX is an event based parser
# It is a pull parser
# It is a non-validating parser
# It is a fast parser
# It is a memory efficient parser
# It is a stream parser
# It is a line by line parser

# DOM is a tree based parser
# It is a push parser
# It is a validating parser
# It is a slow parser
# It is a memory inefficient parser
# It is a non-stream parser
# It is a whole document parser

# XML Parsing using SAX

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content