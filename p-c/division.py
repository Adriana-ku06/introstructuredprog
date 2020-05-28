#Task
#Read two integers and print two lines. The first line should contain integer division

#You don't need to perform any rounding or formatting operations.


from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print("{}\n{}".format(a//b, a/b))