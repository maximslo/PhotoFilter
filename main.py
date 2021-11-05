#
# PhotoFilter by Maxim Slobodchikov
#

from hmcpng import load_pixels #returns 2D list containing pixels for that image
from hmcpng import save_pixels #saves PNG image to disk
from hmcpng import compare_images 

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

# function 1
def grayscale(pixels):
    """Returns a 2D list of pixels that is a greyscale version of the original image."""
    height = len(pixels)
    width = len(pixels[0])

    new_pixels = create_uniform_image(height, width, [0, 255, 0])
    
    for r in range(height):
        for c in range(width):
            pixel = pixels[r][c]
            
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            
            greys = brightness([red, green, blue])
            
            new_pixels[r][c] = [greys, greys, greys]

    return new_pixels

# function 2
def mirror_vert(pixels):
    """Returns a 2D list of pixels for an image in which the original is mirrored vertically."""
    h = len(pixels)
    w = len(pixels[0])
    
    new_pixels = create_uniform_image(h, w, [0, 255, 0])
            
    for r in range(h):
        for c in range(w):
            if r < h//2:
                new_pixels[r][c] = pixels[r][c] #leave it as is
            else:
                new_pixels[r][c] = pixels[-r-1][c] #if NOT then flip
            
    return new_pixels

# function 3 
def flip_horiz(pixels):
    """Returns a 2D list of pixels for an image in which the original image is “flipped” horizontally."""
    h = len(pixels)
    w = len(pixels[0])
    
    new_pixels = create_uniform_image(h, w, [0, 255, 0])
    
    for r in range(h):
        for c in range(w):
            new_pixels[r][c] = pixels[r][-c-1]
            
    return new_pixels

# function 4
def extract(pixels, rmin, rmax, cmin, cmax):
    """Returns a new 2-D list that represents the portion of the original image that is specified by the other four parameters."""
    
    new_pixels = create_uniform_image(rmax-rmin, cmax-cmin, [0, 255, 0])
    
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            new_pixels[r-rmin][c-cmin] = pixels[r][c]
            
    return new_pixels
