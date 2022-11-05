# Copyright (c) 2022 by James K. Lawless
# jimbo@radiks.net
# License: MIT / X11
# See: http://jiml.us/license2022.php
# for full license details.
 
import argparse
from rembg import remove
from PIL import Image 
    
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.description="Remove background from an image file"
    parser.add_argument("-infile",required=True)
    parser.add_argument("-outfile",required=True)
    args=parser.parse_args()
    inp = Image.open(args.infile)
    output = remove(inp)
    output.save(args.outfile)
    