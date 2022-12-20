"""Документация модуля. Описывает работу классов и функций.
Размещается в верхней части файла (начиная с первой строки).
"""
# Импортируйте модуль inspect.

import inspect


def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки
        документации.
        """
        ...
 

print('Без применения cleandoc:')
print(Test.first.__doc__)
print('С применением cleandoc:')
print(inspect.cleandoc(Test.first.__doc__))
# Выведите докстринг, используя метод cleandoc().
