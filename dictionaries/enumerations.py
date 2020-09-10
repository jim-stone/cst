from enum import Enum
from collections import OrderedDict


class Programme (Enum):
    POPC = 'Program Operacyjny Polska Cyfrowa'
    POIR = 'Program Operacyjny Inteligentny Rozwój'
    KPOD = 'Krajowy Program Odbudowy'
    FSTR = 'Fundusz Sprawiedliwej Transformacji'

    @classmethod
    def choices(cls):
        return [(key.name, key.value) for key in cls]

    @classmethod
    def to_dict(cls):
        temp_dict = {key.name: key.value for key in cls}
        return OrderedDict(sorted(temp_dict.items(), key=lambda item: item[0]))


class InstitutionType(Enum):
    KOOR = 'Koordynująca'
    WDRA = 'Wdrażająca'
    BENE = 'Beneficjent'


class InstitutionSubtype(Enum):
    KOOR = 'Instytucja Koordynująca'
    ZARZ = 'Instytucja Zarządzająca'
    POSR = 'Instytucja Pośrednicząca'
    WDRA = 'Instytucja Wdrażająca'
    BENE = 'Beneficjent'
    OBSE = 'Obserwator'
