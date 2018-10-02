def eulersMethod(diffEq, x0, y0, xFinal, deltaX):
    '''
    Uses Euler's Method to approximate a y-value of a function given
    that functions derivative in terms of x and y, and given a starting
    point for that function
    
    @param diffEq a derivative of a function in terms of x and y
    @param y0     a starting y-coordinate of the function
    @param x0     a starting x-coordinate of the function
    @param xFinal the x-value of interest
    @param deltaX the step to be used for the approximation
    '''
    #TODO: make help more mathy

    x = x0
    y = y0
    yield (x, y)

    while x+deltaX <= xFinal:
        roc = diffEq(x, y)  # rate of change
        x += deltaX
        y += roc * deltaX
        yield (x, y)

    if x < xFinal:
        roc = diffEq(x, y)
        deltaX = xFinal - x
        x = xFinal
        y += roc * deltaX
        yield (x, y)
