
class JSONParser:
    
    def __init__(self, obj):
        self.data = obj
    
    def validate(self):
        result_data = {}
        var_data = dict(vars(self.__class__))
        json_fields = {key: val for key, val in var_data.items() if not key.startswith('__')}
        
        for key, val in json_fields.items():
            inner = {}
            val = val.strip('/ ')
            key_list = val.split("/")

            initial = True
            prev_key = None
            for dict_key in key_list:

                if dict_key.startswith("$"):
                    list_idx = dict_key.split(":")
                    if isinstance(inner, list):
                        try:
                            if len(list_idx)==2:
                                inner = inner[int(list_idx[0].strip('$')):int(list_idx[1].strip('$'))]
                            elif len(list_idx)==1:
                                inner = inner[int(list_idx[0].strip('$'))]
                            else:
                                print(f"More than 2 index provided in field {key}")
                        except Exception as e:
                            print(e)
                            break
                    else:
                        print(f"Value of {prev_key} is not a list for field {key}")
                        break
                else:
                    if initial and dict_key in self.data:
                        inner = self.data[dict_key]
                        initial = False
                    elif prev_key is not None and  dict_key in inner:
                        inner = inner[dict_key]
                    else:
                        print(f'Key {dict_key} does not exists for field {key}')
                        break

                    prev_key = dict_key

            result_data[key] = inner
        return result_data

class Test(JSONParser):

    name = 'name/parent/name'
    sur =  'name/surname/$1:$3'

d = {
    'name': {
        'parent': {
            'name': 'sanchay'
        },
        'surname': ['many are there', 't', 'c']
    }

}

t = Test(d)
print(t.validate())

