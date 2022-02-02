"""Module that crops, and a text to, and saves an image."""

import os
from time import time
from PIL import Image, ImageDraw, ImageFont
from random import randint

class MemeGenerator:
    """Class to alter and image and save it."""

    def __init__(self, write_path):
        """Construct the class."""
        self.write_path = write_path
        if not os.path.exists(self.write_path):
            os.makedirs(self.write_path)

    def make_meme(self, image, text, author, width=500) -> str:
        """Create a meme."""
        infile_img = Image.open(image)
        img_width = min(width, 500)
        img_ratio = img_width / float(infile_img.size[0])
        img_height = int(img_ratio * float(infile_img.size[1]))

        resized = infile_img.resize((img_width, img_height), Image.NEAREST)

        text_len = len(text) + len(author)
        text_body = f'{text} {author}'
        image_draw = ImageDraw.Draw(resized)
        font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf', size=18)
        image_draw.text(randint(0, text_len), randint(0, text_len), text_body, font=font, fill='white')

        # save the image
        outfile = os.path.join(self.write_path, f'Image was created at {time()}.png')
        resized.save(outfile)

        return outfile