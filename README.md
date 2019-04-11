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
Предположим, что неизвестные ![pic2](lab1/1.gif) связаны соотношением  
![pic3](lab1/CodeCogsEqn.gif)  
На прямом ходе прогонки находятся коэффициенты ![pic12](lab1/5.gif) , а на обратном неизвестные ![pic4](lab1/1.gif)  
Где в итоге неизвестные ![pic4](lab1/1.gif) выражаются как  
![pic5](lab1/2.gif), т.е.  
![pic6](lab1/3.gif)
### Результаты
Реализация метода прогонки прошла 8 тестов с матрицами размерности от 100 до 800  
![pic7](lab1/pic_sweep.png)  
## Решение СЛАУ методом Холецкого
Ах = f. Дана матрица А, где А - симметричная матрица с диагональным преобладанием, и вектор f. Найти х.  
### Алгоритм решения  
Матрица А разлагается в произведение ![pic11](lab1/formula/1.gif)  , где S - верхняя треугольная матрица. Решение системы сводится к последовательному решению двух систем  
![pic14](lab1/formula/2.gif)  

![pic15](lab1/formula/3.gif)  
![pic16](lab1/formula/5.gif)
### Результаты  
Реализация метода Холецкого прошла 5 тестов с матрицами размерности от 100 до 500  
![pic_chol](lab1/pic_chol.png)
![pic_chol1](lab1/pic_chol1.png)
