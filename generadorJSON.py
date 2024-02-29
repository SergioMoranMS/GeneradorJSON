import json

class GeneradorJSON:
    def __init__(self):
        self.datos = {
            "INPUT": {},
            "ERROR": {},
            "DATA": {},
            "OUTPUT": {},
            "RULES": {}
        }

    def actualizar_datos(self, datos):
        self.datos = datos

    def obtener_datos(self):
        return self.datos

    def generar_json(self, reglas):
        # Ajustar la estructura del JSON según el formato deseado
        json_data = {
            "INPUT": {
                "COUNTRY_ID": self.datos.get("country_id_input", ""),
                "PROJECT": self.datos.get("project_input", ""),
                "ENTITY_ID": self.datos.get("entity_id_input", ""),
                "DOMAIN": self.datos.get("domain_input", ""),
                "SUB_DOMAIN": self.datos.get("sub_domain_input", ""),
                "SEGMENT": self.datos.get("segment_input", ""),
                "AREA": self.datos.get("area_input", ""),
                "TYPE": self.datos.get("type_input", ""),
                "PATH": self.datos.get("path_input", ""),
                "HEADER": self.datos.get("header_input", ""),
                "DELIMITER": self.datos.get("delimiter_input", ""),
                "ACCOUNT": self.datos.get("account_input", ""),
                "KEY": self.datos.get("key_input", ""),
                "HOST": self.datos.get("host_input", ""),
                "PORT": self.datos.get("port_input", ""),
                "DATABASE_NAME": self.datos.get("dbname_input", ""),
                "DATABASE_TABLE": self.datos.get("dbtable_input", ""),
                "DATABASE_USER": self.datos.get("dbuser_input", ""),
                "DATABASE_PASSWORD": self.datos.get("dbpassword_input", ""),
                "TEMPORAL_PATH": self.datos.get("temppath_input", ""),
                "DATA_DATE": self.datos.get("data_date_input", ""),
                # "EMAIL": self.datos.get("email", [""]),
                "ENCRYPT": self.datos.get("encrypt_input", "")
            },
            "ERROR": {
                "PATH": self.datos.get("path_error", ""),
                "TYPE": self.datos.get("type_error", ""),
                "HEADER": self.datos.get("header_error", ""),
                "DELIMITER": self.datos.get("delimiter_error", ""),
                "ACCOUNT": self.datos.get("account_error", ""),
                "KEY": self.datos.get("key_error", "")
            },
            "DATA": {
                "PATH": self.datos.get("path_data", ""),
                "TYPE": self.datos.get("type_data", ""),
                "HEADER": self.datos.get("header_data", ""),
                "DELIMITER": self.datos.get("delimiter_data", ""),
                "ACCOUNT": self.datos.get("account_data", ""),
                "KEY": self.datos.get("key_data", "")
            },
            "OUTPUT": {
                "PATH": self.datos.get("path_output", ""),
                "TYPE": self.datos.get("type_output", ""),
                "HEADER": self.datos.get("header_output", ""),
                "DELIMITER": self.datos.get("delimiter_output", ""),
                "ACCOUNT": self.datos.get("account_output", ""),
                "KEY": self.datos.get("key_output", ""),
                "PARTITIONS": [
                    self.datos.get("partitions_output", "")
                    ]
            },
            "RULES": {}
        }

        for key, value in reglas.items():
            rule_data = {"FIELDS": [value.get("FIELDS", "")]}

            # Agregar todos los campos de la regla al objeto rule_data
            for field_name, field_value in value.items():
                if field_name != "FIELDS":  # Excluir el campo FIELDS de nuevo
                    rule_data[field_name] = field_value

            json_data["RULES"][key] = rule_data
    
        # Usar indent para que cada campo esté en una línea distinta
        return json.dumps(json_data, indent=2, ensure_ascii=False)
