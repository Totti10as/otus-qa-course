# Otus - > QA Automation Course in Python


## Runing tests


To run tests from the __tests project directory__, run one of the following commands:


- python -m pytest test_um_pytest.py # Можно запустить так
- py.test test_um_pytest.py # Или так
- python -m pytest -v test_um_pytest.py # Или так с расширенным выводом
- py.test -v test_um_pytest.py # А еще вот так
- pytest testing/ # Запуск тестов в директории
- pytest test_mod.py::test_func # Запуск отдельного теста в модуле test_mod.py
- pytest test_mod.py::TestClass::test_method # Запуск теста из класса
- pytest -m slow # Запуск промаркированных тестов

To run tests with additional options:


- pytest --version   # shows where pytest was imported from
- pytest --fixtures  # Список фикстур
- pytest -h | --help # Помощь и опции командной строки
- pytest -x            # Остановить тесты после первого фейла
- pytest --maxfail=2    # Остановить тесты после двух неудачных тестов
- pytest -x --pdb   # Включить PDB на первом падении после этого завершить тестовую сессию
- pytest --pdb --maxfail=3  # Включать PDB превые три падения тестов
- pytest -–collect-only # Список тестов






__Use the following link to edit markup the README file__ : 
[Basic writing and formatting syntax](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
