import math
from timeit import default_timer as timer


def f1(n):
    s = 0;
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0;
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0;
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0;
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0;
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


nn = [2000, 4000, 8000, 16000, 32000]



# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n

def pomiar_czasuf1():
    for n in nn:
        start = timer()
        f1(n)
        stop = timer()
        Tn = stop - start
        Fn=n
        print(n, Tn, Fn / Tn)

# pomiar_czasuf1()
# 2000 9.920000002239249e-05 20161290.318029623
# 4000 0.00017959999991035147 22271714.93316607
# 8000 0.00036709999994855025 21792427.134626027
# 16000 0.0007266000000072381 22020368.84095873
# 32000 0.001467100000127175 21811737.439319808

def pomiar_czasuf2():
    for n in nn:
        start = timer()
        f2(n)
        stop = timer()
        Tn = stop - start
        Fn=n
        print(n, Tn, Fn / Tn)

# pomiar_czasuf2()
# 2000 9.969999996428669e-05 20060180.548810586
# 4000 0.0001881000000594213 21265284.4164614
# 8000 0.0003711000001658249 21557531.652991712
# 16000 0.0007447999998930754 21482277.124458894
# 32000 0.001488999999992302 21490933.512535553


def pomiar_czasuf3():
    for n in nn:
        start = timer()
        f3(n)
        stop = timer()
        Tn = stop - start
        Fn=n*n
        print(n, Tn, Fn / Tn)

# pomiar_czasuf3()
# 2000 9.330000011686934e-05 235065043.32103193
# 4000 0.00019089999977950356 250723610.23536938
# 8000 0.0003820000001724111 271534749.29445314
# 16000 0.0007445999999617925 300097432.9385702
# 32000 0.0014912000001459091 321154169.16733336


def pomiar_czasuf4():
    for n in nn:
        start = timer()
        f4(n)
        stop = timer()
        Tn = stop - start
        Fn=n*math.log(n,2)
        print(n, Tn, Fn / Tn)

# pomiar_czasuf4()
# 2000 0.001406200000019453 15596336.629939398
# 4000 0.0030911999997442763 15483675.317872636
# 8000 0.006709899999805202 15458691.527490428
# 16000 0.014429399999698944 15485921.00567283
# 32000 0.03125580000005357 15322119.322121527

def pomiar_czasuf5():
    for n in nn:
        start = timer()
        f5(n)
        stop = timer()
        Tn = stop - start
        Fn=math.log(n,2)
        print(n, Tn, Fn / Tn)

pomiar_czasuf5()
# 2000 2.2999997781880666e-06 4767732.757479178
# 4000 1.500000053056283e-06 7977189.240948052
# 8000 1.2000000424450263e-06 10804819.855042687
# 16000 1.100000190490391e-06 12696165.332876898
# 32000 1.2999998943996616e-06 11512142.692575578