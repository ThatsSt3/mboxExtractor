import argparse
import os
from bin.fileManager import Extractor


def main():
    parser = argparse.ArgumentParser(prog="MBOX file content extractor", description="Extracts text and attachments from emails in MBOX file")
    parser.add_argument('MBOXinputFilename', help="MBOX input file")
    parser.add_argument('-v', '--verbose', help="Verbose output", action='store_true')
    
    args = parser.parse_args()
    
    try:
        path = os.path.abspath(args['MBOXinputFilename'])
    except:
        print('MBOX file not found')
    
    e = Extractor(path)



if __name__ == '__main__':
    main()