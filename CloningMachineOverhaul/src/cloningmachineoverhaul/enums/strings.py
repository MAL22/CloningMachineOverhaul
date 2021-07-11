import enum


class StringTable(enum.Int):
    DEFAULT = 0xECD09801
    AUTOMATIC = 0x576B92FC
    NEITHER = 0

    # STBLs for configuration menu titles
    CMO_RELBIT_MENU_TITLE = 0xD588A7E2
    CMO_GENDER_MENU_TITLE = 0xF95F0C33
    CMO_BODY_SEX_MENU_TITLE = 0x5355410D
    CMO_AGE_MENU_TITLE = 0x13262487
    CMO_FERTILITY_MENU_TITLE = 0x743AFEC4
    CMO_GENITALIA_MENU_TITLE = 0xD1569BC2
    CMO_CLOTHING_PREF_MENU_TITLE = 0xCBD56826
    CMO_DNA_PICKER_DIALOG_TITLE = 0x0E556257
    CMO_RENAME_SIM_DIALOG_TITLE = 0x3968E751

    # STBLs for configuration menu descriptions
    CMO_BODY_SEX_MENU_DESC = 0xCF825E4C
    CMO_AGE_MENU_DESC = 0x26C109D0
    CMO_GENDER_MENU_DESC = 0x39068824
    CMO_RELBIT_MENU_DESC = 0xB65E5700
    CMO_FERTILITY_MENU_DESC = 0x07F12763
    CMO_GENITALIA_MENU_DESC = 0xA773AF75
    CMO_CLOTHING_PREF_MENU_DESC = 0x76D194A1
    CMO_DNA_PICKER_DIALOG_DESC = 0xC0529518
    CMO_RENAME_SIM_DIALOG_DESC = 0x9E93258A

    # Interaction STBLs
    CLONE_SETTINGS = 0x5E5A88DA
    AGE = 0x41B29A5B
    GENDER = 0x693D1836
    SEX = 0x752EE201
    FERTILITY = 0xE1F3ED25
    GENITALIA = 0x814746AB

    # STBLs for life stages
    BABY = 0x150A4F1F
    TODDLER = 0x00F6323E
    CHILD = 0x4E7EBFE5
    TEEN = 0x45865C27
    YOUNGADULT = 0x7A68574A
    ADULT = 0xA95B08A9
    ELDER = 0xF7AFE1E1

    # STBLs for genders
    MALE = 0x19E792E4
    FEMALE = 0x16B2C1D5

    # STBLs for relationship bits
    RELBIT_SIBLING = 0x9536E86F
    RELBIT_OFFSPRING = 0x9BE2DBA5

    # STBLs for voice types
    VOICE_MELODIC = 0x4AAE3F32
    VOICE_SWEET = 0x289FA075
    VOICE_LILTED = 0xA59624F2
    VOICE_CLEAR = 0x56AD31D9
    VOICE_WARM = 0x1CC8C5D4
    VOICE_BRASH = 0x747E6B81