# Tamil Character Predictor

An interactive demonstration of handwritten tamil character classification using Convolutional Neural Network. This model can classify 156 handwritten tamil characters.
## Contents
- [Code](#code)
- [Use Tamil Character Predictor](#use-tamil-character-predictor)
- [Setup](#setup)

## Code

Client-side is a simple one-page app made using [p5.js](https://p5js.org). 
Server-side is a python [flask](https://palletsprojects.com/p/flask/) app which uses [fastAI](https://www.fast.ai) to run the inference. 
The neural net is trained on the [hpl-tamil-iso-char-offline](https://github.com/ashwinr64/TamilCharacterPredictor/raw/master/data/hpl-tamil-iso-char-offline-1.0.tar.gz) dataset released by HP. The model makes use of the resnet50 architecture and is trained to a test accuracy of ```96%```.
To achieve the accuracy the images have been resized to ```128x128```. This was done since the average size of the images were around ```140x120```. The modified dataset can be found [here](https://github.com/ashwinr64/TamilCharacterPredictor/raw/master/data/dataset_resized_final.tar.gz).

## Use Tamil Character Predictor

This app has been deployed on heroku and can be found at [ashwinr64.github.io/TamilCharacterPredictor](https://ashwinr64.github.io/TamilCharacterPredictor/)

## Setup

### Requirements

* [Python 3.7](https://www.python.org/download/releases/3.7/)
* [pip](https://pip.readthedocs.io/en/stable/)

### Install Dependencies
```bash
pip install -r requirements.txt
``` 

### Run Application

To build and run the app locally run:
```bash
python app/server.py
```
