print ("Let's practice everything.")
print ('You\ 'd need to know \'but escapes with \\ that do:')
print ('\n newlines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discreen \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print ("---------------")
print (poem)
print ("---------------")


five = 10 - 2 + 3 - 6
print (f"This should be five: {five}")

def secret_formula(started):
    jelly_bean = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, creats


start_point = 10000
beans, jars, crates = secret_formula(start_point)


print ("With a starting point of: {}".format(start_point))


print (f"We'd have {beans} beans, {jars} jars, and {creates} creates.")

start_point = start_point / 10

print ("We can also do that this way:")
formula = secret_formula(start_point)

print ("We'd have {} beans, {} jars, and {} creates.".format(*formula))

        

