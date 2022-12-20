import os

'''
All the functions in this file are used to delete an image or a folder
The functions are:
    - deleteImg
    - deleteFolder
    - deleteAllDefault
'''

def deleteImg(path = 'ProfMedia/defaultName.jpg'):
    '''
    # To delete an image

    - @path = the path of the image
    '''
    os.remove(path)
    print("image from path"+ path +" deleted successfully")

def deleteFolder(path = 'ProfMedia'):
    '''
    # To delete a folder

    - @path = the path of the folder
    '''

    os.rmdir(path)
    print("folder deleted successfully")

def deleteAllDefault(folder = 'ProfMedia'):
    '''
    -------------------------------------------------------
    WARNING: This Fuction has not been tested yet
    -------------------------------------------------------
        
    # To delete all the images in the folder

    - @folder = the path of the folder
    '''

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                pass
            # elif os.path.isdir(file_path):
            #     shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
