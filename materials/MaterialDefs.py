from Material import Material

class MaterialDefs:

    #Taken from: http://devernay.free.fr/cours/opengl/materials.html

    GOLD = {
	"materialName": "GOLD",
	"ambient": [0.24725, 0.1995, 0.0745, 1.0],
	"diffuse":	[0.75164, 0.60648, 0.22648, 1.0],
	"specular": [0.628281, 0.555802, 0.366065, 1.0],
	"shininess": 0.4 * 128.0
    }

    RED_PLASTIC = {
	"materialName": "RED_PLASTIC",
	"ambient": [0.0, 0.0, 0.0, 1.0],
	"diffuse":	[0.5, 0.0, 0.0, 1.0],
	"specular": [0.7, 0.6, 0.6, 1.0],
	"shininess": 0.25 * 128.0
    }

    GREEN_PLASTIC = {
        "materialName": "GREEN_PLASTIC",
        "ambient": [0.0, 0.0, 0.0, 1.0],
	    "diffuse":	[0.1, 0.35, 0.1, 1.0],
	    "specular": [0.45, 0.55, 0.45, 1.0],
	    "shininess": 0.25 * 128.0
    }

    WHITE_PLASTIC = {
        "materialName": "WHITE_PLASTIC",
        "ambient": [0.0, 0.0, 0.0, 1.0],
	    "diffuse":	[0.55, 0.55, 0.55, 1.0],
	    "specular": [0.70, 0.70, 0.70, 1.0],
	    "shininess": 0.25 * 128.0
    }

    BLACK_PLASTIC = {
        "materialName": "BLACK_PLASTIC",
        "ambient": [0.0, 0.0, 0.0, 1.0],
	    "diffuse":	[0.01, 0.01, 0.01, 1.0],
	    "specular": [0.50, 0.50, 0.50, 1.0],
	    "shininess": 0.25 * 128.0
    }

    YELLOW_PLASTIC = {
        "materialName": "YELLOW_PLASTIC",
        "ambient": [0.0, 0.0, 0.0, 1.0],
	    "diffuse":	[0.5, 0.5, 0.0, 1.0],
	    "specular": [0.60, 0.60, 0.50, 1.0],
	    "shininess": 0.25 * 128.0
    }

    CHROME = {
	"materialName": "CHROME",
	"ambient": [0.25, 0.25, 0.25, 1.0],
	"diffuse":	[0.4, 0.4, 0.4, 1.0],
	"specular": [0.774597, 0.774597, 0.774597, 1.0],
	"shininess": 0.6 * 128.0
    }