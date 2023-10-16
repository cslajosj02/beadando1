from __future__ import annotations

from functools import total_ordering


@total_ordering
class phone:
    mf: str
    _tp: str
    _rl: int

    def __init__(self,gyarto,tipus,ev=2022) -> None:
        super().__init__()
        self._rl=ev
        self._tp=tipus
        self.mf=gyarto


    @property
    def year(self)->int:
        return self._rl

    @year.setter
    def year(self, value)->None:
        self._rl=value
    @property
    def type(self)->str:
        return self._tp

    @type.setter
    def type(self, value)->None:
        self._tp=value

    def __repr__(self) -> str:
        return f'{super().__repr__()}, {self.mf}, {self._tp}, {self._rl}'

    def __str__(self) -> str:
        return f'{self.mf} // {self._tp} ({self._rl})'

    def __eq__(self, o: object) -> bool:
        super().__eq__(o)
        if self._rl==o._rl and self._tp==o._tp and self.mf==o.mf:
            return True
        return False
    def __lt__(self, other: object)->bool:

        if self._tp<other._tp and -self._rl < -other._rl and self.mf<other.mf:
            return True
        return False
    @staticmethod
    def back(list: list[phone],y:int)->list[phone]:
        listaout=[]
        for device in list:
            if device._rl<y:
                listaout.append(device)
        return listaout

class sphone(phone):
    _camera: str

    def __init__(self, gyarto, tipus, ev,camera) -> None:
        super().__init__(gyarto, tipus, ev)
        self._camera=camera
    @property
    def cameraout(self)->str:
        return self._camera

    def __repr__(self) -> str:
        return f'{super().__repr__()}, {self._camera}'

    def __str__(self) -> str:
        return f'{super().__str__()}: {self._camera}'


















