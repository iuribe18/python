# Global Variable
enemies = "Skeleton"
global_variable = 1

# Global Constant
PI = 3.1416

def increase_enemies():
    enemies = "Zombie"
    global global_variable 
    global_variable +=1
    print(f"Enemies Inside Function (Local Scope): {enemies}")
    print(f"Change a global_variable Inside Function (Local Scope): {global_variable}")

increase_enemies()
print(f"Enemies Outside Function (Global Scope): {enemies}")

def bar():
    my_variable = 9
 
    if 16 > 9:
      my_variable = 16
 
    print(my_variable)
 
bar()