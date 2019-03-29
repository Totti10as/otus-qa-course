# Otus - > QA Automation Course in Python

### Running Tests 
_________________
To run tests from the __tests project directory__, run one of the following commands:


- python -m pytest test_um_pytest.py # Можно запустить так
- py.test test_um_pytest.py # Или так
- python -m pytest -v test_um_pytest.py # Или так с расширенным выводом
- py.test -v test_um_pytest.py # А еще вот так
- pytest testing/ # Запуск тестов в директории
- pytest test_mod.py::test_func # Запуск отдельного теста в модуле test_mod.py
- pytest test_mod.py::TestClass::test_method # Запуск теста из класса
- pytest -m slow # Запуск промаркированных тестов
