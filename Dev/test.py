num = int()
def seven(ipt):
    while ipt <= 7:
        ipt = ipt - 2*ipt[-1]
        if ipt == 7:
            print("it's multiplied by 7")
        else:
            print("it's not multiplied by 7")
if __name__ == "__main__":
    seven(1024)