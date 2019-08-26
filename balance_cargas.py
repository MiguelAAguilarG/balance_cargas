import random

def creador_random_fases(a, b, n_fases, elementos_fase):
	lista_principal = []
	c_fases = 0
	for x in range(n_fases):
		lista_principal.append([])
		for y in range(elementos_fase):
			y = random.randint(a,b)
			lista_principal[c_fases].append(y)
		c_fases = c_fases + 1

	return lista_principal

def balanceador(lista_principal_aux):
	lista_principal_plana = []

	suma_cargas = 0
	for x in lista_principal_aux:
		for y in x:
			suma_cargas = suma_cargas + y
			lista_principal_plana.append(y)

	lista_principal_plana_ordenada = sorted(lista_principal_plana, reverse = True)

	lista_principal_balanceada = []
	c_fases = 0
	for x in range(n_fases):
		lista_principal_balanceada.append([])

	promedio_cargas = suma_cargas/n_fases

	for x1 in lista_principal_plana_ordenada:
		suma_cargas_fase = []
		for x2 in lista_principal_balanceada:
			suma_cargas_fase.append(sum(x2))

		indice_valor_minimo = suma_cargas_fase.index(min(suma_cargas_fase))

		lista_principal_balanceada[indice_valor_minimo].append(x1)
	##################################################################
	suma_cargas_fase = []
	for x in lista_principal_balanceada:
		suma_cargas_fase.append(sum(x))
	##################################################################
	carga_menor = min(suma_cargas_fase)
	carga_mayor = max(suma_cargas_fase)

	desbalance = carga_mayor - carga_menor
	desbalance_porcentaje = desbalance*100/carga_mayor

	return suma_cargas, promedio_cargas, lista_principal_balanceada, suma_cargas_fase, desbalance, desbalance_porcentaje

if __name__ == '__main__':
	a = 900
	b = 5000
	n_fases = 3
	elementos_fase = 15

	lista_principal = creador_random_fases(a, b, n_fases, elementos_fase)
	suma_cargas, promedio_cargas, lista_principal_balanceada, suma_cargas_fase, desbalance, desbalance_porcentaje = balanceador(lista_principal)


	print(f'''
	lista principal = {lista_principal} \n
	suma total de cargas = {suma_cargas} \n 
	promedio de cargas por fase = {promedio_cargas} \n
	lista principal balanceada = {lista_principal_balanceada} \n
	suma de cargas por fase = {suma_cargas_fase} \n
	desbalance = {desbalance} \n
	desbalance en porcentaje = {desbalance_porcentaje} \n
	''')
