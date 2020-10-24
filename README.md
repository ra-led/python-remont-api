# python-remont-api
API for interior quality classification

<!-- GETTING STARTED -->
## Getting Started

How to start with our app

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python >= 3.6
```sh
$ sudo apt update
$ sudo apt install python3.6
$ sudo apt install python3-pip
```

### Installation

1. Clone the repo
```sh
$ git clone https://github.com/ra-led/python-remont-api.git
$ cd python-remont-api
```
2. Install Python packages
```sh
$ pip3 install -r requirements.txt
```
3. Download pre-trained weights
```sh
$ gdown https://drive.google.com/uc?id=1pewnHlXGvPEd0h6yzueIpKq8hlnmCU-E
```

### Start server

Start server with Flask default WSGI
```sh
$ python3 run.py
```
Server will start on port 5005, to change port set it in `conf.yml`

Alternativly, you can use [Gunicorn](https://gunicorn.org/) WSGI

<!-- USAGE EXAMPLES -->
## Usage


