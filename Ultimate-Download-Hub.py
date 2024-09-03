import requests
import time
import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
        
# Pc Game Download Section
def pc_game(game_nm):
    
    url_1 = f"https://www.apunkagames.com/{game_nm}"
    find_1 = requests.get(f'{url_1}').status_code
    
    url_2 = f"https://oceanofgames.com/{game_nm}"
    find_2 = requests.get(f"{url_2}").status_code
    
    url_3 = f"https://www.pcgamespunch.com/{game_nm}"
    find_3 = requests.get(f"{url_3}").status_code
    
    if (find_1 == 404) and (find_2) and (find_3 == 404):
        time.sleep(2)
        print(f"\n📥 Game Download Link Not Found➡️  ❌") 
    else:
        game = 1   
    if find_1 == 404:
        game = 1
    else:
        print(f"\n📥 Game Downlaod Link➡️  {url_1}")
    if find_2 == 404:
        game = 1
    else:
        print(f"\n📥 Game Downlaod Link➡️  {url_2}")
    if find_3 == 404:
        game = 1
    else:
        print(f"\n📥 Game Downlaod Link➡️  {url_3}")
            
# Android Game Download Section
def android_gm(game_nm):
    
    url_1 = f"https://apkdone.com/{game_nm}"
    find_1 = requests.get(f'{url_1}').status_code
    
    url_2 = f"https://apkpure.com/search?q={game_nm}"
    find_2 = requests.get(f"{url_2}").status_code    
    
    url_3 =f"https://androeed.store/files/{game_nm}.html"
    find_3 = requests.get(f'{url_3}').status_code
    
    if (find_1 == 404) and (find_2 == 404) and (find_3 == 404):
        print(f"\n📥 Game Download Link Not Found➡️  ❌")
    
    else:
        print(f"\n📥 Game Downlaod Link➡️  {url_1}")
        print(f"\n📥 Game Downlaod Link➡️  {url_2}")
        print(f"\n📥 Game Downlaod Link➡️  {url_3}")
        
## Movie & Series 
def cinedoze(mv_nm):
    url = f'https://cinedoze.com/{mv_nm}'
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 Cinedoze Link Not Available: ❌')
    else:
        print(f'\n📥 Ciniedoze Link Available: {url}')
        
def mls(mv_nm):  
    url = f'https://mlsbd.shop/{mv_nm}'
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 Mlsbd Link Not Available: ❌')
    else:
        print(f'\n📥 Mlsbd Link Available: {url}')
        
def cinevood(mv_nm):
    url = f"https://1cinevood.store/?s={mv_nm}"   
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 Cinevood Link Not Available: ❌')
    else:
        print(f'\n📥 Cinevood Link Available: {url}')
    
def mlwbd(mv_nm):
    url = f"https://mlwbd.lv/{mv_nm}"
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 Mlwbd Link Not Available: ❌')
    else:
        print(f'\n📥 Mlwbd Link Available: {url}')

def rg(mv_nm):
    url = f"https://www.youtube.com/@RGEntertainmentIndia/search?query={mv_nm}"
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 RG Entertainment Link Not Available: ❌')
    else:
        print(f'\n📥 RG Entertainment Link Available: {url}')
        
def hdhub(mv_nm):
    url = f"https://hdhub4u.contact/{mv_nm}"
    search = requests.get(f'{url}')
    if search.status_code == 404:
        print(f'\n📥 Hdhub4u Link Not Available: ❌')
    else:
        print(f'\n📥 Hdhub4u Link Available: {url}')  
                                                    # Movie & Series End
                                                            
