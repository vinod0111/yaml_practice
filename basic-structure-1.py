import yaml

my_file = "basic-structure-1.yaml"

with open(my_file, 'r', encoding='utf8') as stream:

    try:
        data = yaml.safe_load(stream)
        for key, value in data.items():
            print(f"KEY : {key}")
            print(f"VALUE : {value}")
            
    except yaml.YAMLError as err:
        print(err)