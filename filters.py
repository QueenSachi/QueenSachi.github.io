from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open(filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(img):
    img.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(img, filename):
    img.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):
    newdata = []
    data = list(img.getdata())
    for i in range(len(data)):
        intensity=data[i][0]+data[i][1]+data[i][2]



        if intensity < 182:
            newdata.append((0,51,76))
        elif intensity < 364:
            newdata.append((217,26,33))
        elif intensity < 546:
            newdata.append((112,150,158))
        else:
            newdata.append((252,227,166))
    img.putdata(newdata)
    img.show()

    def filter1(img):
        newdata = []
        data = list(img.getdata())
        for i in range (len(data)):
            newdata.append((data[i][0],0,0))
        img.putdata(newdata)
        img.show()


        #picking the right  pixel based on intensity
    newImage.putdata(newdata)
    newImage.show()
