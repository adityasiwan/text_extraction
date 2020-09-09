## Text extraction from document images

Smart phones are replacing personal scanners. They are portable, connected, powerful and affordable. They are on their way to become the new entry point in business processing applications like document archival, ID scanning, check digitization, just to name a few.


### Install

This project was built on **Python 3.6.2** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [OpenCV](https://opencv.org/)
- [NLTK](https://www.nltk.org/)
- [pytesseract](https://pypi.org/project/pytesseract/)

The same environment can be created by executing the following script in the shell :

`./install.sh`

### Run

In a terminal or command window, navigate to the top level directory (that contains this README) and run the following command:

`python main.py`

It will then ask for the set number on which you want to run the program as

![Output_1](https://raw.githubusercontent.com/adityasiwan/text_extraction/master/markdown_images/output1.png)

Enter the set number and the program will yield a cosine similarity score between the actual output document and the predicted output document as

![Output_2](https://github.com/adityasiwan/text_extraction/raw/master/markdown_images/output2.png)
### Data

The dataset used in this project is included in the `DIQ_Part1` directory.

### Deliverables:

* [Main Code](./main.py)
* [report (pdf version)](./report.pdf)
