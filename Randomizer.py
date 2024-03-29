from audioop import reverse
from msilib.schema import CheckBox
from telnetlib import STATUS
from tkinter import *
from tkinter import messagebox
import random
from functools import reduce
from tkinter import filedialog

root = Tk()
root.title("Super Monkey Ball Banana Mania Randomizer!")
def Run():
    Success = Label(root, text="Penis")

#Create the column of World Selections
WorldLabel = Label(root, text="World Selection")

W1 = IntVar()
W2 = IntVar()
W3 = IntVar()
W4 = IntVar()
W5 = IntVar()
W6 = IntVar()
W7 = IntVar()
W8 = IntVar()
W9 = IntVar()
W10 = IntVar()

World1 = Checkbutton(root, text="World 1", variable=W1, onvalue=1, offvalue=0)
World2 = Checkbutton(root, text="World 2", variable=W2, onvalue=1, offvalue=0)
World3 = Checkbutton(root, text="World 3", variable=W3, onvalue=1, offvalue=0)
World4 = Checkbutton(root, text="World 4", variable=W4, onvalue=1, offvalue=0)
World5 = Checkbutton(root, text="World 5", variable=W5, onvalue=1, offvalue=0)
World6 = Checkbutton(root, text="World 6", variable=W6, onvalue=1, offvalue=0)
World7 = Checkbutton(root, text="World 7", variable=W7, onvalue=1, offvalue=0)
World8 = Checkbutton(root, text="World 8", variable=W8, onvalue=1, offvalue=0)
World9 = Checkbutton(root, text="World 9", variable=W9, onvalue=1, offvalue=0)
World10 = Checkbutton(root, text="World 10", variable=W10, onvalue=1, offvalue=0)

WorldLabel.grid(row = 0, column = 0)
World1.grid(row = 1, column = 0)
World2.grid(row = 2, column = 0)
World3.grid(row = 3, column = 0)
World4.grid(row = 4, column = 0)
World5.grid(row = 5, column = 0)
World6.grid(row = 6, column = 0)
World7.grid(row = 7, column = 0)
World8.grid(row = 8, column = 0)
World9.grid(row = 9, column = 0)
World10.grid(row = 10, column = 0)

#Create the Level Selections

LevelLabel = Label(root, text="Level Selection")

SMB1C = IntVar()
SMB1N = IntVar()
SMB1E = IntVar()
SMB1M = IntVar()
SMB2C = IntVar()
SMB2N = IntVar()
SMB2E = IntVar()
SMB2M = IntVar()
DX = IntVar()
Reverse = IntVar()
OGStageBool = IntVar()
Unused = IntVar()

SMB1Casual = Checkbutton(root, text="SMB1 Casual", variable=SMB1C, onvalue=1, offvalue=0)
SMB1Normal = Checkbutton(root, text="SMB1 Normal", variable=SMB1N, onvalue=1, offvalue=0)
SMB1Expert = Checkbutton(root, text="SMB1 Expert", variable=SMB1E, onvalue=1, offvalue=0)
SMB1Master = Checkbutton(root, text="SMB1 Master", variable=SMB1M, onvalue=1, offvalue=0)
SMB2Casual = Checkbutton(root, text="SMB2 Casual", variable=SMB2C, onvalue=1, offvalue=0)
SMB2Normal = Checkbutton(root, text="SMB2 Normal", variable=SMB2N, onvalue=1, offvalue=0)
SMB2Expert = Checkbutton(root, text="SMB2 Expert", variable=SMB2E, onvalue=1, offvalue=0)
SMB2Master = Checkbutton(root, text="SMB2 Master", variable=SMB2M, onvalue=1, offvalue=0)
DXMode = Checkbutton(root, text="DX Mode", variable=DX, onvalue=1, offvalue=0)
ReverseMode = Checkbutton(root, text="Reverse Mode", variable=Reverse, onvalue=1, offvalue=0)
OGStage = Checkbutton(root, text="OG Stage Mode", variable=OGStageBool, onvalue=1, offvalue=0)
UnusedStages = Checkbutton(root, text="Unused Stages", variable=Unused, onvalue=1, offvalue=0)

LevelLabel.grid(row = 0, column = 1)
SMB1Casual.grid(row = 1, column = 1)
SMB1Normal.grid(row = 2, column = 1)
SMB1Expert.grid(row = 3, column = 1)
SMB1Master.grid(row = 4, column = 1)
SMB2Casual.grid(row = 5, column = 1)
SMB2Normal.grid(row = 6, column = 1)
SMB2Expert.grid(row = 7, column = 1)
SMB2Master.grid(row = 8, column = 1)
DXMode.grid(row = 9, column = 1)
ReverseMode.grid(row = 10, column = 1)
OGStage.grid(row = 11, column = 1)
UnusedStages.grid(row = 12, column = 1)

