import argparse
import urllib.parse
import base64
import html
import sys
from rich import print


def encode_decode(input_string, mode, format):
    if format == "url":
        if mode == "encode":
            return urllib.parse.quote(input_string, safe='')
        elif mode == "decode":
            return urllib.parse.unquote(input_string)
    elif format == "base64":
        if mode == "encode":
            input_bytes = input_string.encode('utf-8')
            encoded_bytes = base64.b64encode(input_bytes)
            return encoded_bytes.decode('utf-8')
        elif mode == "decode":
            try:
                input_bytes = input_string.encode('utf-8')
                decoded_bytes = base64.b64decode(input_bytes)
                return decoded_bytes.decode('utf-8')
            except base64.binascii.Error:
                raise ValueError("Invalid base64 input.")
    elif format == "html":
        if mode == "encode":
            return html.escape(input_string)
        elif mode == "decode":
            return html.unescape(input_string)
    elif format == "doubleurl":
        if mode == "encode":
            double_urlencode = urllib.parse.quote(input_string, safe='')
            double_urlencode = urllib.parse.quote(double_urlencode, safe='')
            return double_urlencode
        elif mode == "decode":
            decoded_url = urllib.parse.unquote(input_string)
            decoded_url = urllib.parse.unquote(decoded_url)
            return decoded_url
    elif format == "hex":
        if mode == "encode":
            encoded_hex = input_string.encode('utf-8').hex()
            return encoded_hex
        elif mode == "decode":
            try:
                decoded_hex = bytearray.fromhex(input_string).decode('utf-8')
                return decoded_hex
            except ValueError:
                raise ValueError("Invalid hex input.")
    elif format == "unicode":
        if mode == "encode":
            encoded_unicode = ''.join([f'\\u{ord(char):04x}' for char in input_string])
            return encoded_unicode
        elif mode == "decode":
            decoded_unicode = bytes(input_string, 'utf-8').decode('unicode_escape')
            return decoded_unicode

    elif format == "octal":
        if mode == "encode":
            escaped_octal = ''.join([f'\\{ord(char):03o}' for char in input_string])
            return escaped_octal
        elif mode == "decode":
            try:
                unescaped_octal = bytes(input_string, 'utf-8').decode('unicode_escape').encode('latin1').decode('utf-8')
                return unescaped_octal
            except ValueError:
                raise ValueError("Invalid octal input.")

    raise ValueError("Invalid format specified.")

def input_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except IOError:
        print("[red][✖] [white]File '{}' not found.".format(file_path), file=sys.stderr)
        sys.exit(1)

def write_output_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
            print("[green][✓] [white]Output written to file: '{}'.".format(file_path))
    except IOError:
        print("[red][✖]Error: [white]Unable to write output to file '{}'.".format(file_path), file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='💀')
    parser.add_argument('-s', '--silent', action='store_true', help='dont print banner.')
    parser.add_argument('-f', '--format', choices=['url', 'doubleurl', 'base64', 'html', 'hex', 'unicode', 'octal'], help='Encoding/decoding format')
    parser.add_argument('-e', '--encode', action='store_true', help='Encode')
    parser.add_argument('-d', '--decode', action='store_true', help='Decode')
    parser.add_argument('-i', '--input', help='Input string to encode/decode')
    parser.add_argument('-o', '--output', help='Write output to file')
    parser.add_argument('-l','--file', help='take input from a file')

    args = parser.parse_args()
    if not args.silent:
        print('''[red]___  _  _  ___    __  ___  ___ 
(  _)( \( )(   \  /  \(   \(  _)
 ) _) )  (  ) ) )( () )) ) )) _)
(___)(_)\_)(___/  \__/(___/(___)
        [red][[white]coded by ryuku 🥷[red]]
''')
    if not args.encode and not args.decode:
        args.encode = True

    if args.input:
        input_string = args.input
    elif args.file:
        input_string = input_file(args.file)
    else:
        print("[red][?] [white]No input specified.", file=sys.stderr)
        sys.exit(1)

    if not args.format:
        print("[red][?] [white]No format specified.", file=sys.stderr)
        sys.exit(1)

    try:
        output_string = encode_decode(input_string, "encode" if args.encode else "decode", args.format)
    except ValueError as e:
        print("Error:", str(e), file=sys.stderr)
        sys.exit(1)

    print(output_string)
    if args.output:
        write_output_file(args.output, output_string)
