[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



##
# Silv3rMist -> 🕵️‍♀️
An Information Gathering tool uses [Hunter](https://hunter.io/), [Clearbit](https://clearbit.com/) and [OpenAI](https://openai.com/) to perform OSINT written in Python3.

### 🔧 Technologies & Tools

![](https://img.shields.io/badge/OS-Linux-informational?style=flat-square&logo=ubuntu&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Editor-VS_Code-informational?style=flat-square&logo=visual-studio&logoColor=white&color=5194f0)
![](https://img.shields.io/badge/Language-python-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)
![](https://img.shields.io/badge/Python_Version-3.10-informational?style=flat-square&logo=python&logoColor=white&color=5194f0&bgcolor=110d17)

##

### 📚 Requirements
> - Python 3.9+
> - pip3

### Features
- Quick and easy to use
- User-friendly Textual Interface
- Gather information about a domain, IP address, or a company etc.

> `Note:` Please keep in mind that the tool is still in development and more features will be added soon.
##

### Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
if not installed, install it using the following command.
```bash
sudo apt-get install python3-pip
```

> It is advised to install the python requirements in a virtual environment, for that install the venv package.

```bash
    python3 -m pip install venv
    python3 -m venv env
    source env/bin/activate
```
After that run the following commands:
```bash
    python3 -m pip install -r requirements.txt
```
##

### Configuration
To use the tool, you need to get the API keys from the following websites:
- [Hunter](https://hunter.io/)
- [Clearbit](https://clearbit.com/)
- [OpenAI](https://openai.com/)

After getting all the API keys, Create a file name `.env` in the root directory and add the following lines:
```bash
touch .env
```
Save the API keys in the `.env` file as follows:
```bash
HUNTER_API_KEY=a277************************************
CLEARBIT_API_KEY=sk_8*******************************
OPENAI_API_KEY=sk-M******************************
```

## Usage

```bash
python3 main.py
```
##
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)