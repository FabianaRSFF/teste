from typing import List, Union, Tuple, Dict, Any, NewType, Callable, Sequence, Iterable


# Primitivos
numero: int = 10
flutuante: float = 10.8
string: str = 'Fabiana'
booleano: bool = False

# Sequências
lista: List[int] = [1, 2, 3, 4]
lista_str_int: List[Union[int, str]] = [1, 3, 5, 'Fabi', 'Luiz']
tupla: Tuple[int, int, int, int, str] = (1, 2, 3, 4, 'Fabi')

# Dicionários e conjuntos


# Meu tipo
Meu_dict = Dict[str, Union[str, int, List[int]]] # Alias (apelido)
pessoa: Dict[str, Union[str, int]] = {'nome': 'Luiz Fernando', 'sobrenome': 'Mistério'}
pessoa2: Dict[str, Any] = {'nome': 'Luiz Fernando', 'sobrenome': 'Mistério', 'idade': 57}
pessoa3: Dict[str, Union[str, int, List[int]]] = {'nome': 'Fabiana', 'sobrenome': 'Ladeira', 'idade': 44, 'l': [1, 2, 3]}
pessoa4: Meu_dict = {'nome': 'Fabiana', 'sobrenome': 'Ladeira', 'idade': 44, 'l': [1, 2, 3]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(123456)

def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao

def fala_oi():
    print('oi')

retorna_funcao(fala_oi)()

def retorna_funcao2(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x=10, y=20):
    return x + y

print(retorna_funcao2(soma)(10, 20))


class Pessoa:
    def __init__(self, nome:str, sobrenome:str, idade:int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando.... ')



def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]
print(iterar((1, 2, 3)))
print(iterar([1, 2, 3, 4]))


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]
print(iterar2((1, 2, 3)))
print(iterar2([1, 2, 3, 4]))