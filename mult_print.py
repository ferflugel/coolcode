L = range(104, 0, -1)
def multiple_prints(_list):
    try:
        dummy = 100 / _list[0]
        print(':)', _list[0])
        multiple_prints(_list[1:])
    except:
        exit
multiple_prints(L)