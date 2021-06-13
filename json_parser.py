
class JSONParser:
    '''
    Usage:

    1) Create your class and inherite JSONParser.
    2) Add class variable with map value. For example: "name/first_name", this means i need first_name value from name object.
    3) Create instance of the class and pass json object.
    4) Call validate function and get your result in list or dict form.

    For example:

    class Test(JSONParser):
        first_name = "name/first_name"
        last_name = "name/last_name"
    
    json = {'name':{
        'first_name': 'ABC',
        'last_name': 'EFG'
    }}
    test_obj = Test(json)
    validated_data = test_obj.validate()

    print(validated_data)

    OUTPUT:
        {
            "first_name": "ABC",
            "last_name": "EFG"
        }
    '''
    def __init__(self, obj, many=False):
        '''
        @params
            obj: json_data
            many: whether the json data is object or list of object
        '''
        self.data = obj
        self.many = many

        '''
        If many=False then add the object to list so that it can be looped atleast
        one time in the validate function.
        '''
        if not many:
            self.data = [self.data]

    
    def get_class_attr(self):
        # get the class variable of the child class
        var_data = dict(vars(self.__class__))
        json_fields = {key: val for key, val in var_data.items() if not key.startswith('__')}

        return json_fields

    def validate(self):
        result_data = {} # used for returing the single object
        result_data_list = [] # used for returing the result when many=True

        json_fields = self.get_class_attr() 
        for uni_data in self.data: # Looping through the object
            for key, val in json_fields.items(): # getting the key and value of class variable of child class
                inner = {} # inner supporting dict
                initial = True
                prev_key = None
                val = val.strip('/ ')
                key_list = val.split('/') # sperating the keys defined in the class varibale of child class
                for dict_key in key_list:

                    if dict_key.startswith("$"): # if true we have to get the list values from the json
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
                # if self.many=True we will store our result in sepearte list or will resturn the object
                result_data_list.append(result_data)
                result_data = {}
        return result_data_list if self.many else result_data

