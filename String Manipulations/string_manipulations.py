a = "hello"
print(a[0])
print(a[-1])

#string slicing
a = "Mohammed Jameal"
print(a[0:8])
print(a[2:10:2])
print(a[::-1])

#string concat

x="mohammed"
y="jameal"

print(x+" "+y)

#repetion

print(x*3)

#membership

print("h" in x)
print("a" not in x )

#string methods = using . used for methods

name = "mohammed"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.swapcase())

#search and replace

an = "hello world"
print(an.find("world"))
print(an.index("l"))
print(an.count("l"))
print(an.replace("world","python"))

#checking content

print(an.isupper())
print(an.islower())
print(an.startswith("hello"))
print(an.endswith("world"))
print(an.isdigit())
print(an.isalpha())

#triming

b = "   hello world   "
print(b.strip())
print(b.lstrip())
print(b.rstrip())

#splitting and joining

sentence = "hello world welcome to python"
words = sentence.split()
print(words)

joined_sentence = " ".join(words)
print(joined_sentence)