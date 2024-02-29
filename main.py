 #Nuevo código FLASK
from flask import Flask, render_template, request, jsonify, Response
from generadorJSON import *
from Rules import *
from reglas_calidad import *

app = Flask(__name__)
generador = GeneradorJSON()
reglas = Rules()

# Configuración para servir archivos estáticos desde la carpeta 'Styles'
app.static_folder = 'Styles'

input_form_data = {
    'country_id': '',
    'project': '',
    'entity_id': '',
    'domain': '',
    'sub_domain': '',
    'segment': '',
    'area': '',
    'type': '',
    'path': '',
    'header': '',
    'delimiter': '',
    'account': '',
    'encrypt': '',
    'key': '',
    'Host': '',
    'Port': '',
    'DBName': '',
    'DBTable': '',
    'DBUser': '',
    'DBPassword': '',
    'TempPath': '',
    'data_date': '',
#  'email': '',
    'valuesTypeInput' : ['csv', 'delta', 'parquet', 'prod_csv', 'prod_parquet', 'postgre', 'mysql', 'teradata', 'synapse', 'oracle', 'sqlserver'],
}

error_form_data = {
    'path_error': '',
    'type_error': '[TRUE, FALSE]',
    'header_error': '',
    'delimiter_error': '',
    'account_error': '',
    'key_error': '',
    'valuesTypeError': ['delta', 'csv', 'prod_csv'],
}

data_form_data = {
    'path_data': '',
    'type_data': '',
    'header_data': '',
    'delimiter_data': '',
    'account_data': '',
    'key_data': '',
    'valuesTypeData': ['delta', 'csv', 'prod_csv'],
}

output_form_data = {
    'output_path': '',
    'output_type': '',
    'output_header': '',
    'output_delimiter': '',
    'output_account': '',
    'output_key': '',
    'output_partitions': '',
    'valuesTypeOutput': ['delta', 'csv', 'prod_csv'], 
}

# Juntar todos los diccionarios en uno solo
form_data = {
'input_form': input_form_data,
'error_form': error_form_data,
'data_form': data_form_data,
'output_form': output_form_data,
'rules_form': dic_reglas_JSON,
}


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input')
def input_section():
    # Renderizar la plantilla 'input.html' y pasar el diccionario como contexto
    return render_template('input.html', **form_data)

@app.route('/rules')
def rules_section():
    # Renderizar la plantilla 'rules.html' y pasar el diccionario como contexto
    return render_template('rules.html', **form_data)


@app.route('/generadorJSON', methods=['POST'])
def generate_json():
    try:
     # Obtener los datos del formulario de la sección actual
     form_data = request.form
     # Actualizar los datos en el generador
     generador.actualizar_datos(form_data)

     # Generar el JSON con los datos de la sección actual
     generated_json = generador.generar_json(reglas.get_rules())
     pruebas = reglas.get_rules()
     #limpiar estructura
     return jsonify({'generated_json': generated_json})
     
    except Exception as e:
        app.logger.error(f'Error en generadorJSON: {str(e)}')
        return jsonify({'error': str(e)}), 500
        # return jsonify({'error': 'Error generating JSON'}), 500
    
@app.route('/guardar_regla', methods=['POST'])
def guardar_regla():
    try:
        # Recupera los datos enviados desde el cliente
        data = request.json

        nombre = data.get('datosRegla').get('codigo')
        datos = data.get('datosRegla').get('parametros')

        # Actualiza el diccionario 'parametros' en dic_reglas
        rules_list = reglas.add_rule(nombre, datos)

        # Puedes enviar una respuesta si es necesario
        return jsonify({'mensaje':'Regla guardada exitosamente','reglas':rules_list})
    except Exception as e:
        return jsonify({'error': 'Error al guardar la regla'}), 500
    
@app.route('/cargar_reglas')
def cargar_reglas():
    try:
        rules = reglas.rule_list()
        return jsonify({'reglas': rules, 'codigos_nombres_reglas': reglas_codigo})
        # return jsonify(rules)
    except Exception as e:
        return jsonify({'error': 'Error al cargar las reglas'}), 500
    
@app.route('/regla/<rule>')
def regla_page(rule):
    return render_template('showRule.html', **form_data, rule=rule)

@app.route('/get_campos_info')
def get_campos_info():
    return jsonify(informacion_campos)

if __name__ == '__main__':
     app.run(debug=True)
