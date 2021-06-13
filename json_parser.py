import json

class JSONParser:
    
    def __init__(self, obj, parent=None, many=False):
        self.data = obj
        self.many = False

        if not parent is None:
            self.many = False
            if not isinstance(obj, list):
                self.data = [self.data]
            self.data = self.validate(parent=True, parent_loc=parent)['data']
            # print(self.data)
        
        if not many:
            self.many = False
            self.data = [self.data]
        else:
            self.many = True

    
    def get_class_attr(self):
        var_data = dict(vars(self.__class__))
        json_fields = {key: val for key, val in var_data.items() if not key.startswith('__')}

        return json_fields

    def validate(self, parent=None, parent_loc=None):
        result_data = {}
        result_data_list = []

        json_fields = parent_loc if parent else self.get_class_attr()
        for uni_data in self.data:
            for key, val in json_fields.items():
                inner = {}
                initial = True
                prev_key = None
                val = val.strip('/ ')
                key_list = val.split('/')
                for dict_key in key_list:

                    if dict_key.startswith("$"):
                        list_idx = dict_key.split(":")

                        inner = inner if isinstance(inner, list) else uni_data
                        initial = False
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
                        if initial and dict_key in uni_data:
                            inner = uni_data[dict_key]
                            initial = False
                        elif prev_key is not None and  dict_key in inner:
                            inner = inner[dict_key]
                        else:
                            print(f'Key {dict_key} does not exists for field {key}')
                            break

                        prev_key = dict_key
                result_data[key] = inner
               
            if self.many:
                result_data_list.append(result_data)
                result_data = {}
        return result_data_list if self.many else result_data


file = open('test1.json')
data = json.load(file)

class Test(JSONParser):
    type = 'type'
    attributes = 'attributes/title'

t = Test(data, parent={'data': 'data'}, many=True)
print(t.validate())
