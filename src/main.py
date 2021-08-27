from functions import FitsHandler
import sys
import numpy as np

def main(fits_path, csv_path):
    handler = FitsHandler(fits_path)
    handler.open_fits()

    header = handler.header()
    with open("{}_header.txt".format(csv_path), "w") as f:
        f.write(str(header))

    # DSHARPデータは(画像データ，枚数，縦，横)の配列になっているので画像のみ取り出す
    counter = 0
    datas = handler.data()[0]
    for data in datas:
        np.savetxt("{}_data_{}.csv".format(csv_path, counter), data)
        counter += 1

def usage():
    print("Usage: main.py fits_path save_path")

def help():
    print("Usage: main.py fits_path save_path")

if __name__ == '__main__':
    args = sys.argv
    if len(args) <= 2:
        usage()
    else:
        fits_path = args[1]
        csv_path = args[2]
        main(fits_path, csv_path)
