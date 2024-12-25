def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

# inner_function() - дает ошибку.
test_function()

# Вызов inner_function() вне test_function() дает следующую ошибку:

# Traceback (most recent call last):
#   File "E:\Libraries\Desktop\Учеба, типа\Python (Urban University)\projects\homework4\module_4_2.py", line 6, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

# inner_function() не видно в глобальном пространстве имен.