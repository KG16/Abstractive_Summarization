import os


def main():
    path = "C:\\Users\\kriti\\Documents\\Project\\Abstractive_Summarization\\Output"
    files = os.listdir(path)
    for file in files:
        f = open(path + "\\" + file, 'r')
        lines_list = f.readlines()
        print(lines_list)
        f.close()
        # return
        f = open(path + "\\" + file, 'w')

        line = lines_list[0]
        string = ""

        if 'a' <= lines_list[0] <= 'z':
            string += line[0].upper()
        for i in range(line.__len__()):
            if (line[i] in ('.' or ',' or '!')) and line[i - 1] == ' ':
                if i + 1 < line.__len__() and 'a' <= line[i + 1] <= 'z':
                    string += '. '
                    string += line[i + 1].upper()
            elif line[i - 1] != '.' or ' ':
                string += line[i]
            # elif line[i] == ' ' and line[i+1] != '.':
            #     string += line[i]
        f.write(string)
        print(string)
        f.close()
        break


if __name__ == "__main__":
    main()
