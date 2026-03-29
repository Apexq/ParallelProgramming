custom_power = lambda x = 0, / ,e = 1 : x**e 

def custom_equation(x : int  = 0,y : int = 0,/,a : int = 1,b: int = 1,*,c: int = 1) -> float:
    
    """
    Calculates the mathematical equation.

    :param x: The first base value.
    :param y: The second base value.
    :param a: The exponent for x.
    :param b: The exponent for y.
    :param c: The divisor.
    :return: The result of the equation.
    """

    res = float((x ** a + y**b) / c)
    return res

_call_counter = 0

def fn_w_counter() -> (int,dict[str,int]):
    global _call_counter
    _call_counter += 1
    return _call_counter,{__name__:_call_counter}
