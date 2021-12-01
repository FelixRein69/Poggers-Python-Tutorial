
###########################################################################
#                       ### Variabeln und Typen ###
###########################################################################

# 1) Variablen in Python.

# Eine Variable ist ein Wert, der einem Namen zugewiesen wird. Dies kann man sich ähnlich zu einer Variable aus 
# dem Matheuntericht in der Schule vorstellen. 
# Eine Variable wird in Python mit dem Namen und dann dem Wert deklariert. 
# Dabei gibt es mehrere Typen: 
# - int 
# - float 
#  -

# int                  : Ganzzahlen also -1, 0, 1, ,2     
integer_variable = 1

# float                 : Fließkommazahlen also -0.5, 0.0, 0.5 
float_variable2 = .5 

# String                : Zeichenketten, müssen immer von " umrundet sein zum Beispiel "Hello World" 
string_variable = "Hello World"

# chars                 : Ein einzelnes Zeichen 
char_variable = 'c'

# booleans              : Wahrheitswerte also True oder False 
bool_variable = True 


# Variabeln werden nur durch ihren Namen identifiziert: 
# Das bedeutet variablen, die schon deklariert wurden werden mit einer neuen Zuweisung einfach überschrieben. 
# Dabei können sich auch die Typen ändern. 

variable = 42
variable = "Neuer Wert vom Typ int" 
variable = 42.0                         # Die Variable "variable" hat jetzt den Wert 42.0 vom Typ float 


# Es ist möglich einer Variable konkret zu sagen welchen Typ sie hat indem man hinter den Namen ": [typ]" schreibt. 
# Das heißt aber auch, dass der Wert auf der anderen Seite des "=" entweder vom gleichem Typ ist, oder einfach umgewandelt werden kann. 
# Ein int kann einfach in eine float-Wert umgewandelt werden, da 42 das gleiche wie 42.0 ist. 
# 
# Jedoch kann ein float-Wert nicht immer zu einem Integer richtig umgewandelt werden, da dabei die Nachkommastellen verloren gehen würden. 
# 
# Das Prinzip des "umwandeln" nennt man 'casten'

variable_vom_typ_int : int = 420
#           ^           ^     
#          Name        Typ

variable_vom_typ_float : float = 4


# Variabeln können, nachdem sie deklariert wurden manipuliert werden 
# Für Ints und Floats können die Standard mathematischen Operationen durchgeführt werden. 

variable = 1 
variable_plus = variable + 10 # = 11 

variable_minus = variable - 10 # = -9 

variable_geteilt = variable / 2.0 # = 0.5 

variable_mal = variable * 2 # = 2 


# Sofern der Wert der Variable manipuliert werden soll, also beispielsweise nur plus 5 gerechnet werden soll,
# können auch die Kurzeschreibweise verwendet werden 

variable = 10 
variable += 1 # = variable = variable + 1 
variable -= 1 # = variable = variable - 1 
variable *= 2 # = variable = variable * 2 

# (Aufgabe): 
# Deklariere eine Variable von jedem dir bekannten Typ an. Achte dabei darauf, dass die Namen aussagekräftig und gut lesbar sein sollten. 





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


# (Aufgabe): 
# Gegben sind die beiden Variablen a und b vom Typ float.
# Speichere nun das Ergebniss von der ersten binomischen Formel 
# also a^2 + 2ab + b^2 in einer Variable mit einem passendem Namen: 

a = 10 
b = 5 




# 2) Variablenspeicherung im RAM (Optional) 
# 
# Da ein Computer ausschließlich mit 0,1 arbeitet, kann natürlich nicht "Hello World", 420 oder 0.002 genau so gespeichert werden. 
# Deshalb werden verschiedene Folgen von 0,1 (z.B 00101001) als Zahlen oder Buchstaben interpretiert.
# Hier gehe ich nur ganz kurz auf Ganzzahlen ein. Für einen Programmierer sind diese Konzepte eher unwichtig, jedoch sollte man 
# wenigstens etwas verstehen, wie der Computer eine Variable sieht. 
# 
# Terminologie:
# 
#   Eine Speicherzelle, kann 0 oder 1 sein. Das nennt man "bit"
#   Da ein Bit nur für den Wahrheitswert True oder False stehen kann, sind int, float, String und chars als Kombinationen von 
#   mehreren Bits dargestellt.
#   
#   4 Bit´s nennt man ein byte z.B (0000) ist ein byte: 
# 
# 
# Eine Variable ist also eine Kombination aus bits bspw. (10010010001). Das bedeutet auc 
# 