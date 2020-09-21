nimi = input("Sisestage oma nimi: ")
lubatud = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik = int(input("Sisestage tegelik kiirus (km/h): "))
trahv = (tegelik - lubatud)*3
minimaal = min(190,trahv)
print(nimi+", kiiruse ületamise eest on teie trahv " + str(minimaal) + " eurot.")
