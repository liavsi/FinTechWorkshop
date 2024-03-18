import numpy as np

class Table_Data_Object:
    def __init__(self, Transaction_ID, Name, Price, Side, Timestamp, Volume, Order_Executed, Target):
        self._Transaction_ID = Transaction_ID
        self._Name = Name
        self._Price = Price
        self._Side = Side
        self._Timestamp = Timestamp
        self._Volume = Volume
        self._Order_Executed = Order_Executed
        self._Target = Target

    def __array__(self) -> np.ndarray:
        return np.array([self._Transaction_ID, self._Name, self._Price, self._Side, self._Timestamp, self._Volume, self._Order_Executed, self._Target])

    @property
    def Transaction_ID(self):
        return self._Transaction_ID

    @Transaction_ID.setter
    def Transaction_ID(self, value):
        self._Transaction_ID = value

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, value):
        self._Name = value

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Side(self):
        return self._Side

    @Side.setter
    def Side(self, value):
        self._Side = value

    @property
    def Timestamp(self):
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, value):
        self._Timestamp = value

    @property
    def Order_Executed(self):
        return self._Order_Executed

    @Order_Executed.setter
    def Order_Executed(self, value):
        self._Order_Executed = value

    @property
    def Target(self):
        return self._Target

    @Target.setter
    def Target(self, value):
        self._Target = value

    @property
    def Volume(self):
        return self._Volume

    @Volume.setter
    def Volume(self, value):
        self._Volume = value
