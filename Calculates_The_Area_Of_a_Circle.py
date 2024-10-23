'''2. Use the lambda function to create a function that calculates the area of a circle!
Input is the length from the center of the circle to the border (jari-jari lingkaran).'''

# Mengimpor library math
import math

# Lambda function untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r ** 2

# Input jari-jari dari pengguna
radius = float(input("Masukkan jari-jari lingkaran: "))