#Add in Misc Randomization Elements

# Enable/Disable Randomization
GreenBool = IntVar()
RedBool = IntVar()
CountBool = IntVar()
DuplicateBool = IntVar()
BonusBool = IntVar()
ExtrasBool = IntVar()

def GreenBoolCheck():
    if GreenBool.get() == 0:
        GreenMin.config(state=DISABLED)
        GreenMax.config(state=DISABLED)
    else:
        GreenMin.config(state=NORMAL)
        GreenMax.config(state=NORMAL)

def RedBoolCheck():
    if RedBool.get() == 0:
        RedMin.config(state=DISABLED)
        RedMax.config(state=DISABLED)
    else:
        RedMin.config(state=NORMAL)
        RedMax.config(state=NORMAL)

def LevelCountCheck():
    if CountBool.get() == 0:
        LevelCount.config(state=DISABLED)
    else:
        LevelCount.config(state=NORMAL)

def ExtrasCommand():
    if ExtrasBool.get() == 0:
        ExtrasInput.config(state=DISABLED)
    else:
        ExtrasInput.config(state=NORMAL)

# Setup Output Selection Dropdown
CourseNames = ["SMB1 Casual", "SMB1 Normal", "SMB1 Expert", "SMB1 Master", "SMB1 Marathon", "SMB2 Casual", "SMB2 Normal", "SMB2 Expert", "SMB2 Master", "SMB2 Marathon", "DX Mode", "Reverse Mode", "Original Stage"]
CourseList = StringVar()
CourseList.set(CourseNames[9])

RandomizeGreen = Checkbutton(root, variable = GreenBool, text="Randomize Green Goals?", onvalue=1, offvalue=0, command=GreenBoolCheck)
RandomizeRed = Checkbutton(root, variable = RedBool, text="Randomize Red Goals?", onvalue=1, offvalue=0, command = RedBoolCheck)
CustomLevelCount = Checkbutton(root, variable = CountBool, text="Custom Level Count?", onvalue=1, offvalue=0, command = LevelCountCheck)
Duplicates = Checkbutton(root, variable = DuplicateBool, text="Allow Duplicate Stages?", onvalue=1, offvalue=0)
RemoveBonus = Checkbutton(root, variable = BonusBool, text="Remove Bonus Stages?", onvalue=1, offvalue=0)
ExtrasCheckbox = Checkbutton(root, variable=ExtrasBool, onvalue=1, offvalue =0, text="Limit Extras to End?", command = ExtrasCommand)
ExtrasInput = Entry(root, width=3, state=DISABLED)
OutputLocation = OptionMenu(root, CourseList, *CourseNames)

# Randomization Labels
GreenMinLabel = Label(root, text="Green Goal Min:")
GreenMaxLabel = Label(root, text="Green Goal Max:")
RedMinLabel = Label(root, text="Red Goal Min:")
RedMaxLabel = Label(root, text="Red Goal Max:")
CountLabel = Label(root, text="Custom Level Count:")
OutputLabel = Label(root, text="In-game Difficulty:")
ExtrasLabel = Label(root, text="Extra Stage Count:")

# Randomizer Settings
GreenMin = Entry(root, width=4, state=DISABLED)
GreenMax = Entry(root, width=4, state=DISABLED)
RedMin = Entry(root, width=4, state=DISABLED)
RedMax = Entry(root, width=4, state=DISABLED)
LevelCount = Entry(root, width=4, state=DISABLED)

RandomizeGreen.grid(row = 1, column = 2, columnspan=4)
GreenMinLabel.grid(row = 2, column = 2, sticky="e")
GreenMin.grid(row = 2, column = 3,sticky="w")
GreenMaxLabel.grid(row = 2, column = 4,sticky="e")
GreenMax.grid(row = 2, column = 5, sticky="w")

RandomizeRed.grid(row = 3, column = 2, columnspan=4)
RedMinLabel.grid(row = 4, column = 2, sticky="e")
RedMin.grid(row = 4, column = 3, sticky="w")
RedMaxLabel.grid(row = 4, column = 4, sticky="e")
RedMax.grid(row = 4, column = 5, sticky="w")

CustomLevelCount.grid(row = 5, column = 3, sticky="w")
LevelCount.grid(row = 5, column = 4, sticky="w")
Duplicates.grid(row = 6, column = 3)
RemoveBonus.grid(row = 7, column = 3)
ExtrasCheckbox.grid(row = 8 , column = 2, columnspan=2)
ExtrasLabel.grid(row = 8, column = 4, sticky="w")
ExtrasInput.grid(row = 8, column = 5, sticky="e")

