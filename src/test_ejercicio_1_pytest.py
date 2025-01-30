import pytest
#primer ejercicio
def capital_case(x): #cambio de la funcion
    if not isinstance(x, str):
        raise TypeError('Debes de proporcionar un string')
    return x.capitalize()
def test_capital_case():
    assert capital_case('semáforo') == 'Semáforo'
#tras cambiar el nombre del fichero a test y añadimos la función:
def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
