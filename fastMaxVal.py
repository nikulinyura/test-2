def fastmaxVal(toConsider, avail, memo = {}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    # elif toConsider[0].

