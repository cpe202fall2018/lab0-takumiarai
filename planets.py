def weight_on_planets():
    earthwt = raw_input ("Enter your weight: ")
    marswt = earthwt * 0.38
    jupiterwt = earthwt * 2.34
    print ("What do you weigh on earth? ", earthwt,
           "\n","\n"
           "On Mars you weigh ", marswt, " pounds.", 
           "\n",
           "On Jupiter you weigh ", jupiterwt, " pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
