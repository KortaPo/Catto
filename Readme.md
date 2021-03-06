## What is Catto
Catto is a command line program that downloads random cute animal images, gifs and videos based on your choices. 
This tool is written in `python` and uses [Typer](https://typer.tiangolo.com/) command line framework.

## Installation
Catto can be directly installed using [pip package manager](https://pip.pypa.io/en/stable/) or [Poetry package manager](https://python-poetry.org/) using git:

<strong>Pip</strong>
```bash
pip3 install git+https://github.com/KortaPo/Catto.git
```

<strong>Poetry</strong>
```bash
poetry add git+https://github.com/KortaPo/Catto.git#main
```

## Installation through the repository
If you wish to keep a local version `catto`, you can clone this repository:
```bash
git clone https://github.com/KortaPo/Catto.git
```

To install the required dependencies, you can do the following:

Use [pip package manager](https://pip.pypa.io/en/stable/) to install the libraries from ``requirements.txt`` file.

```bash
pip3 install -r requirements.txt
```

If you have [Poetry package manager](https://python-poetry.org/) installed, you can install the dependencies using 
the following command.

```bash
poetry install
```
As we have included a `pyproject.toml` file, poetry will automatically install the dependencies from the file.

Once you have installed the dependencies, you can use `catto` either, as a python module, or running the `setup.py` file:
```bash
python3 setup.py install
```
or 

```bash
python3 -m catto help
```
## Catto Usage
Catto has two ways to download images:

<strong>1.) Manual</strong>
```bash
catto download --category cats --amount 3 --path ./my_directory_where_the_images_need_to_be_stored
```
The above command will download `3` cute and random images of `cats` ( based on your choice ) to the directory which you provided.

Let's dissect the above command a bit more:

* `--category`: This flag takes the specific type of animal's image you wish to download.
* `--amount`: This flag takes the amount of images of the specific animal that would be downloaded.
* `--path`: This flag takes the path to the directory, where `catto` will download the random images.

This is a simple and fast method of using `catto`, if you wish not to use `catto` in interactive mode.

<strong>Download Command Output</strong>
<img src="./gallery/catto-output/catto_download_output.png" width=450px></img>

<strong>2.) Interactive</strong>
```bash
catto interactive
```
This command will start an interactive `catto` command line session, that will prompt you with a series of questions and choices, and based on your choices 
it will download your images. It has a fancy UI, and it is hard to explain through words, so try it yourself and see.

<strong>Interactive Command Live Output</strong>
<a href="https://asciinema.org/a/VbEQY9JRFk4TYM9jGvdEu5zl9" target="_blank"><img src="https://asciinema.org/a/VbEQY9JRFk4TYM9jGvdEu5zl9.svg" /></a>

## Commands
`Catto` has the following commands:

* `catto help` - *This command shows the help menu of catto.*
* `catto download` - *Simple and a fast way to use catto to download images of your choice.*
* `catto interactive` - *Run catto in an interactive session.*
* `catto version` - *This command shows the current version of catto that is currently installed.*
* `catto status` - *This command shows all the status of all the API endpoints used by catto to search for images.*
* `catto show-all-animals` - *This command shows all the animal categories supported by catto currently.*
* `catto logo` - *This command shows the logo of catto in an animated way.*

## Note
Currently, `catto` will download the images in `<selected-animal>-image-<random-hex-number>` format.

For example:
`cats-image-cdf79775`.

The reason for this feature is that they can be easily distinguished between different animal types and this allows make
sure that the images almost always have a unique random hex number.


## Appreciation
Please read the LICENSE contained in this repository and follow its terms and conditions, and if you enjoy and like using this tool, please star
and share this project, it would be greatly appreciated.
