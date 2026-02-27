a = float(input('valor a pagar: '))

if a < 0 :
  print('El valor a pagar no puede ser negativo')

if a > 1000 :
  descuento = a * 0.20
  valor_a_pagar = a - descuento
  print(f'El monto a pagar es {valor_a_pagar}')

elif a >= 500 :
  descuento = a * 0.10
  valor_a_pagar = a - descuento
  print(f'El monto a pagar es {valor_a_pagar}')

elif a > 0 :
  print('No se aplic}a descuento')
  print(f'El monto a pagar es {a}')
