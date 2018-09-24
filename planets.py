def weight_on_planets():
    earthwt = int(input("What do you weigh on earth? "))
    marswt = earthwt * 0.38
    jupiterwt = earthwt * 2.34
    print("\nOn Mars you would weigh "+ str(marswt) + " pounds.\nOn Jupiter you would weigh " +
          str(jupiterwt) + " pounds.")

if __name__ == '__main__':
    weight_on_planets()
