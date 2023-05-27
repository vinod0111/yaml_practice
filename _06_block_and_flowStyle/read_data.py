import yaml

# my_file = "block_1.yml"
my_file = "flow_1.yml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            
            print(f"KEY : {key}")
            print(f"VALUE : {value}")
            dt = type(value)
            print(f"Data type od {value} is {dt}")
            
    except yaml.YAMLError as err:
        print(err)