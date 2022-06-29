# -*- coding: utf-8 -*-

# API 1 ( https://api-alquranid.herokuapp.com/surah/nomorsurah )
# API 2 ( https://api-alquranid.herokuapp.com/surah )

import os,sys,requests,json

response = requests.get("https://api-alquranid.herokuapp.com/surah").json()


listsurat = []

def getlistsurat():
    for x in response['data']:
        listsurat.append(x["nama"])
    print("\n\n • list surat al qur'an\n")
    for i in range(len(listsurat)):
        print(f"  {i+1}. {listsurat[i]}")
    main()

def main():
    pilih = input("\n • pilih nomor surat yang mau di baca\n • Example : 93\n\n • pilih: ")
    if int(pilih) == 0:
        exit("\n • maaf surat tidak ada!")
    elif int(pilih) >= 115:
        exit("\n • maaf surat tidak ada!")
    else:
        response = requests.get(f"https://api-alquranid.herokuapp.com/surah/{pilih}").json()
        for i in response['data']:
            print(f"\n {i['nomor']}. {i['ar']}")
            print(f" artinya: {i['id']}")

if __name__ == "__main__":
    os.system("clear")
    getlistsurat()