OutputLabel.grid(row = 9, column = 2, columnspan = 2)
OutputLocation.grid(row = 9, column = 2, columnspan = 3, sticky="e")

#Cursed Setup
Cursed = IntVar()
SuperCursed = IntVar()

def CursedCommand() :
    if Cursed.get() == 1:
        SuperCursed = 0
        SuperCursedBox.config(state=DISABLED)
        messagebox.showinfo(title='Warning!',message='Cursed makes it so only one goal per stage will send you forward, and it is based off the Green and Red Max values. Make sure you\'re ready for this!')
    if Cursed.get() == 0:
        SuperCursedBox.config(state=NORMAL)

def SuperCursedCommand() :
    if SuperCursed.get() == 1:
        Cursed = 0
        CursedBox.config(state=DISABLED)
        messagebox.showinfo(title='Warning!',message='Supercursed makes it so only one goal per stage will send you forward, while the rest can send you BACKWARDS (or nowhere)! It is based off the Green and Red Min/Max values (Mins must be 0 OR NEGATIVE). Make sure you\'re ready for this!')
    if SuperCursed.get() == 0:
        CursedBox.config(state=NORMAL)

CursedBox = Checkbutton(root, variable=Cursed, onvalue = 1, offvalue=0, text="Cursed?", comman = CursedCommand, state=NORMAL)
SuperCursedBox = Checkbutton(root, variable=SuperCursed, onvalue = 1, offvalue=0, text="Super Cursed?", command = SuperCursedCommand, state=NORMAL)

CursedBox.grid(row = 10, column = 3)
SuperCursedBox.grid(row = 11, column = 3)

#Seed Setup
SeedLabel = Label(root, text="Seed:")
Seed = Entry(root, width=10)

SeedLabel.grid (row = 12, column = 2, columnspan=2)
Seed.grid (row = 12, column = 2, columnspan = 3)

