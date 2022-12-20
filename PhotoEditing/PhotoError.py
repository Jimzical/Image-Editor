
'''
To Handel Errors
'''


class ImageTypeError(Exception):
    """
    ### Raised When the image format is not supported
    """
    pass

def checkFormat(format):
    try:
        if format in ['.jpg','.jpeg','.png','.bmp']:
            pass
        else:
            raise ImageTypeError
    except ImageTypeError:
        print('ImageTypeError: The image format is not supported\nTry one of these formats: jpg, jpeg, png, bmp')
        return
