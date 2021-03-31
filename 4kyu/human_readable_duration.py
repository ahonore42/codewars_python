# Your task in order to complete this Kata is to write a function which formats a duration, given as 
# a number of seconds, in a human-friendly way.

# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, 
# the duration is expressed as a combination of years, days, hours, minutes and seconds.

# It is much easier to understand with an example:

# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.

# Note that spaces are important.

# Detailed rules
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive 
# integer and one of the valid units of time, separated by a space. The unit of time is used in 
# plural if the integer is greater than 1.

# The components are separated by a comma and a space (", "). Except the last component, which is 
# separated by " and ", just like it would be written in English.

# A more significant units of time will occur before than a least significant one. Therefore, 1 
# second and 1 year is not correct, but 1 year and 1 second is.

# Different components have different unit of times. So there is not repeated units like in 5 seconds 
# and 1 second.

# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds 
# is not valid, but it should be just 1 minute.

# A unit of time must be used "as much as possible". It means that the function should not return 61 
# seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must 
# not be greater than any valid more significant unit of time.


def format_duration(seconds):
  if not seconds: return 'now'
  f_date = []
  
  s = int(seconds % 60)            
  m = int(((seconds - s)/60) % 60)
  h = int(((seconds - (60*m) - s)/3600) % 24 )
  d = int(((seconds - (3600*h) - (60*m) - s) / 86400) % 365)
  y = int(((seconds - (86400 * d) - (3600*h) - (60*m) - s)/31536000))
  
  if y > 0:
    f_date.append(f'{y} years' if y > 1 else f'{y} year')
  if d > 0:
    f_date.append(f'{d} days' if d > 1 else f'{d} day')
  if h > 0:
    f_date.append(f'{h} hours' if h > 1 else f'{h} hour')
  if m > 0:
    f_date.append(f'{m} minutes' if m > 1 else f'{m} minute')
  if s > 0:
    f_date.append(f'{s} seconds' if s > 1 else f'{s} second')
  
  if len(f_date) > 1: 
    f_date[-1] = f'and {f_date[-1]}'
    f_date = ', '.join(f_date)
    remove = f_date.rfind(',')
    return f_date[0:remove] + f_date[remove+1:]
  return f_date[0]