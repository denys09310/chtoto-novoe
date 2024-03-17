from PIL import Image, ImageFilter

with Image.open('11.jpg') as original:
    pic_gray = original.convert('L')
    pic_blur = original.filter(ImageFilter.BLUR)

    pic_gray.save('negr.jpg')
    pic_blur.save('gray.jpg')
    pic_gray.show()