import pandas as pd

df = pd.read_csv("Libary.csv")

array = []

movieLengths = {"Mickeys House of Villains": 68, "Tom Segura Disgraceful": 71, "Secrets in the Fall": 90,
                         "Banana in a Nutshell": 88, "Dear Etranger": 127, "Believe in Me": 131, "Wont Back Down": 121,
                         "Columbus": 100, "Mountain": 74, "Coco": 105,
                         "Phineas and Ferb the Movie Across the 2nd Dimension": 78, "American Made": 115,
                         "Valerian and the City of a Thousand Planets": 137, "Boyka Undisputed": 86,
                         "Power Rangers": 124, "I Tawt I Taw a Puddy Tat": 4, "Peaceful Warrior": 120,
                         "The Founder": 115, "Scrat Spaced Out": 15, "Zero Days": 116,
                         "The Beat That My Heart Skipped": 108, "Tristan + Isolde": 125, "To Save a Life": 120,
                         "Undisputed": 96, "Diary of a Wimpy Kid Rodrick Rules": 99, "Arc": 113, "Bon Cop Bad Cop": 116,
                         "And Everything Is Going Fine": 89, "Kokoda 39th Battalion": 92,
                         "Theory of Obscurity A Film About the Residents": 87, "Dragon Ball Z Resurrection F": 93,
                         "King Solomons Mines": 100, "The Condemned": 113, "Moondance Alexander": 94,
                         "American Ultra": 96, "Sherrybaby": 96, "Winnie the Pooh": 63, "Water for Elephants": 120,
                         "Wasted on the Young": 97, "Undisputed 3 Redemption": 96, "TRON Legacy": 125,
                         "Trick r Treat": 82, "Tomorrow When the War Began": 103,
                         "Tom and Jerry in Shiver Me Whiskers": 75, "Tinker Bell and the Lost Treasure": 81,
                         "Tinker Bell and the Great Fairy Rescue": 76, "Tinker Bell": 78, "Think Like a Man": 122,
                         "The Switch": 101, "The Perfect Host": 93, "The Muppets": 103, "The Ledge": 101,
                         "The Color of Magic": 191, "The Call": 94, "The Blind Side": 129, "The Big Year": 100,
                         "The 84th Annual Academy Awards": 210, "Tangled": 100, "Take Me Home Tonight": 97,
                         "SupermanBatman Apocalypse": 78, "Super": 96, "Stand Up Guys": 95,
                         "Shes Out of My League": 104, "Safety Not Guaranteed": 86, "Ruby Sparks": 104,
                         "Resolution": 93, "Resident Evil Degeneration": 97, "Punk Love": 98, "Promised Land": 106,
                         "Pope Joan": 149, "Polar Bears A Summer Odyssey": 90, "Plastic": 102,
                         "Pirates of the Caribbean On Stranger Tides": 137, "People Like Us": 114,
                         "Paranormal Activity": 86, "Nitro Circus The Movie": 92, "Mr Poppers Penguins": 94,
                         "Morning Glory": 107, "Midnight in Paris": 94, "Mickey Donald Goofy The Three Musketeers": 68,
                         "Men in Black 3": 106, "Marley & Me": 115, "Madagascar 3 Europes Most Wanted": 93,
                         "Loosies": 89, "Life as We Know It": 114, "Letters to Juliet": 105, "Leap Year": 100,
                         "Johnny English": 88, "Jackass 35": 101, "Its Complicated": 120, "In a World": 93,
                         "Hysteria": 100, "Hounddog": 102, "Hot Rod": 88, "Green Lantern Emerald Knights": 84,
                         "Going the Distance": 102, "Gimme Shelter": 101, "Flipped": 90, "Fanboys": 90,
                         "Everybodys Fine": 100, "Emperor": 105, "Diary of a Wimpy Kid": 92, "Catwoman": 104,
                         "Daydream Nation": 98, "Crooked Arrows": 105, "Crazy Stupid Love": 118, "Courageous": 129,
                         "Cirque du Soleil Worlds Away": 91, "Chimpanzee": 78, "Chasing Mavericks": 116,
                         "Charlie St Cloud": 99, "Chalet Girl": 96, "Born to Be Wild": 40, "Being Flynn": 102,
                         "Batman Year One": 64, "Batman Mystery of the Batwoman": 75, "Balto Wolf Quest": 76,
                         "All-Star Superman": 76, "African Cats": 89, "Adventureland": 107, "Adore": 112,
                         "A Little Bit of Heaven": 106, "10 Years": 100, "Toomelah": 106,
                         "Bah Humduck A Looney Tunes Christmas": 46, "Pumpkin and Mayonnaise": 93,
                         "Caroline and Jackie": 85, "The Mummy": 124, "Sleepless": 95, "Pompeii": 105,
                         "Alvin and the Chipmunks The Road Chip": 92, "The Legend of Hercules": 99, "RIPD": 96,
                         "The Osiris Child": 95, "The Smurfs": 103}


movie_lengths = {"Blades of Glory": 93, "Black or White": 121, "Terra Mater Big Bugs - Kleine Krabbler ganz groß": 45, "The Boss Baby and Tims Treasure Hunt Through Time": 24, "Killem All": 96, "Escape from Planet Earth": 89, "Death Race 2050": 93, "Norm of the North": 90, "Saints and Soldiers The Void": 95, "The Debt Collector": 96, "Mythica The Godslayer": 118, "Happy Feet Two": 99, "Tekken Blood Vengeance": 92, "Dirty Movie": 91, "Stuck": 84, "End of a Gun": 87, "Hangman": 98, "The Big Wedding": 89, "The Last Song": 107, "Neighbour No 13": 115, "Beauty & the Briefcase": 83, "The Toxic Avenger The Musical": 134, "Undeserved": 95, "War Eagle Arkansas": 93, "Park": 86, "Social Animals": 90, "Adam Patel Real Magic": 48, "Eagles of Death Metal Nos Amis": 84, "Beirut": 109, "The Tree": 100, "Blind Dating": 95, "Siberia": 105, "Hana": 127, "Girl Followed": 89, "Super Troopers 2": 99, "Kittenhood": 51, "The Honey Killer": 95, "Robin Williams Come Inside My Mind": 116, "Rosy": 92, "Iliza Elder Millennial": 72, "Path of Blood": 91, "Waterschool": 78, "Comedy Central Roast of Bruce Willis": 85, "The Incantation": 98, "Barking Dogs Never Bite": 110, "Pina": 106, "Upgrade": 100, "StreetDance 3D": 98, "Romans": 91, "The Land Before Time X The Great Longneck Migration": 84, "The Keeping Hours": 91, "I Love You Too": 107, "S&man": 84, "Knucklehead": 100, "The Bang Bang Club": 106, "The Echo": 90, "Waikiki Brothers": 113, "My Teacher My Obsession": 90}


for index, row in df.iterrows():
    length = row["Length"]
    if length == 0:
        print(row["Title"])
        """
        try:
            df["Length"].iloc[index] = movie_lengths[row["Title"]]
        except:
            pass

print(df)

df.to_csv("Libary.csv", index=False)
"""