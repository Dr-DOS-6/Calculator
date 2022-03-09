import multiprocessing as ml
def test1(test1_a):
    print(test1_a)
def test2(test1_a):
    print(test1_a)
if __name__ == "__main__":
    queue=ml.Queue()
test1_p = ml.Process(target=test1,args=('test',))
test2_p = ml.Process(target=test2,args=('test',))
test1_p.start()
test2_p.start()