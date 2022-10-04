VARIABLE_STR = "Roberto"
VARIABLE_NUM = 123
MY_LIST = [1,2,3,4,5]
MY_DICT = {
    "name":"Roberto",
    "city":"Madrid"
}

def print_input(x:str="No Input"):
    """Prints the function input
    """
    print(f"This is your input: {x}")

class User():
    def __init__(self,name:str):
        self.name = name

if __name__ == "__main__":
    # Solo se ejecuta en caso de llamar directamente a este script
    print("Modulo 1 Fully executed.")