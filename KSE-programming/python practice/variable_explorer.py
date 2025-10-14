# Explore variables and memory
import sys

# Create different types
name = "Python"
version = 3.12
is_fun = True

# Check types
print(f"name type: {type(name)}")
print(f"version type: {type(version)}")
print(f"is_fun type: {type(is_fun)}")

# Check memory
print(f"\nMemory addresses:")
print(f"name: {hex(id(name))}")
print(f"version: {hex(id(version))}")

# Check sizes
print(f"\nSizes in bytes:")
print(f"name: {sys.getsizeof(name)}")
print(f"version: {sys.getsizeof(version)}")