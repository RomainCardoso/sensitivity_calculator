"""SENS CALCULATOR/CONVERTER (SOURCE ENGINE, OVERWATCH, VALORANT CURRENTLY SUPPORTED)"""


"""games m_yaw scaling"""

source_yaw = 0.022
ow_yaw = 0.0066
valorant_yaw = 0.06996


# get cm/360 --> (360 / (m_yaw * DPI * windows sens multiplier * initial_sens))*2.54

def source_sens_calc():

    dpi = int(input("what is your mouse DPI ?"))
    source_sens = float(input("enter your current SOURCE sens: "))
    cm360 = (360 / (source_yaw * dpi * 1 * source_sens))*2.54
    print("your cm/360 is: ", cm360)


def overwatch_sens_calc():

    dpi = int(input("what is your mouse DPI ?"))
    overwatch_sens = float(input("enter your current OVERWATCH sens: "))
    cm360 = (360 / (ow_yaw * dpi * 1 * overwatch_sens))*2.54
    print("your cm/360 is: ", cm360)


def valorant_sens_calc():

    dpi = int(input("what is your mouse DPI ?"))
    valorant_sens = float(input("enter your current VALORANT sens: "))
    cm360 = (360 / (valorant_yaw * dpi * 1 * valorant_sens))*2.54
    print("your cm/360 is: ", cm360)


def source_to_valorant():

    dpi = int(input("what is your mouse DPI ?"))
    csgo_sens = float(input("enter your current CSGO sens: "))
    output = csgo_sens / 3.18
    cm360 = (360 / (valorant_yaw * dpi * 1 * output))*2.54
    print("your VALORANT sens would be: ", output)
    print("your cm/360 is: ", cm360)


def source_to_overwatch():

    dpi = int(input("what is your mouse DPI ?"))
    csgo_sens = float(input("enter your current CSGO sens: "))
    output = csgo_sens * 100 / 30
    cm360 = (360 / (ow_yaw * dpi * 1 * output))*2.54
    print("your OVERWATCH sens would be: ", output)
    print("your cm/360 is: ", cm360)


def valorant_to_source():

    dpi = int(input("what is your mouse DPI ?"))
    valorant_sens = float(input("enter your current VALORANT sens: "))
    output = valorant_sens * 3.18
    cm360 = (360 / (source_yaw * dpi * 1 * output))*2.54
    print("your CSGO sens would be: ", output)
    print("your cm/360 is: ", cm360)


def valorant_to_ow():

    dpi = int(input("what is your mouse DPI ?"))
    valorant_sens = float(input("enter your current VALORANT sens: "))
    output = valorant_sens * 3.18 * 100 / 30
    cm360 = (360 / (ow_yaw * dpi * 1 * output))*2.54
    print("your OVERWATCH sens would be: ", output)
    print("your cm/360 is: ", cm360)


def ow_to_source():

    dpi = int(input("what is your mouse DPI ?"))
    ow_sens = float(input("enter your current OVERWATCH sens: "))
    output = ow_sens / 100 * 30
    cm360 = (360 / (source_yaw * dpi * 1 * output))*2.54
    print("your CSGO sens would be: ", output)
    print("your cm/360 is: ", cm360)


def ow_to_valorant():

    dpi = int(input("what is your mouse DPI ?"))
    ow_sens = float(input("enter your current OVERWATCH sens: "))
    output = ow_sens / 3.18 / 100 * 30
    cm360 = (360 / (valorant_yaw * dpi * 1 * output))*2.54
    print("your VALORANT sens would be: ", output)
    print("your cm/360 is: ", cm360)


def cmrev_source():

    dpi = int(input("enter your mouse dpi: "))
    desired_sens = float(input("enter your desired cm/rev: "))
    cm360 = (360 / (source_yaw * dpi * 1 * desired_sens))*2.54
    print("your SOURCE ENGINE sensitivity would be: ", cm360)


def cmrev_overwatch():

    dpi = int(input("enter your mouse dpi: "))
    overwatch_sens = float(input("enter your desired cm/rev: "))
    cm360 = (360 / (ow_yaw * dpi * 1 * overwatch_sens))*2.54
    print("your OVERWATCH sensitivity would be: ", cm360)


def cmrev_valorant():

    dpi = int(input("enter your mouse dpi: "))
    valorant_sens = float(input("enter your desired cm/rev: "))
    cm360 = (360 / (valorant_yaw * dpi * 1 * valorant_sens))*2.54
    print("your VALORANT sensitivity would be: ", cm360)


calc_convert = int(input("Choose between options and press the according number: \n\n1- Tell me my cm/rev from listed games \n2- Convert my sensitivity from listed games\n3- cm/rev to ingame sens\n"))

if calc_convert == 1:
    default_game = int(input("choose base game and press the according number: \n\n1- SOURCE ENGINE (CSGO, Quake, TF2) \n2- VALORANT \n3- OVERWATCH\n\n"))
    if default_game == 1:
        source_sens_calc()
    elif default_game == 2:
        valorant_sens_calc()
    elif default_game == 3:
        overwatch_sens_calc()
elif calc_convert == 2:
    default_game = int(input("choose base game and press the according number: \n\n1- SOURCE ENGINE (CSGO, Quake, TF2) \n2- VALORANT \n3- OVERWATCH\n\n"))
    converted_game = int(input("choose game to convert to: \n\n1- SOURCE ENGINE (CSGO, Quake, TF2, etc...) \n2- VALORANT \n3- OVERWATCH\n\n"))
    if default_game == 1 and converted_game == 2:
        source_to_valorant()
    elif default_game == 1 and converted_game == 3:
        source_to_overwatch()
    elif default_game == 2 and converted_game == 1:
        valorant_to_source()
    elif default_game == 2 and converted_game == 3:
        valorant_to_ow()
    elif default_game == 3 and converted_game == 1:
        ow_to_source()
    elif default_game == 3 and converted_game == 2:
        ow_to_valorant()
    while default_game == converted_game:
        repeat = "\n\nERROR: You cannot convert using the same base and converted game, try again ! \n\n"
        print(repeat.upper())

        default_game = int(input("choose base game and press the according number: \n\n 1 SOURCE ENGINE (CSGO, Quake, TF2) \n 2 VALORANT \n 3 OVERWATCH\n\n"))
        converted_game = int(input("choose game to convert to: \n\n1- SOURCE ENGINE (CSGO, Quake, TF2) \n2- VALORANT \n3- OVERWATCH\n\n"))

        if default_game == 1 and converted_game == 2:
            source_to_valorant()
        elif default_game == 1 and converted_game == 3:
            source_to_overwatch()
        elif default_game == 2 and converted_game == 1:
            valorant_to_source()
        elif default_game == 2 and converted_game == 3:
            valorant_to_ow()
        elif default_game == 3 and converted_game == 1:
            ow_to_source()
        elif default_game == 3 and converted_game == 2:
            ow_to_valorant()

if calc_convert == 3:
    base_game = int(input("choose game to convert to: \n\n1- SOURCE ENGINE GAME(CS, Quake, TF2) \n2- OVERWATCH\n3- VALORANT\n\n"))
    if base_game == 1:
        cmrev_source()
    elif base_game == 2:
        cmrev_overwatch()
    elif base_game == 3:
        cmrev_valorant()
