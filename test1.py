# import the necessary packages
import cv2
import os, os.path
import sys
#image path and valid extensions
imageDir = sys.argv[1]
print(sys.argv[1]) #specify your path here
image_path_list = []
valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] #specify your vald extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

#create a list all files in directory and
#append files with a vaild extention to image_path_list
for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))
 
#loop through image_path_list to open each image
for imagePath in image_path_list:
    img = cv2.imread(imagePath)
    # display the image on screen with imshow()
    # after checking that it loaded
    if img is not None:
        cv2.namedWindow(imagePath, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(imagePath, 1200, 1200)
        cv2.moveWindow(imagePath, 700,700)
        cv2.imshow(imagePath, img)
    elif img is None:
        print ("Error loading: " + imagePath)
        #end this loop iteration and move on to next image
        continue
    
    # wait time in milliseconds
    # this is required to show the image
    # 0 = wait indefinitely
    # exit when escape key is pressed
    key = cv2.waitKey(0)
    if key == 27: # escape
        break
 
# close any open windows
cv2.destroyAllWindows()
