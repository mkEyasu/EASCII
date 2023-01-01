from EASCII import Ealpha

eth = Ealpha()
print(eth.eord("ኢትዮጵያ፡ ሀገሬ", space=True))
print(eth.eord("ኢትዮጵያ፡ ሀገሬ", space=False))  # <--- the default value is False
print(eth.echr(135, 98, 193, 246, 190, 0, 279, 0, 1, 209, 42, space=False))
print(eth.echr(135, 98, 193, 246, 190, 0, 279, 0, 1, 209, 42, space=False))    # <--- the default value is False
print(eth.__doc__)
