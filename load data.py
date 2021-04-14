def load():
    with open(file, "r") as f:
        raw_lines = f.load(file)
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    lines.pop(0)
    datas = [convert_line_to_data(line) for line in lines]
    return datas

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="load file",
                    type=str)
args = parser.parse_args()
if args.file :
    print("loading...")
    print(args.file, load)
    print("Selamat datang di 'kantong ajaib!'")
else:
    print("Tidak ada folder yang diberikan!")
    print("USAGE:", args.file)
