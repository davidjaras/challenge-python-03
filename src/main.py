# Resolve the problem!!
import re


def run():
    # Start coding here
    pattern = re.compile(r'[a-zA-Z]+')

    with open('encoded.txt', 'r', encoding='utf-8') as f:
        for line in f:
            response = re.findall(pattern, line)
    
    hide_message = ''.join(response)
    print(hide_message)


if __name__ == '__main__':
    run()
