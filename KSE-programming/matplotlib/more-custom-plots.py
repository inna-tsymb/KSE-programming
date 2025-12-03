import matplotlib.pyplot as plt

# Colors
# Named: 'red', 'blue', 'green', 'orange', 'purple'
# Hex codes: '#FF0000', '#00FF00', '#0000FF'
# RGB: (0.1, 0.2, 0.5)

# Line styles
plt.plot([1, 2], [1, 2], linestyle='-')   # solid
plt.plot([1, 2], [2, 3], linestyle='--')  # dashed
plt.plot([1, 2], [3, 4], linestyle='-.')  # dash-dot
plt.plot([1, 2], [4, 5], linestyle=':')   # dotted

# Markers
plt.plot([1, 2], [1, 2], marker='o')  # circle
plt.plot([1, 2], [2, 3], marker='s')  # square
plt.plot([1, 2], [3, 4], marker='^')  # triangle
plt.plot([1, 2], [4, 5], marker='*')  # star

# Alpha (transparency): 0.0 to 1.0
plt.plot([1, 2], [1, 2], alpha=0.5)  # 50% transparent