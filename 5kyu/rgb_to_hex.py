# The rgb function is incomplete. Complete it so that passing in RGB decimal values will 
# result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. 
# Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

def rgb(r, g, b):
  hex = '0123456789ABCDEF'
  
  def hex_code(val):
    if val <= 0: return '00'
    elif val > 255: return 'FF'
    else:
      num_split = str(val/16).split('.')
      first = hex[int(num_split[0])]
      second = hex[int(float('0.' + num_split[1]) * 16)]
      return first + second
  
    return hex_code(r) + hex_code(g) + hex_code(b)