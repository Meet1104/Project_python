x = 10
def demo_scope():
    x = 20
    return x
print("Global:", x)
print("Local:", demo_scope())
