# Diccionario

informacion_personal = {
    'nombre':'Sonia',

    'ciudad':'Borja',
    'provincia':'Napo',
}
print('----------------------')
print('Diccionario Original')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')

# Clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal['ciudad'] = 'Lumbaqui'
informacion_personal['provincia'] = 'Sucumbios'

# Nueva clave-valor al diccionario "profesion"
informacion_personal['profesion'] = 'estudiante'

# Verifica si la clave "telefono" existe
if 'telefono' not in informacion_personal:
    informacion_personal['telefono'] = '0991782411'



print('----------------------')
print('Diccionario Modificado')
print('----------------------')
for clave, valor in informacion_personal.items():
    print(f'{clave} : {valor}')