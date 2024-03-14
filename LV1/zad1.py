hours = input('Radni sati: ')
hours = hours.split(' ')[0]
hours = int(hours)

pay = input('eura/h: ')
pay = pay.split(' ')[0]
pay = float(pay)

print(f"Ukupno: {hours*pay} eura")