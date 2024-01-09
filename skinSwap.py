'''to create .exe:
python -m PyInstaller skinSwap.py
delete dist after placing "_internal" and the executable in root
delete build
delete .spec'''
import shutil

foo = ['name', 'description (this one is just an example)', "default", "default tunic and pants", "onesie", "a snug purple onesie", "jester", "The Jester", "legendOfZelda", "Link from Legend of Zelda", "goth", "goth", "bootyShortsCalifornia", "red shirt, blonde hair, booty shorts.", "bootyShortsMiami", "pink shirt, black... uh, hair AND skin, booty shorts", "theOriginal", "the original color palette from the very first iteration", "McDonald", "McDonald's Uniform, sorta", "country", "country bumpkin", "santa", "Christmas colors", "hotLeather", "hot leather", "tieAndSlacks", "tie and slacks", "familyGuy", "Peter Griffin from Fortnite"]
names = foo[::2]
dispNames = foo[::2]
descs = foo[1::2]
for i in range(len(dispNames)):
    while(len(dispNames[i])) <= 50:
        dispNames[i] = dispNames[i].split()
        dispNames[i].append('-')
        dispNames[i] = ''.join(dispNames[i])

print('please type the name of the outfit you would like to use, or type "exit" to close the program. You could also just close the window. If it closes immediately after you enter a command, you did it right! :)')
for i in range(len(names)):
    print(f'{dispNames[i]}{descs[i]}')

inp = None
while inp not in names[1:]:
    inp = input('\n>>>')

    if inp == 'name':
        print("===haha you're funny, but that's just an example. Try again.")
    elif inp not in names:
        print("===I don't recognize that name from the list, make sure you copy the name exactly as it appears on the left hand side.")

try:
    shutil.copyfile(f'files/{inp}/player.png', 'data/enemies_gfx/player.png')
    shutil.copyfile(f'files/{inp}/player_arm.png', 'data/enemies_gfx/player_arm.png')
    for part in ['head', 'left_arm', 'left_foot', 'left_thigh', 'right_arm', 'right_foot', 'right_thigh', 'torso']:
        shutil.copyfile(f'files/{inp}/ragdolls/player/{part}.png', f'data/ragdolls/player/{part}.png')
    #print(f'===success! {inp}\'s graphics have been set!') # not needed since program will just close
except FileNotFoundError:
    print('you entered a correct value, but the program did not find the files to move. Make sure this is in the proper mod folder, and that the mod is up to date. Contact me on discord @ "thop." if errors persist.\nExiting...')
except:
    print('some sort of error occured. If you think you\'ve got everything working right, contact me on discord @ "thop."\nExiting...')
