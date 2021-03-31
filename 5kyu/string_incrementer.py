# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo -> foo1
# foobar23 -> foobar24
# foo0042 -> foo0043
# foo9 -> foo10
# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.

def increment_string(strng):
  ints = '0123456789'; inc_num = '';
  
  for char in strng:
    if ints.find(char) != -1:
      inc_num += char
  
  if inc_num == '': return strng + '1'
  
  inc_length = len(inc_num)
  if inc_length > 4:
    inc_num = inc_num[-4:]
    inc_length = 4
    
  sub_strng = strng[:-inc_length]
  new_value = str(int(inc_num)+1)
  
  diff = inc_length - len(new_value)
  for i in range(diff): sub_strng += '0'
  return sub_strng + new_value