def weight_on_planets():
    earthwt = int(input("Enter your weight: "))
    marswt = earthwt * 0.38
    jupiterwt = earthwt * 2.34
    print("What do you weigh on earth? \nOn Mars you weigh "
          + str(marswt) + " pounds.\nOn Jupiter you weigh " + str(jupiterwt) + " pounds.")

if __name__ == '__main__':
    weight_on_planets()
