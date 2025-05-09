import timeit
from fibonacci import fibonacci

def test_fib onacci () :
	assert fibonacci (0) == 0
	assert fibonacci (1) == 1
	assert fibonacci (5) == 5
	print ( " Pruebas pasadas ! Codigo de Elio 806" )

if __name__ == " __main__ " :
	test _fibonac ci ()
	time = timeit . timeit ( " fibonacci (20) " ,
		setup = " from fibonacci import fibonacci " ,
		number =100)
	print ( f " Tiempo : { time :.4 f } segundos " )
