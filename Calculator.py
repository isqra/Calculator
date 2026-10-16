import numpy as np

a = np.array(list(map(int, input("Введите вектор a: ").split())))
b = np.array(list(map(int, input("Введите вектор b: ").split())))

print("Сумма:", a + b)
print("Скалярное произведение: ", a @ b)

if len(a) == 3 and len(b) == 3:
    print("Векторное произведение для 3D-векторов:", np.cross(a, b))

if len(a) == 2:
    cross = a[0] * b[1] - a[1] * b[0]
    print("Векторное произведение 2D-векторов: ", cross)

cos = (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))
print("косинус: ", cos)
