from PIL import Image, ImageDraw
from sort_functions import quickSortIterative
from search_functions import binary_search_sub
from PixelFunctions import compare_pixels, storePixels, pixels_to_points, pixels_to_image, grayscale

def main():
    IMG_NAME = 'monkey'

    with Image.open(IMG_NAME + '.jpg') as im:
        pixels = storePixels(im)
        print("Stored")
        sorted_pixels = pixels.copy()
        quickSortIterative(sorted_pixels, int(len(sorted_pixels[0])), int(len(sorted_pixels)) - 1, compare_pixels)
        print("Sorted")
        #sorted_im = pixels_to_image(im, pixels)
        #sorted_im.save('sorted' + IMG_NAME + '.jpg', 'JPEG')
        threshold = int(input("What threshold would you like to choose?"))
        subi = binary_search_sub([r[0][0] for r in sorted_pixels],
                                 0, len(sorted_pixels) - 1, threshold)
        print("Sublist of reds starts here: ", subi)
        grayscale(im,pixels)
        pixels_to_points(im, sorted_pixels[subi:])
    
    im.save('highlighted_' + IMG_NAME + '.jpg', 'JPEG')
    im.show()
# end of main():


if __name__ == '__main__':
    main()