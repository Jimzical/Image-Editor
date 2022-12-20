import os
import cv2
import PhotoError

'''
All the functions in this file are used to take an image from a file and show it
The functions are:
    - OpenImg
    - showImg
    - SaveImg
'''

def OpenImg(path):
    '''
    # To take an image from a file

    - @path = the path of the image

     Return the image
    '''
    readImg = cv2.imread(path)
    print("image read successfully")
    return readImg



def showImg(img , windowName = 'Image' , waitTime = 0,Resize = 1):
    '''  
    # To show an image

    - @img = the image that you want to show (the item returned from takeImg)
    - @windowName = the name of the window that will show the image (default = 'Image')
    - @waitTime = the time that the image will be shown (default = 0 which is forever)
    '''
    img = cv2.resize(img, (img.shape[1]*Resize, img.shape[0]*Resize))
    cv2.imshow(windowName, img)
    cv2.waitKey(waitTime)
    cv2.destroyAllWindows()



def SaveImg(img, name = 'defaultName', folder = 'ProfMedia', format = 'jpg', overwrite = False):
    '''
    # To save an image
    
    - @img = the image that you want to save (the item returned from takeImg)
    - @name = the name of the image you want to save it as (default = 'defaultName')
    - @folder = the folder that you want to save the image in (default = 'ProfMedia', it will create the folder if it doesn't exist)
    - @format = the format of the image (default = '.jpg')   
    optional:
    - @overwrite = if you want to overwrite the image if it already exists (default = False)
    '''

    print("saving image")
    format = '.' + format
    PhotoError.checkFormat(format)

    path = folder + '/' + name + format

    if not os.path.exists(folder):
        os.makedirs(folder)
        print("folder created successfully")

    if overwrite == False:
        fileNumber = 0
        while (os.path.exists(path)):
            fileNumber += 1
            path = folder + "/" + name + str(fileNumber) + format
            print("path__: " + path)
        
    print("path: " + path)
        
    cv2.imwrite(path, img)


def ListFiles(path):
    '''
    # To list all the files in a folder

    - @path = the path of the folder

     Return a list of all the files in the folder
    '''
    return os.listdir(path)