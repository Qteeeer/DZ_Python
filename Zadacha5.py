# Напишите программу, которая принимает на вход 
# координаты двух точек и находит расстояние между 
# ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

frstPoint = list(
    input("Введите координаты первой точки через пробел ").split())
scndPoint = list(
    input("Введите координаты первой точки через пробел ").split())
print(frstPoint[1])
print(scndPoint)


def distance(fP, scdP):
    if len(fP) != len(scdP):
        print("Точки в разных измерениях")
    else:
        dist = float(0)
        for i in range(len(fP)):
            dist += (int(scdP[i])-int(fP[i]))**2
        print(f"Прямое расстояние между точками {round(dist**(1/2),2)}")


distance(frstPoint, scndPoint)