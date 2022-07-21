def f():
    a=10
    def g():
        print("Hello")
        nonlocal a
        a=40
        print(a)
    g()
f()