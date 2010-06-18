# TimeThis

Time your Python functions in a super simple way.

# How?

Check out timethis_test.py for examples. But here are some nice examples:

    # Print out the running time of the function.
    @timethis
    def function1():
        ...
    
    # Print out the running time of the function, but also remember previous
    # runs and show statistics over multiple runs.
    @timethis(persist=True)
    def function2():
        ...

# What's Next?

Other features such as dumping outputs to a file is planned. Or you can fork
this project and write it yourself. Give me a ping when you do.
