"""
Tipos de Datos Primitivos

- Numeric (integer, float)
- Text (string)
- Booleanos (True / False)


Funcion que utilizamos para saber el tipo de una variable:
* type(<value>)

"""



"""
Numeric
* int
* float
* complex
"""
# Ejemplos de int
from this import d


int_1 = 1
print(type(int_1))

# Ejemplos de float
float_1 = 1.
print(type(float_1))

# Adding integers
n_obs = 100
print(n_obs + 10)

# Adding integers and floats
int_1 = 1
float_1 = 1.0
suma = int_1 + float_1

print(suma)
print(type(suma))

# Adding integers and floats (with signals)
int_1 = -1
float_1 = 1.1
suma = int_1 + float_1
print(suma)

# Ejemplos de exponenciales
exp_1 = 3e2

"""
Booleans
* True
* False
"""
bool_true = True
bool_false = False
print(type(bool_true),type(bool_false))

# Comparison - Equality (== / !=)
print(1 == 1) # True
print(1 != 1) # False

# Comparing integers and floats 
a = 1
b = 1.0
a == b # True

# Comparing boolean values to 0,1
1 == True # True
0 == False # True


# Strings - Cadenas de Texto
# type: str

# Podemos definir las str de distintas formas:
# - ''
# - ""
# - """ (multilineas)


name = 'roberto'
Name = "roberto"
NAME = """roberto"""
name == Name # True
name == NAME # True
type(name) # str

# Example of multiline string
multiline_str = """My name is Roberto
and I'm from Brazil.
"""
print(multiline_str)

# Using quotes in strings
text_1 = "'My name is Roberto' said him."
print(text_1)

text_2 = "My name is Roberto"
print(text_2)

###################################
# STRING METHODS
###################################

# -- capitalize()
name = "roberto"
capitalized_name = name.capitalize()
print(name, capitalized_name)

# -- lower()
name = "RobertO KrameR"
name.lower()

"Roebrto KrameRR 123!!5 DDDD".lower()
# 'roebrto kramerr 123!!5 dddd'

# -- upper()
name = "roberto kramer"
name.upper()
# 'ROBERTO KRAMER'
"roberto kramer".capitalize().upper()
# 'ROBERTO KRAMER'

# -- strip()
name = "   Roberto Kramer"
name.strip()
# 'Roberto Kramer'

"    Roberto    Kramer   Pinto     ".strip()
#'Roberto    Kramer   Pinto'

",,,,,,,,Roberto Kramer  ......".strip(",.")
# 'Roberto Kramer  '

",,,,,,,,Roberto Kramer  ......".strip(",.").strip()
# 'Roberto Kramer'

",,,,,,,,Roberto Kramer  ......".strip(",. R")
#'oberto Kramer'

# -- lstrip(), rstrip()

",,,,,,,,Roberto Kramer  ......".lstrip(",. R")
# 'oberto Kramer  ......'

",,,,,,,,Roberto Kramer  ......".rstrip(",. R")
#',,,,,,,,Roberto Kramer'

# -- startswith()
name = "Madrid"
name.startswith("M") # True
name.startswith("m") # False
name.startswith("Mad") # True

# -- endswith()
name = "Madrid"
name.endswith("D") # False
name.upper().endswith("D") # True

"      Jorge      ".strip().lower().startswith("j") # True

# Using reverted indexes
name = "Barcelona"
name.endswith("ona",0,-1)
name.endswith("ona",0,-1)


name = "Valencia"
name.startswith("l",2) # True

name = "Valencia"
name.endswith("l",0,3) # True

name = "Valencia"
name.endswith("l",0,2) # False

# -- title()
" hello world! Python is great".title()
# ' Hello World! Python Is Great' 
" hello world! Python,is great".title() 
# ' Hello World! Python,Is Great'

# -- replace()
# str.replace(old, new, count)
"12345".replace("123","0")
# '045'

"    Roberto Kramer     ".replace(" ","")
# 'RobertoKramer'

"    Roberto Kramer     ".replace(" ","",4)
#'Roberto Kramer     '

"    Roberto Kramer     ".replace(" ","",5)
#'RobertoKramer     '

