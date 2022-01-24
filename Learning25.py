import time

initial = time.time()
# print(initial)

k = 0
while k<5:
    print("This is While Loop")
    k+=1
print("Execution time for while loop is:", time.time()-initial, "seconds")

# print("\t")

initial2 = time.time()
for i in range(5):
    print("This is for loop")
print("Execution time for for loop is:", time.time()-initial2, "seconds")

print("\n\n")



# Functions In time() modules in Python.
#  [1] time.time() - It measures the number of seconds.
#  [2] time.sleep(sec) - No of seconds we want to sleep that program.
#  [3] time.timezone() - It returns the offset of the local timezone in UTC format
#  [4] time.tzname() - It returns a tuple containing the local non-DST  and DST time zones.
#  [5] time.asctime(time.localtime(time.time())).
#  [6] time.ctime() - It returns the current time .



d= time.timezone
print("d=", d, "\n")

e = time.tzname
print("e=", e, "\n")

f = time.asctime(time.localtime(time.time()))
print("f=", f, "\n")

g= time.ctime()
print("g=", g, "\n")


# Miscellaneous Program


for i in range(1, 5):
    for j in range(1, i+1):
        print("*", end="")
    print()