#!/usr/bin/python3
# v0.0.1 25.09.2021
# Kerszi (Szikers)
# git - https://github.com/kerszl/demorse
import argparse
from os import sys
import re

MORSE_CODE = {
".-": "a",
"-...": "b",
"-.-.": "c",
"-..": "d",
".": "e",
"..-.": "f",
"--.": "g",
"....": "h",
"..": "i",
".---": "j",
"-.-": "k",
".-..": "l",
"--": "m",
"-.": "n",
"---": "o",
".--.": "p",
"--.-": "q",
".-.": "r",
"...": "s",
"-": "t",
"..-": "u",
"...-": "v",
".--": "w",
"-..-": "x",
"-.--": "y",
"--..": "z",
"-----": "0",
".----": "1",
"..---": "2",
"...--": "3",
"....-": "4",
".....": "5",
"-....": "6",
"--...": "7",
"---..": "8",
"----.": "9",
".-.-.-": ".",
"---...": ":",
"--..--": ",",
"-.-.-.": ";",
"..--..": "?",
"-...-": "=",
".----.": "'",
"-..-.": "/",
"-.-.--": "!",
"-....-": "-",
"..--.-": "_",
".-..-.": "\"",
"-.--.": "(",
"-.--.-": ")",
"...-..-": "$",
".-...": "&",
".--.-.": "@"
}

def get_param ():
    #exception for "--" in head of string
    if len(sys.argv)==3:
        if sys.argv[2]=='--':
            return '--'
            
    parser = argparse.ArgumentParser(description="""The program converts the morse code to plain text. 
You can throw in some text like this "\..../.\.-.. .-..|---".
The program will cut unnecessary characters and convert 
it into plain text like: ".... . .-.. .-.. ---" and
convert it to "hello".

Example: demorse -t ".... . .-.. .-.. ---"
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-t', '--text', type=str, help="Text to decode", default=None, nargs=argparse.REMAINDER)
    
    args = parser.parse_args()
        
    if args.text:        
        return str(args.text)
    else:      
        parser.print_help()
        return None

def decode_morse_code(pure_morse_code_2_decode):
    decode_string =""
    morse_string=""
    for i in pure_morse_code_2_decode:
        if i in MORSE_CODE:
            decode_string+=MORSE_CODE[i]
            morse_string+=i+" "
    if len(decode_string)>0:
        return(morse_string,decode_string)
    else:
        return (None,None)


def leave_plain_text (morse_string_code):
    #Clean from unnecessary signs    
    decode_morse_string=re.sub("[^.-]"," ",morse_string_code)
    decode_morse_string=re.sub(" +"," ",decode_morse_string.strip())

    #return string2list
    if (len(decode_morse_string)>0):
        return list(decode_morse_string.split(' '))
    else:
         return None

#----


def just_decode (text2decode):    
    if text2decode:        
        pure_text=leave_plain_text(text2decode)    
        if pure_text:        
            morse_string,decode_morse_string=decode_morse_code(pure_text)        
            if decode_morse_string:            
                print ("Morse   :",morse_string)
                print ("Demorse :",decode_morse_string)
            else:
                print ("No real morse code")
        else:
            print ("Nothing to decode")
    
text2decode=get_param()
just_decode (text2decode)


