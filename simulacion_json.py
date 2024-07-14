import json

# Datos simulados de la tabla
datos = [
    {
        "id": 3,
        "nombre": "Robo a mano armada",
        "descripcion": "Delito grave que involucra el uso de armas para robar.",
        "usuarios_id": 1
    },
    {
        "id": 4,
        "nombre": "Hurto",
        "descripcion": "Apropiación de bienes ajenos sin el uso de violencia.",
        "usuarios_id": 2
    },
    {
        "id": 5,
        "nombre": "Secuestro",
        "descripcion": "Privación de la libertad de una persona contra su voluntad.",
        "usuarios_id": 3
    },
    {
        "id": 6,
        "nombre": "Extorsión",
        "descripcion": "Obtención de bienes o dinero mediante amenazas o coerción.",
        "usuarios_id": 4
    },
    {
        "id": 7,
        "nombre": "Asesinato",
        "descripcion": "Acto de matar a alguien de manera intencional.",
        "usuarios_id": 5
    },
    {
        "id": 8,
        "nombre": "Falsificación",
        "descripcion": "Creación o alteración de documentos o bienes falsos.",
        "usuarios_id": 6
    }
]

# Convertir a formato JSON
datos_json = json.dumps(datos, indent=4)

# Mostrar el JSON generado
print(datos_json)
