class Tabung():
    def __init__(self):
        self.__jarijaritabung = None
        self.__tinggitabung = None
    
    @property
    def jarijaritabung(self):
        return self.__jarijaritabung
    
    @jarijaritabung.setter
    def jarijaritabung(self, value):
        self.__jarijaritabung = value

    @property
    def tinggitabung(self):
        return self.__tinggitabung

    @tinggitabung.setter
    def tinggitabung(self, value):
        self.__tinggitabung = value

    def LuasPermukaanTabung(self):
        LPT = 2 * 3.14 * self.__jarijaritabung * (self.__jarijaritabung + self.__tinggitabung)
        return LPT

    def VolumeTabung(self):
        VT = 3.14 * self.__jarijaritabung * self.__jarijaritabung * self.__tinggitabung
        return VT