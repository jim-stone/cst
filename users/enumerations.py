from enum import Enum


class Application(Enum):
    ADMIN = 'Administracja'
    SZOOP = 'eSZOOP'
    KONT = 'eKONTROLE'
    WOD = 'WOD'
    BK = 'BK'
    SKAN = 'SKANER'
    SL = 'SL2014'
    SRHD = 'SRHD2014'


class InstitutionType(Enum):
    KOOR = 'Koordynująca'
    WDRA = 'Wdrażająca'
    BENE = 'Beneficjent'

    @classmethod
    def to_tuple(cls):
        return tuple((member.name, member.value) for member in cls)


class InstitutionSubtype(Enum):
    KOOR = 'Instytucja Koordynująca'
    ZARZ = 'Instytucja Zarządzająca'
    POSR = 'Instytucja Pośrednicząca'
    WDRA = 'Instytucja Wdrażająca'
    BENE = 'Beneficjent'
    OBSE = 'Obserwator'
