# Endode 🈚
Sometimes i want to encode/decode and i am not on my burp suite :)

## Installation ⚙️

```sh
git clone https://github.com/Ryukudz/endode
cd endode
pip install -r requirements.txt
```

## Features 🎯
- URL & double url encode/decode
- Base64 encode/decode
- HTML encode/decode
- Unicode, hex & octal escaping

## Usage 🪄

```sh
python3 endode.py -h
```
This will display help for the tool, Here are all the switches it supports.
```yaml
usage: endode.py [-h] [-s] [-f {url,doubleurl,base64,html,hex,unicode,octal}] [-e] [-d]
                 [-i INPUT] [-o OUTPUT] [-l FILE]

💀

options:
  -h, --help            show this help message and exit
  -s, --silent          dont print banner.
  -f {url,doubleurl,base64,html,hex,unicode,octal}, --format {url,doubleurl,base64,html,hex,unicode,octal}
                        Encoding/decoding format
  -e, --encode          Encode
  -d, --decode          Decode
  -i INPUT, --input INPUT
                        Input string to encode/decode
  -o OUTPUT, --output OUTPUT
                        Write output to file
  -l FILE, --file FILE  take input from a file
```
## Preview 🧙‍♂️

![Preview](https://raw.githubusercontent.com/Ryukudz/endode/main/preview.png)
