import argparse
import os
import requests

parser = argparse.ArgumentParser("Init AOC input data")
parser.add_argument("session_cookie", help="Your AOC session cookie", type=str)
args = parser.parse_args()

def main(session_cookie: str):
    for day in range(25):
        # skip days that don't exist
        day_dir = f"{os.getcwd()}/day-{day:02d}"
        if not os.path.isdir(day_dir):
            continue

        # skip dirs that already have data
        data_dir = f"{day_dir}/data"
        if os.path.isdir(data_dir):
            continue

        input_url = f"https://adventofcode.com/2024/day/{day}/input"
        response = requests.get(input_url, cookies={'session': session_cookie})

        if response.status_code == 200:
            os.makedirs(data_dir)
            input_file_path = f"{data_dir}/input"
            with open(input_file_path, 'wb') as file:
                file.write(response.content)
        else:
            print('Failed to download file')


if __name__ == '__main__':
    main(args.session_cookie)