while True:
    clear_screen()
    print('\n█▓▒ ULTIMATE DOWNLOAD HUB ▒▓█')
    print('      @TR-FAHIM ')
    print('\n[1] Pc Game Download 🎮\n[2] Android Game Download 🎮\n[3] Movie & Series Downlaod 🎥\n\n[4] About 📑')
    print('[0] Exit 👽')
    choose = input('\n♦️ Choose Option →→ ')
    
    if choose == '1':
        clear_screen()
        print("\nPC Games Download 🎮 >> @trfahim")
        game_nm_input = input('\n🎯 Game Name: ').lower()
        game_nm = game_nm_input.replace(" ","-")
        clear_screen()
        print('\nLoading......')
        time.sleep(2)
        print(f'\n{game_nm.title()} Downlaod Link 👇')
        time.sleep(2)
        pc_game(game_nm)
        
        return_hm=input('\n🧿 [H] Return Home [E] Exit :≡ ')
        if return_hm == 'H' or return_hm == 'h':
            print('\n🏠 Return Home\n')
        elif return_hm == 'e' or return_hm == 'E':
            clear_screen()
            print('\n👽 Exit Done 👽\n')
            break
        else:
            print('\n💀 Wrong Input\n')
            
    
    elif choose == '2':
        clear_screen()
        print("\nAndroid Games & Apps Download 🎮 >> @trfahim")
        game_nm_input = input('\n🎯 Enter [Game/App] Name: ').lower()
        game_nm = game_nm_input.replace(" ","-")
        clear_screen()
        print('\nLoading......')
        time.sleep(2)
        print(f'\n{game_nm.title()} Downlaod Link 👇')
        time.sleep(2)
        android_gm(game_nm)
        
        return_hm=input('\n🧿 [H] Return Home [E] Exit :≡ ')
        if return_hm == 'H' or return_hm == 'h':
            print('\n🏠 Return Home\n')
        elif return_hm == 'e' or return_hm == 'E':
            clear_screen()
            print('\n👽 Exit Done 👽\n')
            break
        else:
            print('\n💀 Wrong Input\n')

## Movie & Series Download Section
    elif choose == '3':
        clear_screen()
        print('\nDOWNLOAD FREE MOVIES & SERIES 🎥 >> @trfahim')        
        mv_nm_input =input('\n📀 Movie & Series Name: ').lower()
        mv_nm=mv_nm_input.replace(" ", "-")
        clear_screen()
        print('\nLoading.....')
        time.sleep(3)
        print(f'\n{mv_nm.title()} Download Link Here 👇')
        cinedoze(mv_nm)
        time.sleep(2)
        mls(mv_nm)
        time.sleep(1)
        cinevood(mv_nm)
        time.sleep(1)
        mlwbd(mv_nm)
        time.sleep(1)
        hdhub(mv_nm)
        time.sleep(1)
        rg(mv_nm)
        
        return_hm=input('\n🧿 [H] Return Home [E] Exit :≡ ')
        if return_hm == 'H' or return_hm == 'h':
            print('\n🏠 Return Home\n')
        elif return_hm == 'e' or return_hm == 'E':
            clear_screen()
            print('\n👽 Exit Done 👽\n')
            break
        else:
            print('\n💀 Wrong Input\n')

## About
    elif choose == '4':
        clear_screen()
        print('\n👀 A B O U T 👀')
        print('\nProgarm Name >> Ultimate Download Hub')
        print('Author >> TR Fahim')
        print('GitHub >> https://github.com/trfahim')
        print('FaceBook >> https://www.facebook.com/tahsan.rahman.fahim')
        
        return_hm=input('\n🧿 [H] Return Home [E] Exit :≡ ')
        if return_hm == 'H' or return_hm == 'h':
            print('\n🏠 Return Home\n')
        elif return_hm == 'e' or return_hm == 'E':
            clear_screen()
            print('\n👽 Exit Done 👽\n')
            break
        else:
            print('\n💀 Wrong Input\n')

## Exit
    elif choose == '0':
        clear_screen()
        print('\n👽 EXIT SUCESSFUL 👽\n')
        break
    else:
        clear_screen()
        print('\n💀  Wrong Input 💀')
        return_hm=input('\n🧿 [H] Return Home [E] Exit :≡ ')
        if return_hm == 'H' or return_hm == 'h':
            print('\n🏠 Return Home\n')
        elif return_hm == 'e' or return_hm == 'E':
            clear_screen()
            print('\n👽 Exit Done 👽\n')
            break
        else:
            print('\n💀 Wrong Input\n')
           
        
        
        
                                  ### END ###
        
