#kodu ingiliççe yorumalrı türkçe yapam bari

import random #random kutuphane
import time # time kutuphanesi

class Remote(): #uzaktan kumanda sınıfı

        #init fonkisyonu tekrar düzenleyip kumanda objeme fonksiyon ekleyecem
    def __init__(self,TVSituation="Closed",TVChannelList=["Kanal D"],TVSound=0,TVChannel="Trt"):
        self.TVSituation=TVSituation
        self.TVChannelList=TVChannelList
        self.TVSound=TVSound
        self.TVChannel=TVChannel

    #açma fonksiyonu
    def TVTurnon(self):
        if(self.TVSituation=="open"):
            print("The tv is already open ")

        else:
            print("The tv is opening")
            self.TVSituation="open"

    #kapama fonksiyonu
    def TVTurnoff(self):
        if(self.TVSituation=="closed"):
            print("The tv is closed already:/")

        else:
            print("The TV is about to close")
            self.TVSituation="closed"
    #ses ayarlama fonksiyonum
    def soundSetting(self):
        #soundLevel=int(input("How much do you want to increase sound "))
        #self.TVSound +=soundLevel

        while True:
            respond=input("decrease: '<'\nıncrease: '>'\nExit:exit")
            if respond == '<':
                if self.TVSound != 0:
                    self.TVSound -= 1
                    print("Sound:", self.TVSound)
            elif respond == '>':
                if self.TVSound != 100:
                    self.TVSound += 1
                    print("Sound:", self.TVSound)
            elif respond.lower() == 'exit':
                print("Sound level has been adjusted:", self.TVSound)
                break
            else:
                print("Invalid input!")


    #kanal ekleme fonksıyonum
    def addChannel(self,newChannel):
        print("ı am adding the channel")
        time.sleep(0.6)

        self.TVChannelList+=newChannel

        self.TVChannelList.append(newChannel)
        time.sleep(0.3)
        print("the channel have been added")

    #random fonksıyonum
    def randomChannel(self):

        randomm=random.randint(0,len(self.TVChannel)-1)

        self.TVChannel=self.TVChannelList[randomm]

        print("Current Channel:",self.TVChannel)


    #len fonksıyonuyla oynuyorum
    def __len__(self):
        return len(self.TVChannelList)
    #str ile oynuyom
    def __str__(self):
        return "TV SİTUATİONS: {}\nTV SOUND: {}\nTV CHANNEL LİST: {}\n CURENNT CHANNEL: {}\n".format(self.TVSituation,self.TVSound,self.TVChannelList,self.TVChannel)
#nesne oluşturma
remote=Remote()
#menum
print("""
TELEVİSİON APPLİCATİON WİTH OOP

1.TV open

2.TV Close

3.Sound adjustment

4.Add channel

5.Learınıng Channel number

6.Going to a random channel

7.TELEVİSİON INFORMATİONS

'q' for EXİT

""")
#işlemlerim
while True:
    choice=input("Chosse what do you want to do from remote")

    if choice=='q':
        print("Exiting bye bye....")
        break

    elif choice=="1":
        remote.TVTurnon()

    elif choice == "2":
        remote.TVTurnoff()

    elif choice == "3":
        remote.soundSetting()

    elif choice == "4":
        channelNames=input("Channel Names ',' with comma")
        TVChannelList=channelNames.split(",")

        for adding in TVChannelList:
            remote.addChannel


    elif choice == "5":
        print("Channel number",len(remote))




    elif choice == "6":
        remote.randomChannel()

    elif choice == "7":
        print(remote)





    else:
        print("İnvalid choice.....")



































