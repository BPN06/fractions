inp = None

def calculate() :
    global inp
    ran = int(input("Range : "))
    
    for i in range(ran):
        for y in range(ran):
            try:
                out = str(float(i)/float(y))[:8]
                if str(inp)[:8] == out:
                    print(str(i) + "/" + str(y))
                elif str(inp)[:8] == ("-" + out[:7]):
                    print("-" + str(i) + "/" + str(y))
            except:
                pass
                
def get_fractions() :
    global inp
    cal = str(input("Calcul : "))
    
    if cal == "":
        calculate()
    else:
      num = input("Numérateur : ")
      den = input("Dénominateur : ")
      
      fra = (float(num)/float(den))
      
      
      if cal == "+":
          inp = inp + fra
          get_fractions()
      elif cal == "-":
          inp = inp - fra
          get_fractions()
      elif cal == "x":
          inp = inp * fra
          get_fractions()
      elif cal == "/":
          inp = inp / fra
          get_fractions()
    
def start() :
    global inp
    num = input("Numérateur : ")
    den = input("Dénominateur : ")
    
    inp = (float(num)/float(den))
    
    get_fractions()
    
start()
