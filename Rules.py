class Rules:
    def __init__(self):
        self.rule_dict = {}

    def add_rule(self, rules_name, rule_data):
        # Generar un nombre único para la regla 
        count = 1
        rule_name = f"{rules_name}.{count}"
        # Verificar si el nombre ya está en uso y agregar sufijo
        while rule_name in self.rule_dict:
            count += 1
            rule_name = f"{rules_name}.{count}"

        self.rule_dict[rule_name] = rule_data
        
        rules_list = list(self.rule_dict.keys())

        return rules_list

    #Aun por definir
    def remove_rule(self):
        return self
    
    def rule_list(self):
        return list(self.rule_dict.keys())
 

    def get_rules(self):
        return self.rule_dict
