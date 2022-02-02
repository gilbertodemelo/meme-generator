import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeGenerator
from QuoteEngine import Ingestor, QuoteModel

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # quote_files variable
    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    # images within the images images_path directory
    imgs = []
    for root, directories, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """.Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    text_body = QuoteModel(request.form['body'], request.form['author'])
    response = request.get(image_url)
    path_temp = './temp/image_temp.png'

    with open(path_temp, 'wb') as outimage:
        outimage.write(response.content)

    path = meme.make_meme(path_temp, text_body.text, text_body.author)
    os.remove(path_temp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
