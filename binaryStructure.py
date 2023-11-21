import sys

from json import JSONDecoder
from collections import OrderedDict

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class StructureLoader:
    content = []
    structure = {}
    index = 0

    def __init__ (self, binFilePath, structureFilePath):
        customdecoder = JSONDecoder(object_pairs_hook=OrderedDict)
        with open (binFilePath, "r") as f:
            self.content = f.read ().replace ("\n", "").split (" ")

        with open (structureFilePath, "r") as f:
            self.structure = customdecoder.decode (f.read ())
        
        self.index = 0

    def findLength (self, node, value, arrIndex = 0):
        if (type (value) == OrderedDict):
            for subnode, subvalue in value.items ():
                node_buff = "{}.{}".format (node, subnode)
                self.findLength (node_buff, subvalue)
        elif (type (value) == list):
            for element in value:
                node_buff = "{}.{}".format (node, arrIndex)
                self.findLength (node_buff, element, arrIndex)
                arrIndex += 1
        else:
            print (
                "{:>6} | ".format (self.index) + 
                bcolors.UNDERLINE + "{:<50}".format (node) + bcolors.ENDC +
                "| " +
                bcolors.WARNING +
                "{}".format (" ".join (self.content[self.index:self.index + value])) +
                bcolors.ENDC
            )
            self.index += value

    def parseBin (self):
        print (
            "offset | " + 
            bcolors.BOLD + bcolors.OKBLUE +
            "node" + bcolors.ENDC + " " * 46 +
            "| " + bcolors.BOLD + bcolors.WARNING +
            "value" + bcolors.ENDC
        )
        for node, value in self.structure.items ():
            self.findLength (node, value)

        print ("-" * 50)
        print ("Total Bytes - {}".format (self.index))

if __name__ == "__main__":
    readInput = ""
    if (sys.version_info[0] == 2):
        readInput = raw_input
    elif (sys.version_info[0] == 3):
        readInput = input
    else:
        print ("Weird version", sys.version)
        sys.exit (1)

    binFile = readInput ("Enter bin file path: ")
    structureFile = readInput ("Enter structure file path: ")
    loader = StructureLoader(binFile, structureFile)
    loader.parseBin ()