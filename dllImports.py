import ctypes

lib = ctypes.cdll.LoadLibrary("testLibrary.dll")




'''

func = lib['_ZN11TestLibrary4calcEv']  #my func is double myFunc(double);
func.restype = ctypes.c_int

value = func()
print(value)

'''




