def sun_and_product(*args):
    total = sum(args)
    product = 1
    for num in args:
        product *= num
    return total,product

print(sun_and_product(1,2,3,4))