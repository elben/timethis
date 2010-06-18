from timethis import timethis
import unittest

@timethis
def boring_loop():
    for i in xrange(9999999):
        pass

@timethis(persist=True)
def boring_loop2():
    for i in xrange(500000):
        pass

@timethis(outfile='outputfile.txt')
def boring_loop3():
    for i in xrange(4000000):
        pass

@timethis(outfile='out.txt', persist=True)
def boring_loop4():
    for i in xrange(5999999):
        pass

boring_loop()

boring_loop2()
boring_loop2()
boring_loop2()
boring_loop2()

boring_loop3()
boring_loop3()

boring_loop4()
boring_loop4()
boring_loop4()


class TestTimeThis(unittest.TestCase):
    def test_plain_decorator(self):
        @timethis
        def temp(): pass

        self.assertTrue(hasattr(temp, '__call__'))

    def test_fancy_decorators(self):
        @timethis(persist=True)
        def temp(): pass
        self.assertTrue(hasattr(temp, '__call__'))

        @timethis(display=False, persist=True, outfile='test.dat')
        def temp(): pass
        self.assertTrue(hasattr(temp, '__call__'))

if __name__ == '__main__':
    unittest.main()
