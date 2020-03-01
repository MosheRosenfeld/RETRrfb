import os
import datetime
import time
def write_something(word):
    file = open("output/testfile.txt", "a")
    file.write("This is {}\n".format(word))
    file.close()
def main():
    directory = "output"
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    i = 0
    while i < 3000:
        time.sleep(1)
        i += 1
        print("working {}".format(i))
        write_something(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
if __name__ == "__main__":
    main()
