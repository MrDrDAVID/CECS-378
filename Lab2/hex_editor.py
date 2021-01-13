#Saved game file location; edit according to file location
filePath = 'C:/Games/Ultima_5/SAVED.GAM'

#In-game characters
characters = {1: 'PLAYER', 2: 'SHAMINO', 3: 'IOLO',
         4: 'MARIAH', 5: 'GEOFFREY', 6: 'JAANA',
         7: 'JULIA', 8: 'DUPRE', 9: 'KATRINA',
         10: 'SENTRI', 11: 'GWENNO',  12: 'JOHNE',
         13: 'GORN', 14: 'MAXWELL', 15: 'TOSHI',
         16: 'SADUJ'}

#Offset (position) of characters in SAVED.GAM
characterOffsets = {'PLAYER': int('0x02', 16), 'SHAMINO': int('0x22', 16), 'IOLO': int('0x42', 16),
                'MARIAH': int('0x62', 16), 'GEOFFREY': int('0x82', 16), 'JAANA': int('0xA2', 16),
                'JULIA': int('0xC2', 16), 'DUPRE': int('0xE2', 16), 'KATRINA': int('0x102', 16),
                'SENTRI': int('0x122', 16), 'GWENNO': int('0x142', 16), 'JOHNE': int('0x162', 16),
                'GORN': int('0x182', 16), 'MAXWELL': int('0x1A2', 16), 'TOSHI': int('0x1C2', 16),
                'SADUJ': int('0x1E2', 16)}

#Character stats
stats = {1: 'STRENGTH', 2: 'DEXTERITY', 3: 'INTELLIGENCE',
         4: 'MAGIC', 5: 'HP', 6: 'MAX HP', 7: 'EXPERIENCE'}

#Offset (position) of character stats in SAVED.GAM
statOffsets = {'STRENGTH': int('0x0E', 16), 'DEXTERITY': int('0x0F', 16), 'INTELLIGENCE': int('0x10', 16),
               'MAGIC': int('0x11', 16), 'HP': int('0x12', 16), 'MAX HP': int('0x14', 16),
               'EXPERIENCE': int('0x16', 16)}

#Maximum values for statss (in decimal to be converted to hex for offsets in SAVED.GAM)
statMaxVal = {'STRENGTH': 99, 'DEXTERITY': 99, 'INTELLIGENCE': 99,
              'MAGIC': 99, 'HP': 999, 'MAX HP': 999, 'EXPERIENCE': 9999}

def readFile() -> list:
    """
    Reads in binary values of SAVED.GAM file
    @returns: list of SAVE.GAM hex offset values in decimal form
    """
    with open(filePath, 'rb') as saveFile:
        dataBytes = list(bytearray(saveFile.read()))
        saveFile.close()
    return dataBytes

def writeToFile(fileData:list):
    """
    Writes in binary values to SAVED.GAM file
    @param fileData: list of SAVE.GAM hex offset values in decimal form
    """
    with open(filePath, 'wb') as saveFile:
        saveFile.write(bytearray(fileData))
        saveFile.close()
        
def editStats(charDictKey:int, fileData:list):
    """
    Prompts user to select which stat they want to edit
    @param charDictKey: the key associated with the character in 'characters'
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('\n-----------------------------------------')
    print('Choose a stat to edit for {}:'.format(characters[charDictKey]))
    print('[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}'.format(stats[1], stats[2], stats[3], stats[4],
                                                                          stats[5], stats[6], stats[7]))
    print('-----------------------------------------')
    
    #Prompt user to choose which stat to edit
    while True:
        try:
            userInp = int(input(': '))
        except ValueError:
            print('Please enter a valid option (1-7).')
            continue
        if userInp < 1 or userInp > 7:
            print('Please enter a valid option (1-7).')
            continue
        else:
            break
        
    statName = stats[userInp]
    index = statOffsets[statName] + characterOffsets[characters[charDictKey]] - 2
    maxVal = statMaxVal[statName]
        
    #Prompt user for stat val to change to
    while True:
        try:
            print('Current stat for {}\'S {} is {}.'.format(characters[charDictKey], statName, fileData[index]))
            print('What would you like to change it to? (0 - {})'.format(maxVal))
            statChange = int(input(': '))
        except ValueError:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        if statChange < 0 or statChange > maxVal:
            print('Please enter a valid option (0 - {}).'.format(maxVal))
            continue
        else:
            break
        
    #Make changes to SAVE.GAM
    count = 0
    byteArray = list(bytearray((statChange).to_bytes(2, byteorder='little')))
    if len(byteArray) == 1:
        byteArray.insert(0, 0)
    for b in byteArray:
        if b != 0:
            fileData[index + count] = b
        count += 1
    print('{} {} changed to {}'.format(characters[charDictKey], statName, statChange))
    
    #Prompt user for additional changes
    print('\nWould you like to edit another stat? [Y or N]')
    userInp = input(': ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input(': ')
    if userInp.upper() == 'Y':
        editStats(charDictKey, fileData)
    else:
        print('Returning to character selection...\n')
        
def charSelect(fileData:list):
    """
    Prompts user to select a character they want to edit
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('\n-----------------------------------------')
    print('Choose a character to edit:')
    print('[1] {}\n[2] {}\n[3] {}\n[4] {}\n[5] {}\n[6] {}\n[7] {}\n[8] {}'.format(characters[1], characters[2], characters[3], characters[4],
                                                                                  characters[5], characters[6], characters[7], characters[8]))
    print('[9] {}\n[10] {}\n[11] {}\n[12] {}\n[13] {}\n[14] {}\n[15] {}\n[16] {}'.format(characters[9], characters[10], characters[11], characters[12],
                                                                                  characters[13], characters[14], characters[15], characters[16]))
    print('-----------------------------------------')
    
    #Prompt user to choose which character to edit
    while True:
        try:
            userInp = int(input(': '))
        except ValueError:
            print('Please enter a valid option (1 - 16).')
            continue
        if userInp < 1 or userInp > 16:
            print('Please enter a valid option (1 - 16).')
            continue
        else:
            break
    editStats(userInp, fileData)
    
    #Prompt user for additional changes
    print('Would you like to edit another character? [Y or N]')
    userInp = input(': ')
    while userInp.upper() != 'Y' and userInp.upper() != 'N':
        print('Please enter a valid option (Y or N).')
        userInp = input(': ')
    if userInp.upper() == 'Y':
        charSelect(fileData)
    else:
        print('Returning to menu...\n')
        menu(fileData)

def menu(fileData:list):
    """
    Text UI for hex editor
    @param fileData: list of SAVE.GAM hex offset values in decimal form (from readFile())
    """
    print('+++++++++++++++++++++++')
    print('+ ULTIMA V HEX EDITOR +')
    print('+++++++++++++++++++++++')
    print('-----------------------------------------')
    print('Choose a category to edit:')
    print('[1] Character Stats (e.g. str, int, etc.)')
    print('[2] Save Game File and Exit')
    print('-----------------------------------------')
    
    #Prompt user to choose a category to edit
    userInp = input(': ')
    while userInp != '1' and userInp != '2':
        print('Please enter one of the valid options (1 - 2).')
        userInp = input(': ')
    if userInp == '1':
        charSelect(fileData)
    elif userInp == '2':
        print('Saving edits...')
        writeToFile(fileData) #Finalize all user changes to SAVE.GAM
        print('Game file modified. Exiting.')
    
if __name__ == '__main__':
    menu(readFile())