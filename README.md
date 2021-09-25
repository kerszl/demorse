# Demorse
![obraz](https://user-images.githubusercontent.com/45152848/134786084-6e3bf6e2-a599-465e-9ad5-0c5be600fd62.png)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Remove](#remove)
* [Example of use](#Example-of-use)

## General info
When doing CTF assignments you sometimes need to decode the morse code. You can do it through websites, but you can also use demorse. The program is small, fast, and resistant to weird inserts characters.
	
## Technologies
Project is created with:
* Python 3: 
	
## Setup
To run this program, install it locally using Git:
### Linux
```
$ git clone https://github.com/kerszl/demorse
$ cd demorse
$ chmod +x install.sh uninstall.sh
$ ./install

```
### Windows
```
$ git clone https://github.com/kerszl/demorse
$ cd demorse
$ python3 demorse.py
```
## Remove
### Linux
```
./uninstall
```
### Windows
Just remove 

## Example of use
```
demorse -t "This is not ....-.-. a morse code, but it is \..../.\.-.. .-..|---"
demorse -t ... --- ...
```
