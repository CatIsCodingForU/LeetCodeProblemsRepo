def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > (2 ** 31 - 1) or x < (2 ** 31) * (-1):
        return 0
    else:
        old_int_str = str(x)
        new_int_str = ""
        minus = False

        if old_int_str[0] == '-':
            minus = True
            old_int_str = old_int_str[1:]

        for i in range(len(old_int_str) - 1, -1, -1):
            new_int_str += old_int_str[i]
        new_x = int(new_int_str)
        if new_x >= 2 ** 31 - 1:
            return 0
        if minus:
            new_x *= -1

        return new_x


