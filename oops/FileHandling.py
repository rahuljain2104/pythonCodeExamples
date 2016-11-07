import  FileNotFoundException

try:
    file = open('mydata2.txt', 'w+', encoding="utf-8")
    if file is None:
        raise FileNotFoundException

    file.write("writing in the file.. hurray")

    file1 = open('mydata3.txt')


except IOError:
    print("IO error, file not found")

