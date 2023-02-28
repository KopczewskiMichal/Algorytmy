import random
from timeit import default_timer as timer


def funkcja1(matrix):  # algotytm jak na tablicy podczas zajęć, złożoność czasowa O(n^6)
    n = len(matrix)
    max_area = 0
    for xstart in range(n):
        for ystart in range(n):
            for xend in range(xstart, n):
                for yend in range(ystart, n):
                    correct_submatrix = True
                    for act_y in range(ystart, yend + 1):
                        sub_row = matrix[act_y][xstart: xend + 1]
                        if 0 in sub_row:
                            correct_submatrix = False
                            break
                    if correct_submatrix == True and ((xend - xstart + 1) * (yend - ystart + 1) > max_area):
                        max_area = (xend - xstart + 1) * (yend - ystart + 1)
    return (max_area)


def test_funkcja1(n):
    A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
    for row in A:
        print(row)
    print("Wielkość największej podmacierzy wynosi:   ", funkcja1(A))


def pomiar_czasu_f1(nn):
    for n in nn:
        A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
        time_start = timer()
        b = funkcja1(A)
        time_stop = timer()
        Tn = time_stop - time_start
        Fn = n ** 6
        print(n, Tn, Fn / Tn)

# test_funkcja1(5)
# pomiar_czasu_f1([5, 10, 20, 40, 60])

def funkcja2(matrix):   # złożoność czasowa O(n^2)
    n = len(matrix)
    dynamic = [0 for i in range(n)]
    max_area = 0
    for row in matrix:
        for i in range(n):
            if row[i] == 0:
                dynamic[i] = 0
            else:
                dynamic[i] += 1

        for start in range(n):
            if dynamic[start] != 0:
                end = start + 1
                while end < (n + 1) and dynamic[end - 1] != 0:
                    if (min(dynamic[start : end]) * (end - start)) > max_area:
                        max_area = min(dynamic[start : end]) * (end - start)
                    end += 1
    return max_area


def test_funkcja1(n):
    A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
    for row in A:
        print(row)
    print("Wielkość największej podmacierzy wynosi:   ", funkcja2(A))


def pomiar_czasu_f2(nn):
    for n in nn:
        A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
        time_start = timer()
        b = funkcja2(A)
        time_stop = timer()
        Tn = time_stop - time_start
        Fn = n ** 2
        print(n, Tn, Fn / Tn)

# pomiar_czasu_f2([5,50,100,200,500, 1000, 2000])


def test_zgodności_wyników(n, iletestow):
    for z in range(iletestow):
        A = [[random.randint(0, 1) for i in range(n)] for j in range(n)]
        # for row in A:
        #     print(row)
        wynik1 = funkcja1(A)
        wynik2 = funkcja2(A)
        if wynik1 > maks:
            maks = wynik1
        # print(f"Wielkość największej podmacierzy policzona sposobem:\n \
        #       pierwszym: {wynik1}\n \
        #       drugim: {wynik2}")
        if wynik1 != wynik2:
            print("Jedna z funkcji działa błędnie !!!")
            break
        # else:
        #     print(f"test {z} zakończył się pozytywnie\n")



# test_zgodności_wyników(20, 100)