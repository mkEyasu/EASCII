# EASCII
    Usage:

    NOTE: The Default ``space``  value is False
    *
        from EASCII import Ealpha
        eth = Ealpha()
        print(eth.eord("ኢትዮጵያ", space=True))
        135 98 193 246 190
    *
        print(eth.eord("ኢትዮጵያ"))
        13598193246190
    *
        print(eth.eord("ኢትዮጵያ ሀገሬ"))
        13598193246190 120942
    *
        print(eth.eord("ኢትዮጵያ ሀገሬ", space=True))
        135 98 193 246 190 0 1 209 42
    #################################################################
    *
        from EASCII import Ealpha
        eth = Ealpha()
        print(eth.echr(1))
        ሀ
    *
        print(eth.echr(135, 98, 193, 246, 190, 0, 1, 209, 42))
        ኢትዮጵያ ሀገሬ
    *
        print(eth.echr(135, 98, 193, 246, 190, 1, 209, 42))
        ኢትዮጵያሀገሬ
    *
        print(eth.echr(135, 98, 193, 246, 190, 1, 209, 42, space=True))
        ኢ ት ዮ ጵ ያ  ሀ ገ ሬ
    

Process finished with exit code 0
