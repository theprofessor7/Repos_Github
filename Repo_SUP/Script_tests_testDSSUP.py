import time

def exercices(*args,exercice):
     try:
          start_test = time.time()
          for name, value in args: globals()[name]=value
          print("========================== début du test =========================="+'\n')

          #-----------------------------------------condition(s) que l'on teste
          #--------------------------------------------------------------------
          if exercice==1:
               assert double([2,3,4,19,6,15,8,7])==5, "La moyenne des nombres pairs n'est pas correcte "
          elif exercice==2:
               assert tets([2, 15, 8, 9, 4])== [9], "La liste retournée par la fonction test() n'est pas exacte"

          #--------------------------------------------------------------------
          #--------------------------------------------------------------------

          stop_test = time.time()
          tps = stop_test -start_test
          print ("Test réussi en ",round(tps,2)," secondes",'\n')
          print("=========================== fin du test ===========================")

     except (AssertionError, NameError) as err:
          stop_test = time.time()
          tps = stop_test -start_test
          print(err,"\n")
          print ("Test échoué en ",round(tps,2)," secondes",'\n')
          print("=========================== fin du test ===========================")


