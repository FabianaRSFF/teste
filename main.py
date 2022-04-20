from calculadora import soma

#  Geralmente os assertions são utilizados para comunicação
#  entre desenvolvedores, dificilmente chegarão ao consumidor 
#  final. Muito útil para o desenvolvimento de programas em ´
#  plataformas open source.


try:
    print(soma('30' , 40, 10))
except AssertionError as e:
    print(f'Conta inválida:{e}')