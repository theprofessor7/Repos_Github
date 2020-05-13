import time,IPython.core.display
from IPython.display import Javascript

def exercices(*args,exercice):
     try:
          start_test = time.time()
          for name, value in args: globals()[name]=value
          print("========================== début du test =========================="+'\n')

          #-----------------------------------------condition(s) que l'on teste
          #--------------------------------------------------------------------
          if exercice==2:
               assert moyenne([1,9,15])==12, "La moyenne des nombres impairs et multiples de trois n'est pas correcte "
          elif exercice==3:
               assert XOR(False, False)== False, "Le résultat retourné par XOR n'est pas exact"
	       assert XOR(False, True)== True, "Le résultat retourné par XOR n'est pas exact"
	       assert XOR(True, False)== True, "Le résultat retourné par XOR n'est pas exact"
	       assert XOR(True, True)== False, "Le résultat retourné par XOR n'est pas exact"

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

def eval_compteur(cpt):
    print("Vous avez quitté",cpt,"fois la page")
    
# Commandes Javascript pour bloquer les accès Ctrl+C/Ctrl+V aux étudiants + compteur de sorties
 
jscode_cmd = """
document.body.addEventListener('keydown', event => {
	
  if (event.ctrlKey && 'cvxspwuaz'.indexOf(event.key) !== -1) {
      event.preventDefault()}})
	  
jQuery(document).bind("contextmenu", function(e) {
    e.preventDefault();});
var cpt=0;
window.addEventListener('blur', (event) => {
    cpt=cpt+1
    if cpt > 5
    	alert("Vous n'avez pas le droit de quitter la page")
    IPython.notebook.kernel.execute("cpt = '" + cpt + "'")
    Jupyter.notebook.execute_cells([5]);
    
});
"""
display(IPython.core.display.Javascript(jscode_cmd))
print("Vous pouvez commencer l'épreuve")
