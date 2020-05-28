

#task Read an integer . For all non-negative integers , print . See the sample for details.

#Input Format

#The first and only line contains the integer, .


if __name__ == '__main__':
    n = int(raw_input())
    i=0
    num=0
    for i in range(n):
        num=i*i
        print("{}".format(num))