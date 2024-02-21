
import re

args = 'Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297'
name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
class_match = re.match(name_pattern, args)
class_name = class_match.group('name')
params_str = args[len(class_name):].strip()

str_pattern = r'(?P<t_str>"([^"]|\")*")'
params = params_str.split(' ')

str_pattern = r'(?P<t_str>"([^"]|\")*")'
float_pattern = r'(?P<t_float>[-+]?\d+\.\d+)'
int_pattern = r'(?P<t_int>[-+]?\d+)'
param_pattern = '{}=({}|{}|{})'.format(
            name_pattern,
            str_pattern,
            float_pattern,
            int_pattern
        )
obj_kwargs = {}
for param in params:
            # Match parameter pattern
            param_match = re.fullmatch(param_pattern, param)
            # If parameter matches pattern
            if param_match is not None:
                # Get parameter name
                key_name = param_match.group('name')
                # Get matched string value
                str_v = param_match.group('t_str')
                # Get matched float value
                float_v = param_match.group('t_float')
                # Get matched integer value
                int_v = param_match.group('t_int')
                if float_v is not None:
                    obj_kwargs[key_name] = float(float_v)
                if int_v is not None:
                    obj_kwargs[key_name] = int(int_v)
                if str_v is not None:
                    obj_kwargs[key_name] = str_v[1:-1].replace('_', ' ')
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&')
for key, value in obj_kwargs.items():
    print(key,value)
print('*******************************')

print('**************')
print(param_pattern)
print('**************')

print(type(obj_kwargs))