num_empleado = int(input('Ingrese número de empleados: '))
contador = 0

nombres = []
horas = []
tarifas = []
pago_semanal = []

while (contador < num_empleado):
    nombre_empleado = str(input('Ingrese nombre de empleado: '))
    horas_trabajadas = int(input('Ingrese número de horas trabajadas: '))
    paga_hora = float(input('Ingrese tarifa por hora: '))

    if horas_trabajadas <= 35:
        paga = paga_hora * horas_trabajadas
    else:
        paga = paga_hora * 35 + paga_hora * (horas_trabajadas-35) * 1.5

    nombres.append(nombre_empleado)
    horas.append(horas_trabajadas)
    tarifas.append(paga_hora)
    pago_semanal.append(paga)

    contador += 1

for a, b, c, d in zip(nombres, horas, tarifas, pago_semanal):
    print(a, b, c, d)
