from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('IMG_20210130_094722.JPG')
# show image
plt.imshow(img)
plt.show()

small_img=img.resize((128,128),Image.BILINEAR)

#resize
o_size=(1000,1000) #output size
res=small_img.resize(o_size,Image.NEAREST)
#save image
res.save('test.png')
#display image
plt.imshow(small_img)
plt.show()