print("Hello User What Is The Wind Chill Today?")
windChill = int(input())

if windChill <= -25:
    print("No School!!!")

elif windChill >= -9:
    print("Theres School ):")

elif windChill in range(-24, -10):
    print("Maybe school")

elif windChill >= 60:
    print("Bruh its summer")
