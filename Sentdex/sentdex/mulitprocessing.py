from multiprocessing import Pool
def num(n):
    return n*2
if __name__=='__main___':
    a=Pool(processes=20)
    data=a.map(num,range(10))
    a.close()
    print(data)        
