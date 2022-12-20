
def greet(**kwargs):
    if kwargs:
        print(f"Hello, {kwargs['name']} {kwargs['age']}!")
    else:
        print("Hello, World!")

greet()  # Output: "Hello, World!"
greet(name="John", age="19")  # Output: "Hello, John!"

def my_function(arg1, arg2, **kwargs):
  # Do something with the regular arguments
  result = arg1 + arg2
  
  # Access the keyword arguments
  for key, value in kwargs.items():
    result += value
    
  return result

result = my_function(1, 2, a=3, b=4, c=5)
print(result)  # Output: 15


