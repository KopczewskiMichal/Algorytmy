from timeit import default_timer as timer
import math
# lewy syn A[i] jest w A[2i+1]
# - prawy syn A[i] jest w A[2i+2]
# - ojciec A[i] jest w A[⎣(i-1)/2⎦]
import random
def heapify(A, heapSize, i):
    l = 2 * i + 1  # lewy syn
    r = 2 * i + 2  # prawy syn
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, heapSize, largest)
    return A


def buildHeap(A):
    heapSize = len(A)
    k = int((len(A) - 2) / 2)  # ojciec ostatniego węzła
    for i in range(k, -1, -1):
        heapify(A, heapSize, i)
    return A


def heapSort(A):
    A = buildHeap(A)
    heapSize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[heapSize - 1] = A[heapSize - 1], A[0]
        heapSize -= 1
        heapify(A, heapSize, 0)
    return A


# list = [random.randint(1, 1000) for i in range(200)]
# B = heapSort(list)
# print(B)


def prettyPrint(n, time, divided):
    z = 30
    result = str(n) + "  " + str(time)
    if len(result) < z:
        result += (' ' * (z - len(result)))
    print(result, divided)


def pomiar_czasu_rosnące(nn):
    for n in nn:
        list = [i for i in range(n)]
        start = timer()
        heapSort(list)
        stop = timer()
        Tn = stop - start
        Fn = n * math.log(n)
        prettyPrint(n, Tn, Fn / Tn)

def pomiar_czasu_identyczne(nn):
    for n in nn:
        list = [7 for i in range(n)]
        start = timer()
        heapSort(list)
        stop = timer()
        Tn = stop - start
        Fn = n * math.log(n)
        prettyPrint(n, Tn, Fn / Tn)

def pomiar_czasu_malejące(nn):
    for n in nn:
        list = [i for i in range(n, -1, -1)]
        start = timer()
        heapSort(list)
        stop = timer()
        Tn = stop - start
        Fn = n * math.log(n)
        prettyPrint(n, Tn, Fn / Tn)


def podsumowanieTestów(nn):
    # nn = [100, 200, 500, 1000, 5000, 10000]
    print("Poniżej przypadek idealny, tablica już posortowana")
    pomiar_czasu_rosnące(nn)
    print("\nPoniżej jeśli damy tablicę identycznych liczb")
    pomiar_czasu_identyczne(nn)
    print("\nPrzypadek tablicy wejściowej ułożonej malejąco")
    pomiar_czasu_malejące(nn)


podsumowanieTestów([100, 200, 500, 1000, 5000, 10000, 50000])
