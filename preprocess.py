import os


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Dataset"
    files = os.listdir(path)
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        f.close()

        f = open(path + "\\" + file, 'w')
        for line in lines_list:
            line = line.rstrip('\n')
            if line[-1] not in [".", "!", "?"]:
                line += '.'
            line += '\n'
            f.write(line)
        f.close()


if __name__ == "__main__":
    main()
