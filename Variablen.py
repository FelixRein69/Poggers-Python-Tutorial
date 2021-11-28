# Eine Variable wird in Python mit dem Namen und dann dem Wert deklariert. 
# Dabei ist mehrere Typen: 

# int                   : Ganzzahlen also -1, 0, 1, ,2,             modeliert teilweise die Natürlichen Zahlen 
integer_variable = 1

# float                 : Fließkommazahlen also -0.5, 0.0, 0.5      modeliert teilweise die Reellen Zahlen 
float_variable = 0.5 # .5 und 0.5 ist das gleiche 
float_variable2 = .5 

# String                : Zeichenketten, müssen immer von " umrundet sein zum Beispiel "Hello World" 
string_variable = "Hello World"

# chars                 : Ein einzelnes Zeichen 
char_variable = 'c'

# booleans              : Wahrheitswerte also True oder False 
bool_variable = True 



# Variabeln werden nur durch ihren Namen identifiziert: 
# Das bedeutet variablen, die schon deklariert wurden werden mit einer neuen Zuweisung einfach überschrieben. 
# Dabei können sich auch die Typen ändern 
variable = 42
variable = "Neuer Wert vom Typ int" 
variable = 42.0


# Variabeln können, nachdem sie deklariert wurden manipuliert werden 
# Für Ints und Floats können die Standard Mathe operationen durchgeführt werden 

variable = 1 
variable2 = variable + 10 # = 11 

variable3 = variable - 10 # = -9 

variable4 = variable / 2.0 # = 0.5 

variable5 = variable * 2 # = 2 



# Sofern die Variable nur manipuliert werden soll und nicht das Ergebniss in einer neuen Variable gespeichert werden soll
# können auch die Kurzeschreibweise verwendet werden 

variable = 10 
variable += 1 # = variable = variable + 1 
variable -= 1 # = variable = variable - 1 
variable *= 2 # = variable = variable * 2 

# (Aufgabe): 
# Deklariere eine Variable von jedem dir bekannten Typ an. Achte dabei darauf, dass die Namen aussagekräftig sein sollten. 





# (Aufgabe): 
# Manipuliere die variable "variable" folgerdermaßen: 
#   - addiere 10  
#   - subtrahiere 69 
#   - multiplieziere mit 5 

variable = 10 



# Variabeln können auch nicht nur statischen Werten wie 4, 3.0 oder "Hello World" zugewiesen werden, sondern auch anderen variablen 

variable1 = 100 
variable2 = variable1 # variable2 hat nun den Wert 100 
# Wenn wir variable1 verändern ändert sich jedoch NICHT der Wert von variable2. 
variable1 += 10 
# variable1 = 110, variable2 = 100 





