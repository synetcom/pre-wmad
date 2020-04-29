# Convert from Fahrenheit to Celcius
# Convert from Celsius to Fahrenheit

# Fahrenheit 212 = Celcius 100
# Fahrenheit 212-180 = 32 = Celcius 0
# The range of Fahrenheit 32 - 212
# Same as 1 - 100 in Celcius
# Use def(Function)


def celcius(f):
    c = (5 / 9) * (f - 32)
    return c


def fahrenheit(c):
    f = (9 / 5) * c + 32
    return f


# function fahrenheit(){
#     let celcius = Number(prompt("Tell me a celcius degree"));
#     let farenheit = (9 / 5) * celcius +32;
#     document.write(fahrenheit)
# # }
# print(celcius(int(input("Tell me a Fahrenheit degree"))))
print(fahrenheit(int(input("Tell me a Celcius degree"))))
