from PIL import Image
import os

def image_to_back_and_white(infile, outfile):
    img = Image.open(infile)
    thresh = 235
    fn = lambda x : 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')
    r.save(outfile)


# This function will give you a list of tuples, each containing the coordinates of the upper-left corner and the lower-right corner of each tile.
# Example usage:
# grid_w, grid_h, tile_w, tile_h = 25, 25, 11, 12
# tile_corners = get_tile_coordinates(grid_w, grid_h, tile_w, tile_h)
# print(tile_corners)
def get_tile_coordinates(grid_w, grid_h, tile_w, tile_h):
    tile_coords = []
    for y in range(0, grid_h, tile_h):
        for x in range(0, grid_w, tile_w):
            lower_right_x = min(x + tile_w, grid_w)
            lower_right_y = min(y + tile_h, grid_h)
            # tile_coords.append(((x, y, lower_right_x - 1, lower_right_y - 1)))
            tile_coords.append(((x, y, lower_right_x, lower_right_y)))
    return tile_coords

def tile2(filename, dir_in, dir_out, tile_w, tile_h):
    from itertools import product
    name, ext = os.path.splitext(os.path.basename(filename))

    print(name, ext)
    img = Image.open(filename)
    w, h = img.size

   
    tile_corners = get_tile_coordinates(w, h, tile_w, tile_h)


    for tile_coords in tile_corners:
        print(tile_coords)
        x1, y1, x2, y2 = tile_coords
        out = os.path.join(dir_out, f'{name}_{x1}_{y1}_{x2}_{y2}{ext}')
        # print(out)
        img.crop(tile_coords).save(out)	



    # for i, j in grid:
    #     box = (j, i, j+d, i+d)
    #     print(box)
    #     out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
    #     img.crop(box).save(out)

def tile(filename, dir_in, dir_out, d):
    from itertools import product
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size

    print("w/h: ", w, h)
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        print(box)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)





# tile_corners = get_tile_coordinates(25, 25, 11, 12)
# list(map(print, tile_corners))


input_img = "input\\img002.png"
# output_img = "output\\img001.png"

# image_to_back_and_white(input_img, output_img)
tile2(input_img, "input", "output", 12, 12)

img = Image.open(input_img)
# img.crop((0, 0, 2, 2)).save("output\\test02.png")
# img.crop((1, 1, 2, 2)).save("output\\test12.png")
# img.crop((2, 2, 3, 3)).save("output\\test23.png")


# x1, y1, x2, y2 = 24, 24, 25, 25
# img.crop((x1, y1, x2, y2)).save("output\\test24.png")



