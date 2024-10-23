'''1. Create a function that converts temperature from Celsius to Fahrenheit and vice versa.
The function accepts two parameters, namely the temperature value and the temperature unit
('C' for Celsius, 'F' for Fahrenheit).'''

# Input unit suhu dan nilai suhu dari pengguna
unit_temperature = input("Ketikan yang mau di konversi (C/F): ")
value_temperature = float(input("Masukan nilai suhu yang ingin dikonversi: "))

# Fungsi untuk konversi suhu
def temperature_funtion(value_temperature, unit_temperature):
    if unit_temperature == 'C':
        # Konversi dari Celsius ke Fahrenheit
        return (value_temperature * 9/5) + 32
    else:
        # Konversi dari Fahrenheit ke Celsius
        return (value_temperature - 32) * 5/9
    
# Panggil fungsi dan simpan hasilnya
konvert_temperature = temperature_funtion(value_temperature, unit_temperature)