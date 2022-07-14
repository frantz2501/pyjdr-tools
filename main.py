# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pyjdr import *
import argparse

def main():
    # Use a breakpoint in the code line below to debug your script.
    parser = argparse.ArgumentParser(description='Random generation & kanka export')
    parser.add_argument('-p', '--path', help='path of data files', required=True)
    parser.add_argument('-k', '--kanka', help='kanka switch (bool)', required=True)
    parser.add_argument('-a', '--asset', help='asset type for kanka upload', required=False)
    parser.add_argument('-i', '--id-campaign', help='id of campaign for kanka upload', required=False)
    args = vars(parser.parse_args())

    myPath = args['path']
    kSwitch = args['kanka']
    kAsset = args['asset']
    kId = args['id_campaign']

    selection = []

    fileList = openFolder(myPath)
    for sfile in fileList:
        choosedItem = randomize(extractData(sfile, myPath))
        selection.append(f"{sfile.split('.')[0]} : {choosedItem}")
        selection.append((sfile, choosedItem))
        print(f"{sfile.split('.')[0]} : {choosedItem}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
