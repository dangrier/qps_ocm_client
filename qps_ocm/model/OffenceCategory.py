from enum import IntEnum


class OffenceCategory(IntEnum):
    HOMICIDE = 10
    OTHER_HOMICIDE = 20
    ASSAULT = 90
    ROBBERY = 150
    OTHER_OFFENCES_AGAINST_THE_PERSON = 180
    UNLAWFUL_ENTRY = 220
    ARSON = 280
    OTHER_PROPERTY_DAMAGE = 290
    UNLAWFUL_USE_OF_MOTOR_VEHICLE = 300
    OTHER_THEFT = 310
    FRAUD = 360
    HANDLING_STOLEN_GOODS = 400
    DRUG_OFFENCES = 460
    PROSTITUTION = 520
    LIQUOR = 610
    GAMING_RACING_AND_BETTING = 620
    TRESPASSING_AND_VAGRANCY = 640
    WEAPONS_ACT_OFFENCES = 645
    GOOD_ORDER_OFFENCES = 650
    STOCK_RELATED_OFFENCES = 710
    TRAFFIC_RELATED_OFFENCES = 740
    MISCELLANEOUS_OFFENCES = 790

    def __repr__(self) -> str:
        __offence_map = {
            OffenceCategory.HOMICIDE: "Homicide",
            OffenceCategory.OTHER_HOMICIDE: "Other Homicide",
            OffenceCategory.ASSAULT: "Assault",
            OffenceCategory.ROBBERY: "Robbery",
            OffenceCategory.OTHER_OFFENCES_AGAINST_THE_PERSON: "Other Offences Against the Person",
            OffenceCategory.UNLAWFUL_ENTRY: "Unlawful Entry",
            OffenceCategory.ARSON: "Arson",
            OffenceCategory.OTHER_PROPERTY_DAMAGE: "Other Property Damage",
            OffenceCategory.UNLAWFUL_USE_OF_MOTOR_VEHICLE: "Unlawful Use of Motor Vehicle",
            OffenceCategory.OTHER_THEFT: "Other Theft (excl. Unlawful Entry)",
            OffenceCategory.FRAUD: "Fraud",
            OffenceCategory.HANDLING_STOLEN_GOODS: "Handling Stolen Goods",
            OffenceCategory.DRUG_OFFENCES: "Drug Offences",
            OffenceCategory.PROSTITUTION: "Prostitution",
            OffenceCategory.LIQUOR: "Liquor (excl. Drunkenness)",
            OffenceCategory.GAMING_RACING_AND_BETTING: "Gaming Racing & Betting Offences",
            OffenceCategory.TRESPASSING_AND_VAGRANCY: "Trespassing & Vagrancy",
            OffenceCategory.WEAPONS_ACT_OFFENCES: "Weapons Act Offences",
            OffenceCategory.GOOD_ORDER_OFFENCES: "Good Order Offences",
            OffenceCategory.STOCK_RELATED_OFFENCES: "Stock Related Offences",
            OffenceCategory.TRAFFIC_RELATED_OFFENCES: "Traffic & Related Offences",
            OffenceCategory.MISCELLANEOUS_OFFENCES: "Miscellaneous Offences",
        }
        return __offence_map.get(self) or "Unknown"

    def __str__(self) -> str:
        return self.__repr__()
