from PIL import Image, ImageDraw



def compare_pixels(pix1,pix2):
    return pix1 > pix2


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    for i in range(width):
        for j in range(height):
            # get rgb values of pixel at position
            r, g, b = im.getpixel((i,j))
            pixel_array.append([(r,g,b), (i,j)])

    return pixel_array
#end function


def pixels_to_points(im, pixels):
    for p in pixels:
        im.putpixel(p[1], p[0])
    im.show()


def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    outimg.putdata([p[0] for p in pixels])
    outimg.show()
    return outimg


def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2])/3)
        draw.point(px[1], (gray_av, gray_av, gray_av))