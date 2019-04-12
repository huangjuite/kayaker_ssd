#Usage:
<<<<<<< HEAD
#python distribute_data.py -i /home/ray/tensorflow/workspace/kayaker_ssd/images/ -p 0.2
=======
# Create train data:
#python xml_to_csv.py -i [PATH_TO_IMAGES_FOLDER]/train -o [PATH_TO_ANNOTATIONS_FOLDER]/train_labels.csv

# Create test data:
#python xml_to_csv.py -i [PATH_TO_IMAGES_FOLDER]/test -o [PATH_TO_ANNOTATIONS_FOLDER]/test_labels.csv
>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703

import os
import glob
import argparse
import re
from shutil import copyfile,move
<<<<<<< HEAD
import xml.etree.ElementTree as ET
import panda as pd
=======

>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703


def main():
    # Initiate argument parser
    parser = argparse.ArgumentParser(
        description="distribute training and testing data")
    parser.add_argument("-i",
                        "--inputDir",
                        help="Path to the folder where the input .xml files are stored",
                        type=str)
    parser.add_argument("-p",
                        "--percentage",
                        help="testing/training",
                        type=str)
    args = parser.parse_args()

    if(args.inputDir is None):
        return

    if(args.percentage is None):
        args.percentage = 0.2
<<<<<<< HEAD
    
    assert(os.path.isdir(args.inputDir))
    #-----------------------------------------------------------
    #-----------------------------------------------------------
=======

    
    assert(os.path.isdir(args.inputDir))

>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703
    files = glob.glob(args.inputDir + 'annotation/*.xml')
    train_xmls = []
    test_xmls = []
    for i,xml_file in enumerate(files):
        if i<len(files)*args.percentage:
            test_xmls.append(xml_file)
        else:
            train_xmls.append(xml_file)
<<<<<<< HEAD
    #-----------------------------------------------------------
    #-----------------------------------------------------------
=======

>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703
    try:
        os.mkdir(args.inputDir+'test')
    except:
        print 'test folder already esxist'
    for xml_file in test_xmls:
        num = re.findall(r'\d+',xml_file)[-1]
        jpg_file = args.inputDir + 'image/frame'+num+'.jpg'

        move(xml_file,args.inputDir + 'test/frame'+num+'.xml')
        move(jpg_file,args.inputDir + 'test/frame'+num+'.jpg')
<<<<<<< HEAD
    #-----------------------------------------------------------
    #-----------------------------------------------------------
=======

>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703
    try:
        os.mkdir(args.inputDir+'train')
    except:
        print 'train folder already esxist'
    for xml_file in train_xmls:
        num = re.findall(r'\d+',xml_file)[-1]
        jpg_file = args.inputDir + 'image/frame'+num+'.jpg'

        move(xml_file,args.inputDir + 'train/frame'+num+'.xml')
        move(jpg_file,args.inputDir + 'train/frame'+num+'.jpg')
<<<<<<< HEAD

    print('Successfully transfer %d labeled sets'%len(files))
    #-----------------------------------------------------------
    #-----------------------------------------------------------
    files = glob.glob(args.inputDir + 'image/*.jpg')
    print('%d images has no label'%len(files))
    for file in files:
        num = re.findall(r'\d+',file)[-1]
        move(file,args.inputDir + 'train/frame'+num+'.jpg')
=======
        
    files = glob.glob(args.inputDir + 'annotation/*.xml')

    print('Successfully transfer %d xml files'%len(files))

>>>>>>> 74cdf08bdb9cb8362343f3e20741b03a53428703

if __name__ == '__main__':
    main()