World1List = [2201, 2202, 2203, 2204, 2001, 2002, 2003, 2004, 2005, 2006]
World2List = [ 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
World3List = [ 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2017]
World4List = [ 2018, 2019, 2020, 2021, 2022, 5023, 2024, 2025, 2026, 5027]
World5List = [ 2028, 2029, 2030, 2031, 2032, 2033, 2034, 2035, 2036, 2037]
World6List = [ 2038, 2039, 2040, 2041, 2042, 2043, 2044, 2045, 2046, 2047]
World7List = [ 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 5289, 2048]
World8List = [ 2049, 5050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058]
World9List = [ 2059, 2060, 2061, 2062, 2063, 2064, 2065, 2066, 2067, 5068]
World10List = [ 2341, 2342, 2343, 2344, 2345, 2346, 2347, 2348, 2349, 2350]
SMB1CasualList = [ 1001, 1002, 1003, 1004, 1091, 1005, 1006, 1007, 1008, 1009, 1101, 1102, 1103 ]
SMB1NormalList = [ 1011, 1012, 1013, 1014, 1091, 1015, 1016, 1017, 1018, 1092, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1093, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 4040, 1101, 1104, 1105, 1103, 4106 ]
SMB1ExpertList = [1041, 1042, 1043, 1044, 1091, 1045, 4046, 1047, 4048, 1092, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1093, 4061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1094, 1071, 4072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1095, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1101, 1107, 1104, 1108, 1109, 1110, 1111, 1103, 1112, 1113 ]
SMB1MasterList = [4121, 1122, 4123, 1124, 4125, 1126, 1127, 4128, 4129, 1130]
SMB2CasualList = [2201, 2202, 2203, 2204, 2205, 2206, 2207, 2208, 2209, 2210, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220]
SMB2NormalList = [2221, 2222, 2223, 2224, 2225, 2226, 2227, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2235, 2236, 2237, 2238, 2239, 2240, 2241, 2242, 2243, 2244, 2245, 5246, 2247, 2248, 2249, 5250, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260]
SMB2ExpertList = [2261, 2262, 2263, 2264, 2265, 2266, 2267, 2268, 2269, 2270, 2271, 2272, 2273, 2274, 2275, 2276, 2277, 2278, 2279, 2280, 2281, 2282, 2283, 2284, 2285, 2286, 2287, 2288, 5289, 2290, 2291, 5292, 2293, 2294, 2295, 2296, 2297, 2298, 2299, 2300, 2301, 2302, 2303, 2304, 2305, 2306, 2307, 2308, 2309, 5310, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320]
SMB2MasterList = [2321, 2322, 5323, 2324, 5325, 2326, 5327, 2328, 2329, 5330, 2331, 2332, 2333, 2334, 2335, 2336, 5337, 2338, 2339, 2340]
DXList = [3932, 3938, 3966, 3946, 3964, 3953, 3965, 3948, 3963, 3960, 3975, 3931, 3957, 3935, 3952, 3945, 3937, 3941, 6974, 3970, 3962, 3933, 3959, 3976, 3954, 3947, 3955, 3967, 3972, 3968, 3949, 3956, 3944, 3961, 3950, 3973, 3943, 3940, 3934, 3951, 3958, 3939, 3971, 3942, 3969, 3936]
ReverseList = [7042, 9954, 8316, 7086, 8257, 7083, 7088, 8039, 7082, 7106]
OGStageList = [3974, 1040, 2023, 2027, 1106, 3934, 1046, 1048, 1061, 2289, 1072, 2050, 2068, 2323, 2325, 2327, 2330, 1121, 1123, 1125, 1128, 1129, 2337]
GreenGoalList = [1002, 1043, 1082, 1086, 1015, 1021, 1028, 1035, 2204, 2214, 2262, 2266, 2272, 2275, 2278, 2289, 2294, 2296, 2297, 2301, 2304, 2312, 2316, 2236, 2247, 2248, 2324, 2332, 2334, 2337, 2338, 2322, 2228, 2241, 2246, 2014, 5023, 2024, 2025, 2029, 2033, 2039, 2042, 2045, 5289, 2052, 2054, 2055, 2059, 2062]
RedGoalList = [1042, 1082, 1028, 2266, 2275, 2289, 2301, 2316, 2228, 2236, 2247, 2266, 2275, 2289, 2301, 2332, 2014, 2024, 2033, 2042, 5289, 2059]
BonusStageList = [1091, 1092, 1093, 1094, 1095, 2205, 2225, 2230, 2240, 2265, 2270, 2280, 2290, 2300, 3942, 3943, 3960, 3969]
ExtrasStageList = [1101, 1102, 1103, 1104, 1105, 4106, 1107, 1108, 1109, 1110, 1111, 1103, 1112, 1113, 2211, 2212, 2213, 2214, 2215, 2216, 2217, 2218, 2219, 2220, 2251, 2252, 2253, 2254, 2255, 2256, 2257, 2258, 2259, 2260, 2311, 2312, 2313, 2314, 2315, 2316, 2317, 2318, 2319, 2320, 2331, 2332, 2333, 2334, 2335, 2336, 5337, 2338, 2339, 2340]
UnusedStagesList = [2246, 2250, 2292, 2310]
TrueCourseNames = ["Smb1_Casual", "Smb1_Normal", "Smb1_Expert", "Smb1_Master", "Smb1_Marathon", "Smb2_Casual", "Smb2_Normal", "Smb2_Expert", "Smb2_Master", "Smb2_Marathon", "SmbDx", "SpecialReverse", "SpecialOriginal"]
RandomizerList = []



def Randomize():
    RandomizerList = []
    RandomizerExtras = []
    OriginalRandomizerList = []
    OriginalRandomizerExtras = []
    if W1.get() == 1:
        RandomizerList.extend(World1List)
    if W2.get() == 1:
        RandomizerList.extend(World2List)
    if W3.get() == 1:
        RandomizerList.extend(World3List)
    if W4.get() == 1:
        RandomizerList.extend(World4List)
    if W5.get() == 1:
        RandomizerList.extend(World5List)
    if W6.get() == 1:
        RandomizerList.extend(World6List)
    if W7.get() == 1:
        RandomizerList.extend(World7List)
    if W8.get() == 1:
        RandomizerList.extend(World8List)
    if W9.get() == 1:
        RandomizerList.extend(World9List)
    if W10.get() == 1:
        RandomizerList.extend(World10List)
    if Unused.get() == 1:
        RandomizerList.extend(UnusedStagesList)
    if SMB1C.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB1CasualList)
        else:
            [RandomizerList.append(x) for x in SMB1CasualList if x not in BonusStageList]
    if SMB1N.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB1NormalList)
        else:
            [RandomizerList.append(x) for x in SMB1NormalList if x not in BonusStageList]
    if SMB1E.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB1ExpertList)
        else:
            [RandomizerList.append(x) for x in SMB1ExpertList if x not in BonusStageList]
    if SMB1M.get() == 1:
        RandomizerList.extend(SMB1MasterList)
    if SMB2C.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB2CasualList)
        else:
            [RandomizerList.append(x) for x in SMB2CasualList if x not in BonusStageList]
    if SMB2N.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB2NormalList)
        else:
            [RandomizerList.append(x) for x in SMB2NormalList if x not in BonusStageList]
    if SMB2E.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(SMB2ExpertList)
        else:
            [RandomizerList.append(x) for x in SMB2ExpertList if x not in BonusStageList]
    if SMB2M.get() == 1:
        RandomizerList.extend(SMB2MasterList)
    if DX.get() == 1:
        if BonusBool.get() == 0:
            RandomizerList.extend(DXList)
        else:
            [RandomizerList.append(x) for x in DXList if x not in BonusStageList]
    if Reverse.get() == 1:
        RandomizerList.extend(ReverseList)
    if OGStageBool.get() == 1:
        RandomizerList.extend(OGStageList)
    DupeRemover = []
    [DupeRemover.append(x) for x in RandomizerList if x not in DupeRemover]
    RandomizerList  = DupeRemover
    RandomizerExtras = []
    OriginalRandomizerList = RandomizerList
    if ExtrasBool.get() == 1:
        [RandomizerExtras.append(x) for x in RandomizerList if x in ExtrasStageList]
        RandomizerList = []
        [RandomizerList.append(x) for x in OriginalRandomizerList if x not in ExtrasStageList]
        OriginalRandomizerExtras = RandomizerExtras
    if Seed.get() == '' :
        random.shuffle(RandomizerList)
        random.shuffle(RandomizerExtras)
    else :
        TheSeed = Seed.get()
        random.seed(TheSeed)
        random.shuffle(RandomizerList)
        random.shuffle(RandomizerExtras)
    if CountBool.get() == 1:
        if LevelCount.get() == '':
            messagebox.showinfo(title='Error!',message='There is no custom level count set! Please add one and try again.')
            return
        while len(RandomizerList) < int(LevelCount.get()):
            RandomizerList.extend(OriginalRandomizerList)
        if len(RandomizerList) > int(LevelCount.get()):
            RandomizerList = RandomizerList[:int(LevelCount.get())]
        if RandomizerExtras != []:
            while len(RandomizerList) < (int(LevelCount.get()) - int(ExtrasInput.get())):
                RandomizerList.extend(OriginalRandomizerList)
            if len(RandomizerList) > (int(LevelCount.get()) - int(ExtrasInput.get())):
                RandomizerList = RandomizerList[:(int(LevelCount.get()) - int(ExtrasInput.get()))]
            while int(ExtrasInput.get()) > len(RandomizerExtras):
                RandomizerExtras.extend(OriginalRandomizerExtras)
                count = 0
            if len(RandomizerExtras) > int(ExtrasInput.get()):
                RandomizerExtras = RandomizerExtras[:int(ExtrasInput.get())]
        RandoSize = len(RandomizerList)
        ExtrasSize = len(RandomizerExtras)
    if len(RandomizerList) == 0:
            messagebox.showinfo(title='Error!',message='You have not selected any levels! Please select at least one and try again.')
            return
    #Seed Easter Eggs lol
    if Seed.get() == 'Helix13_':
        RandomizerList = [3934]
        while len(RandomizerList) < RandoSize:
            RandomizerList.append(3934)
        if RandomizerExtras != []:
            RandomizerExtras = [3934]
            while len(RandomizerExtras) < ExtrasSize:
                RandomizerExtras.append(3934)
    if Seed.get() == 'iswimfly':
        RandomizerList = [5237]
        while len(RandomizerList) < RandoSize:
            RandomizerList.append(5237)
        if RandomizerExtras != []:
            RandomizerExtras = [5237]
            while len(RandomizerExtras) < ExtrasSize:
                RandomizerExtras.append(5237)
    if Seed.get() == 'Stairs':
        RandomizerList = [2347]
        for x in OriginalRandomizerList:
            RandomizerList.append(2347)
        RandomizerExtras = [1087]
        if OriginalRandomizerExtras != []:
            for x in OriginalRandomizerExtras:
                RandomizerList.append(1087)   
    if Seed.get() == '' :
        random.shuffle(RandomizerList)
        random.shuffle(RandomizerExtras)
    else :
        TheSeed = Seed.get()
        random.seed(TheSeed)
        random.shuffle(RandomizerList)
        random.shuffle(RandomizerExtras)    


    file = open("Randomized.json", "w")
    OutputIndex = CourseNames.index(CourseList.get())
    file.write("\n {\"name\":\"Randomized Course Replacing: " + CourseNames[OutputIndex] + "\",\"course_defs\": {\"" + TrueCourseNames[OutputIndex] + "\" : {\"next_course\": \"Invalid\",\"start_movie_id\": \"Invalid\",\"end_movie_id\": \"Invalid\",\"course_stages\": [")
    i = 0
    for x in RandomizerList:
        if i == 0:
            file.write("{\"is_check_point\": false,\"is_half_time\": false, \"stage_id\": ")
        else:
            if len(RandomizerExtras) != 0:
                if i == len(RandomizerList) - 1:
                    file.write(",{\"is_check_point\": true,\"is_half_time\": true, \"stage_id\": ")
                else:
                    file.write(",{\"is_check_point\": false,\"is_half_time\": false, \"stage_id\": ")
            else:
                file.write(",{\"is_check_point\": false,\"is_half_time\": false, \"stage_id\": ")
        if DuplicateBool.get() == 1:
            Stage = random.randint(0, (len(RandomizerList) - 1))
            file.write(str(RandomizerList[Stage]))
            i = Stage     
        else:
            file.write(str(RandomizerList[i]))

        if Cursed.get() == 1:
            if GreenMin.get() == '' or GreenMax.get() == '':
                messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again.')
                return
            if RedMin.get() == '' or RedMax.get() == '':
                messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again.')
                return
            if RandomizerList[i] in GreenGoalList:
                if RandomizerList[i] in RedGoalList:
                    GoalWarps = [0,0,random.randint(1,int(RedMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                else:
                    GoalWarps = [0,random.randint(1,int(GreenMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[0]) + "}")
            if RandomizerList[i] in RedGoalList and RandomizerList[i] not in GreenGoalList:
                    GoalWarps = [0,random.randint(1,int(RedMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
            if RandomizerList[i] not in RedGoalList and RandomizerList[i] not in GreenGoalList:
                file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")   
            if Seed.get() != '':
                TheSeed = random.randint(0,99999)
                random.seed(TheSeed)      
        if SuperCursed.get() == 1:
            if GreenMin.get() == '' or GreenMax.get() == '':
                messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again.')
                return
            if RedMin.get() == '' or RedMax.get() == '':
                messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again.')
                return
            if RandomizerList[i] in GreenGoalList:
                if RandomizerList[i] in RedGoalList:
                    GoalWarps = [random.randint(int(GreenMin.get()),0),random.randint(int(RedMin.get()),0),random.randint(1,int(RedMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                else:
                    GoalWarps = [random.randint(int(GreenMin.get()),0),random.randint(1,int(GreenMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[0]) + "}")
            if RandomizerList[i] in RedGoalList and RandomizerList[i] not in GreenGoalList:
                    GoalWarps = [random.randint(int(RedMin.get()),0),random.randint(1,int(RedMax.get()))]
                    Goal = random.randint(0,len(GoalWarps)-1)
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                    GoalWarps.pop(Goal)
                    file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
            if RandomizerList[i] not in RedGoalList and RandomizerList[i] not in GreenGoalList:
                file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")
            if Seed.get() != '':
                        TheSeed = random.randint(0,99999)
                        random.seed(TheSeed)        
        if Cursed.get() == 0 and SuperCursed.get() == 0:
            file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")
            if RandomizerList[i] in GreenGoalList:
                file.write(",{\"goal_kind\":\"Green\",\"next_step\":")         
                if GreenBool.get() == 0 :
                    if str(RandomizerList[i]) == 1015:
                            file.write("4}")
                    if str(RandomizerList[i]) == 1021 or 1035 or 1002:
                            file.write("3}")
                    else:
                            file.write("2}")
                else:
                    if GreenMin.get() == '' or GreenMax.get() == '':
                        messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again, or uncheck the box.')
                        return
                    GreenGoal = random.randint(int(GreenMin.get()),int(GreenMax.get()))
                    if i - GreenGoal < 0:
                        file.write(str(random.randint(0,int(GreenMax.get()))) + "}")
                    else:
                        file.write(str(GreenGoal) + "}")
                if Seed.get() != '':
                    TheSeed = random.randint(0,99999)
                    random.seed(TheSeed) 
            if RandomizerList[i] in RedGoalList:
                file.write(",{\"goal_kind\": \"Red\", \"next_step\":")
                if RedBool.get() == 0:
                    if RandomizerList[i] == 1028:
                        file.write("7}")
                    else:
                        file.write("3}")
                else:
                    if RedMin.get() == '' or RedMax.get() == '':
                        messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again, or uncheck the box.')
                        return
                    RedGoal = random.randint(int(RedMin.get()),int(RedMax.get()))
                    if i - RedGoal < 0:
                        file.write(str(random.randint(0,int(RedMax.get()))) + "}")
                    else:
                        file.write(str(RedGoal) + "}")
                if Seed.get() != '':
                    TheSeed = random.randint(0,99999)
                    random.seed(TheSeed)
        file.write("]}")
        i = i + 1
    if i == len(RandomizerList):
        i = 0
        for x in RandomizerExtras:
            if i == 0:
                file.write(",{\"is_check_point\": false,\"is_half_time\": false, \"stage_id\": ")
            else:
                file.write(",{\"is_check_point\": false,\"is_half_time\": false, \"stage_id\": ")
            if DuplicateBool.get() == 1:
                Stage = random.randint(0, (len(RandomizerExtras) - 1))
                file.write(str(RandomizerExtras[Stage]))
                i = Stage   
            else:
                file.write(str(RandomizerExtras[i]))
            if Cursed.get() == 1:
                if GreenMin.get() == '' or GreenMax.get() == '':
                    messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again.')
                    return
                if RedMin.get() == '' or RedMax.get() == '':
                    messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again.')
                    return
                if RandomizerExtras[i] in GreenGoalList:
                    if RandomizerExtras[i] in RedGoalList:
                        GoalWarps = [0,0,random.randint(1,int(RedMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                    else:
                        GoalWarps = [0,random.randint(1,int(GreenMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[0]) + "}")
                if RandomizerExtras[i] in RedGoalList and RandomizerExtras[i] not in GreenGoalList:
                        GoalWarps = [0,random.randint(1,int(RedMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                if RandomizerExtras[i] not in RedGoalList and RandomizerExtras[i] not in GreenGoalList:
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")   
                if Seed.get() != '':
                    TheSeed = random.randint(0,99999)
                    random.seed(TheSeed)
            if SuperCursed.get() == 1:
                if GreenMin.get() == '' or GreenMax.get() == '':
                    messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again.')
                    return
                if RedMin.get() == '' or RedMax.get() == '':
                    messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again.')
                    return
                if RandomizerExtras[i] in GreenGoalList:
                    if RandomizerExtras[i] in RedGoalList:
                        GoalWarps = [random.randint(int(GreenMin.get()),0),random.randint(int(RedMin.get()),0),random.randint(1,int(RedMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                    else:
                        GoalWarps = [random.randint(int(GreenMin.get()),0),random.randint(1,int(GreenMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\":\"Green\",\"next_step\":" + str(GoalWarps[0]) + "}")
                if RandomizerExtras[i] in RedGoalList and RandomizerExtras[i] not in GreenGoalList:
                        GoalWarps = [random.randint(int(RedMin.get()),0),random.randint(1,int(RedMax.get()))]
                        Goal = random.randint(0,len(GoalWarps)-1)
                        file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":" + str(GoalWarps[Goal]) + "}")
                        GoalWarps.pop(Goal)
                        file.write(",{\"goal_kind\": \"Red\", \"next_step\":" + str(GoalWarps[0]) + "}")
                if RandomizerExtras[i] not in RedGoalList and RandomizerExtras[i] not in GreenGoalList:
                    file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")
                if Seed.get() != '':
                            TheSeed = random.randint(0,99999)
                            random.seed(TheSeed)        
            if Cursed.get() == 0 and SuperCursed.get() == 0:
                file.write(",\"goals\": [{\"goal_kind\":\"Blue\",\"next_step\":1}")
                if RandomizerExtras[i] in GreenGoalList:
                    file.write(",{\"goal_kind\":\"Green\",\"next_step\":")         
                    if GreenBool.get() == 0 :
                        if str(RandomizerExtras[i]) == 1015:
                                file.write("4}")
                        if str(RandomizerExtras[i]) == 1021 or 1035 or 1002:
                                file.write("3}")
                        else:
                                file.write("2}")
                    else:
                        if GreenMin.get() == '' or GreenMax.get() == '':
                            messagebox.showinfo(title='Error!',message='One of the Custom Green Goal Settings is missing! Please fill both in and try again, or uncheck the box.')
                            return
                        GreenGoal = random.randint(int(GreenMin.get()),int(GreenMax.get()))
                        if i - GreenGoal < 0:
                            file.write(str(random.randint(0,int(GreenMax.get()))) + "}")
                        else:
                            file.write(str(GreenGoal) + "}")
                    if Seed.get() != '':
                        TheSeed = random.randint(0,99999)
                        random.seed(TheSeed) 
                if RandomizerExtras[i] in RedGoalList:
                    file.write(",{\"goal_kind\": \"Red\", \"next_step\":")
                    if RedBool.get() == 0:
                        if RandomizerExtras[i] == 1028:
                            file.write("7}")
                        else:
                            file.write("3}")
                    else:
                        if RedMin.get() == '' or RedMax.get() == '':
                            messagebox.showinfo(title='Error!',message='One of the Custom Red Goal Settings is missing! Please fill both in and try again, or uncheck the box.')
                            return
                        RedGoal = random.randint(int(RedMin.get()),int(RedMax.get()))
                        if i - RedGoal < 0:
                            file.write(str(random.randint(0,int(RedMax.get()))) + "}")
                        else:
                            file.write(str(RedGoal) + "}")
                    if Seed.get() != '':
                        TheSeed = random.randint(0,99999)
                        random.seed(TheSeed)
            i = i + 1
            file.write("]}")
    file.write("]}}}")   
    file.close()
    messagebox.showinfo(title='Success!',message='The Randomization is complete! Randomized.json should be next to your executable file.')


def ExportConfig():
    filename = filedialog.asksaveasfilename(
        defaultextension='.cfg', filetypes=[("Config File", '*.cfg')], 
        title="Save as...")
    if not filename.endswith('.cfg'):
        filename += '.cfg'
    file = open(filename , "w")
    #World 1 Through 10
    file.write(str(W1.get()) + ',' + str(W2.get()) + ',' + str(W3.get()) + ',' + str(W4.get()) + ',' + str(W5.get()) + ',' + str(W6.get()) + ',' + str(W7.get()) + ',' + str(W8.get()) + ',' + str(W9.get()) + ',' + str(W10.get()) + ',')
    #SMB1CNEM, SMB2CNEM, DX, Reverse, OG, Unused
    file.write(str(SMB1C.get()) + ',' + str(SMB1N.get()) + ',' + str(SMB1E.get()) + ',' + str(SMB1M.get()) + ',' + str(SMB2C.get()) + ',' + str(SMB2N.get()) + ',' + str(SMB2E.get()) + ',' + str(SMB2M.get()) + ',' + str(DX.get()) + ',' + str(Reverse.get()) + ',' + str(OGStageBool.get()) + ',' + str(Unused.get()) + ',')
    #Misc Stuff
    file.write(str(GreenBool.get()) + ',' + str(GreenMin.get()) + ',' + str(GreenMax.get()) + ',' + str(RedBool.get()) + ',' + str(RedMin.get()) + ',' + str(RedMax.get()) + ',' + str(CountBool.get()) + ',' + str(LevelCount.get()) + ',' + str(DuplicateBool.get()) + ',' + str(BonusBool.get()) + ',' + str(ExtrasBool.get()) + ',' + str(ExtrasInput.get()) + ',' + str(CourseNames.index(CourseList.get())) + ',' + str(Cursed.get()) + ',' + str(SuperCursed.get()) + ',' + str(Seed.get()))
    file.close
def ImportConfig():
    configname = filedialog.askopenfilename(
        defaultextension='.cfg', filetypes=[("Config File", '*.cfg')], 
        title="Open a config..."
    )
    if not configname.endswith('.cfg'):
        messagebox.showinfo(title='Error!', message='It looks like you didn\'t select a config file. Please try again!')
    config = open(configname)
    data = config.read()
    datalist = data.split(',')
    print(len(datalist))
    if len(datalist) != 38:
        messagebox.showinfo(title='Error!', message='It looks like you\'ve selected an invalid config file. Please try again!')
    else:
        W1.set("")
        W1.set(datalist[0])
        W2.set(datalist[1])
        W3.set(datalist[2])
        W4.set(datalist[3])
        W5.set(datalist[4])
        W6.set(datalist[5])
        W7.set(datalist[6])
        W8.set(datalist[7])
        W9.set(datalist[8])
        W10.set(datalist[9])
        SMB1C.set(datalist[10])
        SMB1N.set(datalist[11])
        SMB1E.set(datalist[12])
        SMB1M.set(datalist[13])
        SMB2C.set(datalist[14])
        SMB2N.set(datalist[15])
        SMB2E.set(datalist[16])
        SMB2M.set(datalist[17])
        DX.set(datalist[18])
        Reverse.set(datalist[19])
        OGStageBool.set(datalist[20])
        Unused.set(datalist[21])
        GreenBool.set(datalist[22])
        GreenBoolCheck()

        GreenMin.delete(0, END)
        GreenMin.insert(0, datalist[23])
        GreenMax.delete(0, END)
        GreenMax.insert(0, datalist[24])
        RedBool.set(datalist[25])
        RedBoolCheck()
        RedMin.delete(0, END)
        RedMin.insert(0, datalist[26])
        RedMax.delete(0, END)
        RedMax.insert(0, datalist[27])
        CountBool.set(datalist[28])
        LevelCountCheck()
        LevelCount.delete(0, END)
        LevelCount.insert(0, datalist[29])
        DuplicateBool.set(datalist[30])
        BonusBool.set(datalist[31])
        ExtrasBool.set(datalist[32])
        ExtrasCommand()
        ExtrasInput.delete(0, END)
        ExtrasInput.insert(0, datalist[33])
        CourseList.set(CourseNames[int(datalist[34])])
        Cursed.set(datalist[35])
        CursedCommand()
        SuperCursed.set(datalist[36])
        SuperCursedCommand()
        Seed.delete(0, END)
        Seed.insert(0, datalist[37])

ExportButton = Button(root, text="Export Config", command = ExportConfig)
ImportButton = Button(root, text="Import Config", command = ImportConfig)
RandomizeButton = Button(root, text="Randomize!", command = Randomize)

RandomizeButton.grid(row = 15, column = 3)
ExportButton.grid(row=15, column=0)
ImportButton.grid(row=15, column=1)
root.mainloop()