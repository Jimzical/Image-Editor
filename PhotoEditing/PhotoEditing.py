# from DeleteFunctions import deleteFile, deleteFolder  #Import Error
from BasicImageFunctions import *
from DeleteFunctions import *
from ImageFilters import *
from ImageEditing import *
import sys
def main():
#  making command line arguments


    # make a swtich case for the user to choose what he wants to do
    option = sys.argv[0]
    if (option == '-o' or '--open'):
        imgPath = sys.argv[1]
    elif (option == '-s' or '--save'):
        imgPath = sys.argv[1]
        savePath = sys.argv[2]
        SaveImg(imgPath,savePath)
    elif (option == '-d' or '--delete'):
        imgPath = sys.argv[1]
        deleteImg(imgPath)
    elif (option == '-r' or '--remove'):
        folderPath = sys.argv[1]
        deleteFolder(folderPath)
    elif (option == '-l' or '--list'):
        folderPath = sys.argv[1]
        print(ListFiles(folderPath))
    elif (option == '-f' or '--filter'):
        if (sys.argv[1] == 'oil' or '-o'):
            imgPath = sys.argv[2]
            img = OpenImg(imgPath)
            # check if sys.argv[3] exits
            if (len(sys.argv) > 4):
                level = sys.argv[3]
                OilPainting(img,level)
            if (len(sys.argv) > 5):
                level = sys.argv[3]
                size = sys.argv[4]
                OilPainting(img)
            OilPainting(img)
    # read image
    img = OpenImg(imgPath)
    showImg(img)
    
    return 1




if __name__ == '__main__':
    main()