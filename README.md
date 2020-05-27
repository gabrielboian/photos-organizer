## photos-organizer
A simple script to organize your photos using Python

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
Some times this script cannot be able to organize your pictures because we are using Pillow and for a BUG issue they can't get METADATA using getexif on code.

### Prerequisites
Assuming you have already installed Python 3 and pip on your machine, it's a good practice to create a Virtualenv so for doing that type the command below.

On your directory:
```
virtualenv -p python3 env
```

### Installing
On your directory:
```
git clone https://github.com/gabrielboian/photos-organizer.git
```

after cloning the repo:
Start your virtualenv:
```
source env/bin/activate
```

Entry on folder and type:
```
pip install -r requirements.txt
```

### Running
After all steps above get on your directory with your photos and run the script

If your script is inside of the photos directory
```
python index.py
```

If your script is outside of the photos directory
```
python ../path/to/script
```

## Author

* **Gabriel Boian** - [GabrielBoian](https://github.com/gabrielboian)

## License

This project is licensed under the MIT License