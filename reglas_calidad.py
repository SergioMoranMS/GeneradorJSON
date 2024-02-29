dic_reglas_JSON = {
    "Prerequisitos":{
        "codigo":"100",
        "parametros":{
            "FIELDS": ""
        },
    },
    "Nulos":{
        "codigo":"101",
        "parametros": {
            "FIELDS" : "",
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Duplicados":{
        "codigo":"102",
        "parametros":{
            "FIELDS" : "",
            "THRESHOLD" : "",
            "REPETITIONS_NUMBER" : "", 
            "WRITE" : ""
        },
    },
    "Integridad Referencial":{
        "codigo":"103",
        "parametros":{
            "FIELDS" : "",
            "INPUT" : "",
            "TYPE" : "", 
            "PATH" : "", 
            "HEADER" : "", 
            "DELIMITER" : "", 
            "REFERENCE_FIELDS" : "", 
            "ACCOUNT" : "", 
            "KEY" : "", 
            "THRESHOLD" : "", 
            "WRITE" : "",
            "HOST" : "",
            "PORT" : "",
            "DB_NAME" : "",
            "DB_TABLE" : "",
            "DB_USER" : "",
            "DB_PSWD" : "",
            "TEMP_PATH" : ""
        },
    },
    "Formato Fecha":{
        "codigo":"104",
        "parametros":{
            "FIELDS" : "", 
            "FORMAT_DATE" : "",
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Rango":{
        "codigo":"105",
        "parametros":{
            "FIELDS" : "", 
            "MIN_RANGE" : "",
            "INCLUDE_LIMIT_LEFT" : "", 
            "MAX_RANGE" : "", 
            "INCLUDE_LIMIT_RIGHT" : "", 
            "INCLUSIVE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Catálogo":{
        "codigo":"106",
        "parametros":{
            "FIELDS" : "",
            "VALUES" : "",
            "THRESHOLD" : "",
            "WRITE": ""
        },
    },
    "Caracteres Prohibidos":{
        "codigo":"107",
        "parametros":{
            "FIELDS" : "",
            "VALUES" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Tipo Dato(CSV)":{
        "codigo":"108",
        "parametros":{
            "FIELDS" : "", 
            "DATA_TYPE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Composición":{
        "codigo":"109",
        "parametros":{
            "FIELDS" : "", 
            "VALUES" : "", 
            "DELIMITER" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
            },
    },
    "Longitud":{
        "codigo":"110",
        "parametros":{
            "FIELDS" : "", 
            "MIN_RANGE" : "", 
            "MAX_RANGE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Tipo Dato(Parquet)":{
        "codigo":"111",
        "parametros":{
            "FIELDS" : "", 
            "DATA_TYPE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Formato Numerico":{
        "codigo":"112",
        "parametros":{
            "FIELDS" : "", 
            "MAX_INT" : "", 
            "SEP" : "", 
            "NUM_DEC" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Calculadora":{
        "codigo":"113",
        "parametros":{
            "FIELDS" : "", 
            "INPUT_VAL" : "", 
            "OPERATOR" : "", 
            "ERROR_VAL" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Analisis Estadistico":{
        "codigo":"114",
        "parametros":{
            "FIELDS" : ""
        }
    },
    "Rango Fechas":{
        "codigo":"115",
        "parametros":{
            "FIELDS" : "", 
            "MIN_RANGE" : "",
            "MAX_RANGE" : "", 
            "DIFFERENT_UNIT" : "", 
            "REFERENCE_DATE" : "", 
            "FORMAT_DATE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
            },
    },
    "Condicional":{
        "codigo":"116",
        "parametros":{
            "CONDITION" : "", 
            "FILTER_LIST" : "", 
            "QUALITY_FUNCTION" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Valor en posicion especifica":{
        "codigo":"117",
        "parametros":{
            "FIELDS" : "", 
            "INITIAL_POSITION" : "", 
            "FINAL_POSITION" : "", 
            "EXPECTED_VALUE" : "", 
            "THRESHOLD" : "", 
            "WRITE" : ""
        },
    },
    "Valor en Tendencia":{
        "codigo":"119",
        "parametros":{
            "FIELDS" : "",
            "METHOD" : "",
            "THRESHOLD" : "",
            "WRITE" : ""
        },
    }
}

reglas_codigo = {
    "100": "Prerequisitos",
    "101": "Nulos",
    "102": "Duplicados",
    "103": "Integridad Referencial",
    "104": "Formato Fecha",
    "105": "Rango",
    "106": "Catálogo",
    "107": "Caracteres Prohibidos",
    "108": "Tipo Dato(CSV)",
    "109": "Composición",
    "110": "Longitud",
    "111": "Tipo Dato(Parquet)",
    "112": "Formato Numerico",
    "113": "Calculadora",
    "114": "Analisis Estadistico",
    "115": "Rango Fechas",
    "116": "Condicional",
    "117": "Valor en posicion especifica",
    "119": "Valor en Tendencia"
}

informacion_campos = {
    'COUNTRY_ID': 'Campo que indica el pais',
    'PROJECT': 'Nombre del proyecto al que pertenece el fichero',
    'ENTITY_ID': 'Nombre del fichero que se va a validar',
    'DOMAIN': '',
    'SUB_DOMAIN': 'Hola hola hola',
    'SEGMENT': 'HOASDDGJERD',
    'AREA': '',
    'TYPE': '',
    'PATH': '',
    'HEADER': '',
    'DELIMITER': '',
    'ACCOUNT': '',
    'ENCRYPT': '',
    'KEY': '',
    'HOST': '',
    'PORT': '',
    'DBNAME': '',
    'DBTABLE': '',
    'DBUSER': '',
    'DBPASSWORD': '',
    'TEMP_PATH': '',
    'DATA_DATE': '',
    'PARTITIONS': ''
}

