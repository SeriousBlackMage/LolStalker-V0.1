from riotwatcher import RiotWatcher
from termcolor import cprint
from pyfiglet import figlet_format
import os

class Stalker:

    def __init__(self, region):
        if(str(input("Api Key: Already Set[a], Configure[b]:")) == 'b'):
            self.file = open("API-Key.txt","w+")
            self.file.write(str(input("API-Key:")))
            self.file.close()
        with open('API-Key.txt','r') as key:
            self.watcher = RiotWatcher(key.read())
        self.my_region = region
        self.setTarget()
        self.chNames = {
            516: "Ornn",
            164: "Camille",
            497: "Rakan",
            498: "Xayah",
            141: "Kayn",
            266: "Aatrox",
            412:  "Thresh",
            23:  "Tryndamere",
            79:  "Gragas",
            69:  "Cassiopeia",
            136:  "Aurelion Sol",
            13:  "Ryze",
            78:  "Poppy",
            14:  "Sion",
            1:  "Annie",
            202:  "Jhin",
            43:  "Karma",
            111:  "Nautilus",
            240:  "Kled",
            99:  "Lux",
            103:  "Ahri",
            2:  "Olaf",
            112:  "Viktor",
            34:  "Anivia",
            27:  "Singed",
            86:  "Garen",
            127:  "Lissandra",
            57:  "Maokai",
            25:  "Morgana",
            28:  "Evelynn",
            105:  "Fizz",
            74:  "Heimerdinger",
            238:  "Zed",
            68:  "Rumble",
            82:  "Mordekaiser",
            37:  "Sona",
            96:  "Kog'Maw",
            55:  "Katarina",
            117:  "Lulu",
            22:  "Ashe",
            30:  "Karthus",
            12:  "Alistar",
            122:  "Darius",
            67:  "Vayne",
            110:  "Varus",
            77:  "Udyr",
            89:  "Leona",
            126:  "Jayce",
            134:  "Syndra",
            80:  "Pantheon",
            92:  "Riven",
            121:  "Kha'Zix",
            42:  "Corki",
            268:  "Azir",
            51:  "Caitlyn",
            76:  "Nidalee",
            85:  "Kennen",
            3:  "Galio",
            45:  "Veigar",
            432:  "Bard",
            150:  "Gnar",
            90:  "Malzahar",
            104:  "Graves",
            254:  "Vi",
            10:  "Kayle",
            39:  "Irelia",
            64:  "Lee Sin",
            420:  "Illaoi",
            60:  "Elise",
            106:  "Volibear",
            20:  "Nunu",
            4:  "Twisted Fate",
            24:  "Jax",
            102:  "Shyvana",
            429:  "Kalista",
            36:  "Dr. Mundo",
            427:  "Ivern",
            131:  "Diana",
            223:  "Tahm Kench",
            63:  "Brand",
            113:  "Sejuani",
            8:  "Vladimir",
            154:  "Zac",
            421:  "Rek'Sai",
            133:  "Quinn",
            84:  "Akali",
            163:  "Taliyah",
            18:  "Tristana",
            120:  "Hecarim",
            15:  "Sivir",
            236:  "Lucian",
            107:  "Rengar",
            19:  "Warwick",
            72:  "Skarner",
            54:  "Malphite",
            157:  "Yasuo",
            101:  "Xerath",
            17:  "Teemo",
            75:  "Nasus",
            58:  "Renekton",
            119:  "Draven",
            35:  "Shaco",
            50:  "Swain",
            91:  "Talon",
            40:  "Janna",
            115:  "Ziggs",
            245:  "Ekko",
            61:  "Orianna",
            114:  "Fiora",
            9:  "Fiddlesticks",
            31:  "Cho'Gath",
            33:  "Rammus",
            7:  "LeBlanc",
            16:  "Soraka",
            26:  "Zilean",
            56:  "Nocturne",
            222:  "Jinx",
            83:  "Yorick",
            6:  "Urgot",
            203:  "Kindred",
            21:  "Miss Fortune",
            62:  "Wukong",
            53:  "Blitzcrank",
            98:  "Shen",
            201:  "Braum",
            5:  "Xin Zhao",
            29:  "Twitch",
            11:  "Master Yi",
            44:  "Taric",
            32:  "Amumu",
            41:  "Gangplank",
            48:  "Trundle",
            38:  "Kassadin",
            161:  "Vel'Koz",
            143:  "Zyra",
            267:  "Nami",
            59:  "Jarvan IV",
            81:  "Ezreal"
    }
        self.draw()

    def setTarget(self):
        self.target = self.watcher.summoner.by_name(self.my_region, str(input("Who is your Target?: ")))
        self.targetID = self.target['id']
        self.targetAccID = self.target['accountId']

    def draw(self):
        clear = lambda: os.system('cls')
        clear()
        print("\n")
        cprint(figlet_format('Stalker', font='starwars'),attrs=['bold'])

    def mainloop(self):

        print("\n----------------------------------------------\nWhat do you want to know ?")
        choice = str(input("----------------------------------------------\n\nUser Information:\n-----------------\nDetails[d]\nChampMasteries[c]\nUserMasteries[m]\nUserRunes[r]\nUserLeagues[l]\nUserMatch[h]\n----------------------------------------------\n\nMisc:\n-----\nFreeToPlayChamps[f]\nNew Target[a]\n ----------------------------------------------\n\nChoice:"))
        self.draw()
        if choice == 'd': self.userDetails()
        elif choice == 'a': self.setTarget()
        elif choice == 'f': self.freeToPlayChamps()
        elif choice == 'c': self.userCmasteries()
        elif choice == 'l': self.userLeagues()
        elif choice == 'm': self.userMasteries()
        elif choice == 'h': self.userMatch()
        elif choice == 'r': self.userRunes()
        elif choice == 's': self.spectTest()

    def userDetails(self):
        print("\nName:",self.target['name'])
        print("Account ID:", self.target['accountId'])
        print("Level:", self.target['summonerLevel'])
        print("Icon:", self.target['profileIconId'])

    def freeToPlayChamps(self):
        fChamps = self.watcher.champion.all(self.my_region,True)
        for i in fChamps['champions']:
            print("\nChampion ID:",i['id'])
            print("Champion Name:",self.chNames[i['id']],)

    def userCmasteries(self):
        inputR = str(input("Abfrage nach Score[a] , Abfrage nach Champion[c], GesamterChampionScore[s]: "))

        if inputR == 'a':
            print("\nSummoner:",self.watcher.summoner.by_id(self.my_region,self.targetID)['name'])
            for x in self.watcher.champion_mastery.by_summoner(self.my_region,self.targetID):
                print("Champion:",self.chNames[x['championId']],
                      "\nChampionLevel:",x['championLevel'],
                      "\nMastery Points:",x['championPoints'],
                      "\nChest Granted?:",x['chestGranted'],"\n")

        elif inputR == 'c':
            print(self.watcher.champion_mastery.by_summoner_by_champion(
                self.my_region,self.targetID,input("Bitte Champion Id eingeben:")))
                #Not Finished

        elif inputR == 's':
            print("\nMastery score of",self.target['name'],":",self.watcher.champion_mastery.scores_by_summoner(self.my_region, self.targetID))

        #print(self.watcher.champion_mastery.by_summoner(self.my_region, userM))

    def userLeagues(self):
        leagueInfo = self.watcher.league.positions_by_summoner(self.my_region, self.targetID)
        print("\nLeagueInfo of:",self.target['name'])
        for i in leagueInfo:
            print("\nQueue Type:",i['queueType'])
            print("Tier:",i['tier'],i['rank'])
            print("LeagueName:",i['leagueName'])
            print("Wins:",i['wins'],"Losses:",i['losses'])
            print("League Points:",i['leaguePoints'])
            print("HotStreak?",i['hotStreak'],"\n")

    def userMasteries(self):
        masterieInfo = self.watcher.masteries.by_summoner(self.my_region, self.targetID)
        print(masterieInfo)
        print("\nMasteries of",self.target['name'])
        for i in masterieInfo['pages']:
            print("Name:", i['name'])

    def userMatch(self):
        matchInfoRecent = self.watcher.match.matchlist_by_account_recent(self.my_region, self.targetAccID)
        print(matchInfoRecent)
        #nicht Fertig

    def userRunes(self):
        runesInfo = self.watcher.runes.by_summoner(self.my_region, self.targetID)
        print(runesInfo)
        #nicht Fertig

    def spectTest(self):
        curGameInfo = self.watcher.spectator.by_summoner(self.my_region, self.targetID)
        print("GameID:",curGameInfo['gameId'])
        print("GameMode:",curGameInfo['gameMode'])
        print("GameType:",curGameInfo['gameType'])
        print("\nParticipants:")
        for i in curGameInfo['participants']:
            print(i['summonerName'], "plays", self.chNames[i['championId']],)
            fLeagueInf = self.watcher.league.positions_by_summoner(self.my_region,i['summonerId'])
            for j in fLeagueInf:
                print("Queue Type:", j['queueType'])
                print("Tier:", j['tier'], j['rank'])
                print("Wins:", j['wins'], "Losses:", j['losses'],"\n")
            print("\n")


def main():
    my_region = 'euw1'

    root = Stalker(my_region)
    while True :
        root.mainloop()
        if(str(input("\nExit[e],Continue[Other Key]"))=='e'):
            exit()
        else:
            root.draw()


main()
input('PRess Enter to exit')
