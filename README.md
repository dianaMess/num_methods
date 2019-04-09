# num_methods
# First Lab
## Решение СЛАУ методом Гаусса
Ax = f. Дана матрица A с диагональным преобладанием, и вектор f. Найти x.
### Алгоритм решения
Представим А, как А = LU, где L - нижнетреугольная, U - верхнетреугольная матрица.  
Задача решается в два хода:  
- Прямой ход: привести матрицу к верхнетреугольному виду элементарными преобразованиеми строк.  
- Обратный ход: привести матрицу к диагональному виду элементарными преобразованиями строк.  
### Результаты  
Реализация метода Гаусса прошла 5 тестов с матрицами размерности от 100 до 500  
Также предоставлен график зависимости время выполнения программы от размерности матрицы:  
![pic](lab1/pic_gauss.png)
## Решение СЛАУ методом прогонки  
Ах = f. Дана матрица A, где А - трехдиагональная матрица с диагональным преобладанием, и вектор f. Найти x.
### Алгоритм решения  
Предположим, что неизвестные ----- связаны соотношением  
![pic1](lab1/CodeCogsEqn.gif)
