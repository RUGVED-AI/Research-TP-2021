#import libraries
import cv2
import numpy as np

#now we will define some variables(initialized with random values at first)
drawn = False
startx, starty = -1, -1
rectangle = (0, 0, 0, 0)

#we will be loading the image to memory and resizing it to an appropriate size
def load_and_resize(path):
    image = cv2.imread(path)
    new_size = (1280, 960)
    resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
    return resized_image

#now we will define region selection function
#It is responsible for handling the mouse callback events i.e. clicking the mouse ,also it takes x and y coordinates of the mouse when clicked
def select_roi(event, newx, newy, flags, params):
    global startx, starty, drawn, rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        startx, starty = newx, newy
        cv2.circle(image, (startx, starty), 4, (255, 255, 120), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawn = True
        cv2.rectangle(image, (startx, starty), (newx, newy), (0, 255, 0), 3)
        rectangle = (startx, starty, newx - startx, newy - starty)
        print("\nROI Selected Successfully")

#Foreground extraction function
#it is responsible for performing the background subtraction and display the resulting foreground image
def extract_foreground(image):
    global drawn
    cv2.namedWindow(winname='FG Extractor')
    cv2.setMouseCallback('FG Extractor', select_roi)
    print("\nSelect ROI from mouse pointer.")
    black_mask = np.zeros(image.shape[:2], np.uint8)
    background = np.zeros((1, 65), np.float64)
    foreground = np.zeros((1, 65), np.float64)
    while True:
        if drawn:
            print("\nPerforming Foreground Extraction")
            cv2.grabCut(image, black_mask, rectangle, background, foreground, 5, cv2.GC_INIT_WITH_RECT)
            # cv2.imshow('Image before multipllication',image)
            mask2 = np.where((black_mask == 2) | (black_mask == 0), 0, 1).astype('uint8')
            #cv2.imshow('Mask', mask2)
            image = image * mask2[:, :, np.newaxis]
            drawn = False
            print("\nExtraction complete")
        cv2.imshow('FG Extractor', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

#Finally, we call the ‘extract_foreground’ function to begin the foreground extraction process using the grabcut algorithm
image = load_and_resize('car.jpg')
extract_foreground(image)