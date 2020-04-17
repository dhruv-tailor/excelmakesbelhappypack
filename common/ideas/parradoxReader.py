
import argparse
import json
import os
import re
import sys
import time
### https://raw.githubusercontent.com/joshnygaard/paradox-reader/master/paradoxReader.py

def main():
    start_time = time.time()
    args = _get_args()
    decode(args.file_name, args.intermediate, args.no_json)
    print("--- %s seconds ---" % (time.time() - start_time))


def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name')
    parser.add_argument('--intermediate', '-i', help="Save the intermediate code. Useful for debugging", action="store_true", default=False)
    parser.add_argument('--encode', '-i', help="Save the intermediate code. Useful for debugging", action="store_true", default=False)
    parser.add_argument('--no_json', '-n', action="store_true", default=False)

    return parser.parse_args()


def decode(file_path, save_intermediate, no_json):
    try:
        file = open(file_path, 'r',encoding="ANSI")
    except FileNotFoundError:
        print('ERROR: Unable to find file: ' + file_path)
        sys.exit()

    data = file.read()
    data = re.sub(r'#.*', '', data) # Remove comments
    data = re.sub(r'[\t ]', '', data) # Remove tabs and spaces
    data = re.sub(r'\n{2,}', '\n', data) # Remove excessive new lines
    data = re.sub(r'\n', '', data, count=1)  # Remove the first new line
    data = re.sub(r'{(?=\w)', '{\n', data) # reformat one-liners
    data = re.sub(r'(?<=\w)}', '\n}', data) # reformat one-liners
    data = re.sub(r'^([\w-]+)', r'"\g<1>"', data, flags=re.MULTILINE)  # Add quotes around keys
    data = re.sub(r'=', ':', data)  # Replace = with :
    data = re.sub(r'(?<=:)\w*[a-zA-Z_]+\w*', r'"\g<0>"', data)  # Add quotes around string values
    data = re.sub(r':"yes"', ':true', data) # Replace yes with true
    data = re.sub(r':"no"', ':false', data)  # Replace no with false
    data = re.sub(r'([<>])(.+)', r':{"value":\g<2>,"operand":"\g<1>"}', data) # Handle < >
    data = re.sub(r'(?<![:{])\n(?!}|$)', ',', data)  # Add commas
    data = '{' + data + '}'

    file_name = os.path.basename(file_path)

    if save_intermediate:
        with open(file_name + '.intermediate', 'w') as output:
            output.write(data)

    try:
        json_data = json.loads(data, object_pairs_hook=_handle_duplicates)
    except json.decoder.JSONDecodeError:
        print('ERROR: Unable to parse {}'.format(file_name))
        print('Dumping intermediate code into file: {}_{:.0f}.intermediate'.format(file_name, time.time()))

        sys.exit()
    if not no_json:
        with open(file_name + '.json', 'w') as file:
            json.dump(json_data, file, indent=4)

    return json_data

def encode(json, pretty_print = False, depth = 0):
    if pretty_print:
        end = "\r\n" + "".ljust(depth, '\t')
    else:
        end = " "
    stringout = ""
    if type(json) == dict:
        for key in json:
            stringout += "" + str(key) + " = " 
            if type(json[key]) == dict:
                stringout += "{" + end + '\t' + encode(json[key], pretty_print, depth + 1)
                stringout = stringout[:-1] + '}' + end 
            elif  type(json[key]) == list:
                length = len(str(key)) + 3
                stringout = stringout[:-length]
                for duplicat in json[key]:
                    stringout += "" + str(key) + " = " 
                    if type(duplicat) == dict:
                        stringout += "{" + end + '\t' + encode(duplicat,pretty_print,depth) + "}" + end
                    else:
                        stringout += encode(duplicat,pretty_print,depth)
            else:
                stringout += encode(json[key]) + end
    elif  type(json) == str:
        stringout += json + end
    elif  type(json) == float:
        stringout += str(json) + end
    elif  type(json) == int:
        stringout += str(json) + end
    elif  type(json) == bool:
        stringout += "yes" if json else "no"
        stringout += end
    else:
        stringout += str(type(json))
    return stringout


def _handle_duplicates(ordered_pairs):
    d = {}
    for k, v in ordered_pairs:
        if k in d:
            if isinstance(d[k], list):
                d[k].append(v)
            else:
                d[k] = [d[k], v]
        else:
           d[k] = v
    return d


if __name__ == "__main__":
    main()
