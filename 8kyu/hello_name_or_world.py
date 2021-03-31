# Define a method hello that returns "Hello, Name!" to a given name, or says 
# Hello, World! if name is not given (or passed as an empty String).

# Assuming that name is a String and it checks for user typos to return a 
# name with a first capital letter (Xxxx).

# Examples:

# hello "john"   => "Hello, John!"
# hello "aliCE"  => "Hello, Alice!"
# hello          => "Hello, World!" # name not given
# hello ""       => "Hello, World!" # name is an empty String


def hello(name=None):
  if name == '' or  name == None: return "Hello, World!"
  else:
    fixed_name = name[0].upper() + name[1:].lower()
    return f'Hello, {fixed_name}!'