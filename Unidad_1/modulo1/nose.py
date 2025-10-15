from platform import platform, machine, system, version
from platform import python_implementation, python_version

print(python_implementation(), end=' ')
for n in python_version():
    print(n, end="")
print()
print(system(), end=' ')
print(version())
print(machine())
print(platform())
print(platform(1))
print(platform(0, 1))

