from timethis import timethis

@timethis
def boring_loop():
    for i in xrange(9999999):
        pass

@timethis('persist')
def boring_loop2():
    for i in xrange(500000):
        pass

boring_loop()
boring_loop2()
boring_loop2()
boring_loop2()
boring_loop2()
