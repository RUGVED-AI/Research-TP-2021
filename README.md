# **Foreground Extraction Using Grabcut Algorithm**

### Foreground extraction refers to the process of employing image segmentation techniques and algorithms to extract the foreground (desired) and discard the background (undesired) part of an image or video feed.


![Car Image](car.jpg)

###  **Grabcut is a robust computer vision algorithm for foreground extraction. The algorithm can be summarized as below –**       
#### 1. Coordinates of a rectangle enclosing the region of interest are defined (area lying outside these coordinates are automatically defined as part of the background).  
#### 2. The parts that are classified as ‘background’ in the above step are used as a reference to classify the pixels inside the user-defined-ROI. The Gaussian mixture model is used to label pixels as probable background/foreground.
#### 3. Each pixel is connected to its surrounding pixels and each edge is assigned a probability of being foreground or background.

#### Thus the image is segmented into two parts foreground and background.

### **Results of Foreground Extraction**  

#### This is the result of the foreground extraction of one of the sample images that we gave to our code and we can see that the grabcut algorithm has really done its job quite well!  

![Result](background_extraction_final.png)# Research-TP-2021
