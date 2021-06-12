
class JSONParser:
    
    def __init__(self, obj):
        self.data = obj
    
    def validate(self):
        
        var_data = dict(vars(self.__class__))
        json_fields = {key: val for key, val in var_data.items() if not key.startswith('__')}
        result_data = {}

        for key, val in json_fields.items():

            temp_data = {}

            key_list = val.split('/')
            temp_data = self.data[key_list[0]]

            for idx in range(1, len(key_list)):
                temp_data = temp_data[key_list[idx]]
            
            result_data[key] = temp_data
        
        return result_data

class Test(JSONParser):

    name = 'name/parent/name'
    surname = 'name/surname'

d = {
    'name': {
        'parent': {
            'name': 'sanchay'
        },
        'surname': ['many are there']
    }

}

t = Test(d)
print(t.validate())

