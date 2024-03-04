# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad 1
        [   # Semana 1
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 35},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 85},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 14},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 42},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 75}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 86},
            {"day": "Miércoles", "temp":52},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 91},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 45},
            {"day": "Martes", "temp": 46},
            {"day": "Miércoles", "temp": 85},
            {"day": "Jueves", "temp": 43},
            {"day": "Viernes", "temp": 52},
            {"day": "Sábado", "temp": 12},
            {"day": "Domingo", "temp": 96}
        ]
    ],
    [   # Ciudad 2
        [   # Semana 1
            {"day": "Lunes", "temp": 62},
            {"day": "Martes", "temp": 64},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 73},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp":79},
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 63},
            {"day": "Martes", "temp": 58},
            {"day": "Miércoles", "temp": 70},
            {"day": "Jueves", "temp": 72},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 77},
            {"day": "Domingo", "temp": 96}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 75},
            {"day": "Martes", "temp": 65},
            {"day": "Miércoles", "temp": 68},
            {"day": "Jueves", "temp": 85},
            {"day": "Viernes", "temp": 72},
            {"day": "Sábado", "temp": 35},
            {"day": "Domingo", "temp": 80}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 52},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 69},
            {"day": "Jueves", "temp": 82},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 80}
        ]
    ],
    [   # Ciudad 3
        [   # Semana 1
            {"day": "Lunes", "temp": 78},
            {"day": "Martes", "temp": 92},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp":61},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp":68},
            {"day": "Domingo", "temp": 66}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp":56},
            {"day": "Martes", "temp": 53},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 90},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 81}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 53},
            {"day": "Martes", "temp": 93},
            {"day": "Miércoles", "temp": 95},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 89},
            {"day": "Sábado", "temp": 42},
            {"day": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 28},
            {"day": "Martes", "temp": 90},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 89},
            {"day": "Viernes", "temp": 86},
            {"day": "Sábado", "temp": 78},
            {"day": "Domingo", "temp": 80}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)