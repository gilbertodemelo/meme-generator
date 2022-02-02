## **Meme Generator Project**
This project builds a meme generator: an application that creates memes. The memes include an images with an overlaying quote.

## **Application Overview**
The application deals with different text and image files. It first loads quotes from text files, specifically PDF, Word (Docx), CSV, and Text (.txt) files. As well, it loads, crops, and saves image files as well.

## Quote Engine Module
The Quote Engine Module implements several classes to parse different types of text files (pdf, txt, csv, docx). It achieves the purpose by implementing an Ingestor Interface and then a different Ingestor class for each type of file.

## Meme Generator Module
The Meme Generator Module crops and write texts onto images. It uses the image manipulation Pillow by loading an image, then cropping an image to a specified size (default is 500px). Finally, it adds a caption (string) onto the image.

## How to run the program
• First, download the code and install the dependencies.
• Install the dependencies of the application by going to the project directory and type:

    pip install -r requirements.txt

Then, run the command:

    python3 app.py