from multiprocessing import Process, Manager
import time

def f(val):
    print 'CHILD: val.value: %s' % val.value
    for i in range(10):
        print '\ti: ',i
        print '\tval.value',val.value
        time.sleep(1)

if __name__ == '__main__':
    manager = Manager()

    val = manager.Value(str, 'start')
    print 'PARENT: val.value: %s' % val.value

    p = Process(target=f, args=(val, ))
    p.start()

    for j in range(10):
        print '\tj: ',j
        val.value = 'it'+str(j)
        print '\tval.value',val.value
        time.sleep(1)