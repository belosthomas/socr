# Structured OCR

## About

Structured OCR is a line localization and text recognition tools using Deep Learning with PyTorch.

## Setting up

### Requirements

 - If you want to use GPU, **NVIDIA Graphic Card with CUDA 8 minimum**, otherwhise use ```--disablecuda``` 
 - Python 3 with Anaconda and Pip
 - GCC and G++ Version 5 (even if it's not your default compiler)

Only on Windows :
 - Microsoft Visual C++ 14.0 (2015) is required. Get it with "Microsoft Visual C++ Build Tools": https://www.microsoft.com/en-us/download/details.aspx?id=48159

### Compilation

Use ```python3 setup.py install_requirements``` to install all the necessary requirements.
Then, to compile, run ```python3 setup.py build_ext --inplace```.

## How to recognize a page of text ?

### Command line

Please make sure that the checkpoints .pth.tar files is present under the ```checkpoints``` folder.
Then run 
```./launch recognizer [your files] [your folders]  ...```

### API

See [example.ipnyb](examples/example.ipynb)

### Trained models

You can download the trained models and copy it to the checkpoints folder : 
[Download on DropBox](https://www.dropbox.com/sh/wvhdnldsq4652wx/AAA3iUDFWHVh56zPia10nwrQa?dl=0)

## How to train/test with command line

### Settings up the database

Modify the file ```datasets.cfg``` so it correspond to your data-sets.
See [datasets.example.cfg](examples/datasets.example.cfg) for a example.

### How to train/test the line recognizer ?

Execute ```./launch line --model dhSegment --name myDhSegmentTraining --bs 8 --lr 0.0001``` to train the line recognizer.
Use ```./launch line --help``` for more help.

You can modifiy the file ```settings.cfg``` for more configuration.

### How to train/test the ocr network ?

Execute ```./launch text --model resSru --name myResSruTraining --bs 8 --lr 0.0001``` to train the ocr network.
Use ```./launch text --help``` for more help.

You can modifiy the file ```settings.cfg``` for more configuration.

### Command line arguments

You can select a model using the ```--model [MODEL]``` argument, and give a custom name to a model by using ```--name``` argument.
When ```CTRL-C``` is pressed, the program will ask you to save the weight or not. The weights are saved under the checkpoints folder, with the given name as argument, or with the model name if no name is specified.
The programe will automatically load the good model.

In can of problem, a backup of the weights are made with the extension ```.autosave``` under the ```checkpoints``` folder.

The ```--lr [lr]``` option permit to select the initial learning rate. Use ```--overlr``` to override the current learning rate.

The ```--bs``` option permit to specify a batch size.

### Multi-GPU

Use ```CUDA_VISIBLE_DEVICES=0,1``` to select the available GPU. SOCR will use all available GPU if you are training, or one GPU if you only evaluate.

## Make a custom model

See [socr/models/README.md](socr/models/README.md)