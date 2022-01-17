# Using Python External and Built In Modules

import random

random_number = random.randint(1, 10)
print(random_number)

"""
    random.randint(a,b) ye function a se b ke beech koi 
    bhi value de dega jisme 'a' or 'b' dono hi included 
    rhte hai. Jaise ki upar wale example me (1, 10) ka 
    matlab hai ki 1 se 10 ke beech koi bhi no o/p dega.
"""




lst = ["Star Plus", "DD1", "Aaj Tak", "Aakash Kumar"]
random_choice = random.choice(lst)
print(random_choice)

"""
    random.choice(lst), ye function list ya dictionary ya 
    sets, dictionary me se koi bhi ek random element nikal 
    kar de dega.
"""




q = random.randrange(3, 20, 2)
"""
    syntax - random.randrange( start, stop, step)
"""
print(q)





r = random.uniform(1, 10)
"""
    Returns a random float number between two given parameters
"""
print(r)


s = random.betavariate(5, 2)
"""
    Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)
"""
print(s)
